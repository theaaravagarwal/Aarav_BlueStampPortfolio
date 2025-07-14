#include <Wire.h>                         //i2c 
#include <Adafruit_AHRS_NXPFusion.h>      //ahrs
#include <FS.h>                           //filesys
#include <SPIFFS.h>                       //spiffs
#include <math.h>                         //math
#include <vector>                         //dynamic arr
#include "pedometer.h"                    //step counter class
#include "bluetooth.h"                    //custom bluetooth
#define USE_MATH_DEFINES                  //math definitions
#define vec vector
#define pb push_back
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned int ui;
typedef long double ld;
typedef long long ll;
typedef long l;
const double G = 9.851400755649225;       //gravity, std = 9.80665 but for sf its 9.851400755649225

//accelerometer config
Adafruit_LSM6DS3TRC lsm6ds3trc;           //accelerometer/gyro sensor
Adafruit_LIS3MDL lis3mdl;                 //magnetometer sensor

//sensor config
const int fsr = 36;                       //fsr pin

#define FSR_WINDOW_SIZE 10                //num of samples in the window (time=size*delay) (Ex. 10 samples, 100ms delay = 1s window)
float fsrwin[FSR_WINDOW_SIZE];            //window array to store fsr values
int fsridx = 0;                           //ptr to the curr idx in the window
bool fsrfwin = false;                     //if the window is full

//buzzer config
const int buzzer = 25;                    //buzzer pin

const int ledcch = 0;                     //the led control channel
const int ledct = 0;                      //the led control time
const int ledcres = 8;                    //the led control resolution

//modules
Adafruit_NXPSensorFusion ahrs;            //ahrs filter
Pedometer pd(0.8, 200);                   //step counter
BluetoothSerial bt;                       //bluetooth serial

bool sound = 0;                           //play sound on buzzer
bool ble = 1;                             //print data to bluetooth
bool once = 0;                            //print legend only once

//movement detection
bool ismov = 0;                           //flag
ul lupd = 0;                              //ms

//dist tracking
float stlen = 0.7f;                       //default in meters
float d = 0.0f;
int lstpc = 0;

//funcs
void playTone(int freq) {ledcWriteTone(ledcch, freq);}
void stopTone() {ledcWriteTone(ledcch, 0);}

void setup() {
  Serial.begin(115200); delay(1000); bt.begin();
  if (!ledcSetup(ledcch, 2000, ledcres)) {Serial.println("Failed to setup LEDC"); while (1) delay(10);} ledcAttachPin(buzzer, ledcch);
  if (!SPIFFS.begin(true)) {Serial.println("SPIFFS Mount Failed"); while (1) delay(10);}
  if (!lsm6ds3trc.begin_I2C()) {Serial.println("Failed to find LSM6DS3TRC chip"); while (1) delay(10);} Serial.println("LSM6DS3TRC Found!");
  if (!lis3mdl.begin_I2C()) {Serial.println("Failed to find LIS3MDL chip"); while (1) delay(10);} Serial.println("LIS3MDL Found!");
  ahrs.begin(100.0f);
  lupd = millis();
}

void loop() {
  static ul lwr = 0;
  sensors_event_t accel, gyro, temp, mag;
  lsm6ds3trc.getEvent(&accel, &gyro, &temp);
  lis3mdl.getEvent(&mag);
  ul now = millis();
  float dt = (now-lupd)/1000.0f;
  lupd = now;

  ahrs.update(
    gyro.gyro.x*180.0f/PI,
    gyro.gyro.y*180.0f/PI,
    gyro.gyro.z*180.0f/PI,
    accel.acceleration.x/G,                         //convert m/s^2 to g
    accel.acceleration.y/G,
    accel.acceleration.z/G,
    mag.magnetic.x*G,                               //so we had a magnetometer LOL
    mag.magnetic.y*G,                               //this fixes so much its insane
    mag.magnetic.z*G
  );

  float roll = ahrs.getRoll();
  float pitch = ahrs.getPitch();
  float yaw = ahrs.getYaw();

  float gx, gy, gz;
  ahrs.getGravityVector(&gx, &gy, &gz);

  float lax, lay, laz;
  ahrs.getLinearAcceleration(&lax, &lay, &laz);
  lax*=G; lay*=G; laz*=G;

  float linmag = sqrt(lax*lax+lay*lay+laz*laz);

  sensors_event_t lin_accel = accel;
  lin_accel.acceleration.x = lax;
  lin_accel.acceleration.y = lay;
  lin_accel.acceleration.z = laz;

  pd.update(lin_accel);

  //estimate distance
  int stpc = pd.getStepCount();
  static float mxlinmag = 0.0f;                       //this block is same thing as the pedometer.h file but for stride
  if (linmag>mxlinmag) mxlinmag = linmag;
  if (stpc>lstpc) {
    float dst = 0.45f+0.25f*(mxlinmag/G-1.0f);        //formula: base+scale*(peak accel-1g)
    if (dst<0.3f) dst = 0.3f;                         //lower bound
    if (dst>1.2f) dst = 1.2f;                         //upper bound
    stlen = dst;
    int stptk = stpc-lstpc;
    d+=stptk*stlen;
    lstpc = stpc;
    mxlinmag = 0.0f;
  }

  //movement detection
  static float lroll = roll, lpitch = pitch;
  const float EULER_MOVEMENT_THRESHOLD = 15.0f;        //deg
  float droll = fabs(roll-lroll);
  float dpitch = fabs(pitch-lpitch);

  if (droll>EULER_MOVEMENT_THRESHOLD||dpitch>EULER_MOVEMENT_THRESHOLD) {
    if (!ismov) {
      ismov = 1;
      if (ble) bt.println("Movement detected");
    }
  } else {
    if (ismov) {
      ismov = 0;
      if (ble) bt.println("Not moving");
    }
  }
  lroll = roll; lpitch = pitch;

  int fsrvl = analogRead(fsr);                        //0-4095
  fsrwin[fsridx++] = fsrvl;
  if (fsridx>=FSR_WINDOW_SIZE) {
    fsridx = 0; fsrfwin = true;
  }

  float fsravg = 0, fsrvr = 0;
  int n = fsrfwin?FSR_WINDOW_SIZE:fsridx;
  for (int i=0; i<n; i++) fsravg+=fsrwin[i];
  fsravg/=n;
  for (int i=0; i<n; i++) fsrvr+=(fsrwin[i]-fsravg)*(fsrwin[i]-fsravg);
  fsrvr/=n;

  bool fsrstable = true;
  for (int i=0; i<n; i++) {
    if (abs(fsrwin[i]-fsrvl)>500) {
      fsrstable = false;
      break;
    }
  }
  if (fsrstable&&fsrfwin) {
    for (int i=0; i<FSR_WINDOW_SIZE; i++) fsrwin[i] = fsrvl;
    fsravg = fsrvl;
    fsrvr = 0;
  }

  const float FSR_VAR_THRESHOLD = 175175.0f;    //tune later
  if (fsrfwin&&fsrvr>FSR_VAR_THRESHOLD) if (sound) playTone(750);
  else stopTone();

  //bluetooth logging
  if (ble) {
    String blestr = String(now)+","+String(roll,1)+","+String(pitch,1)+","+String(yaw,1)+","+
                    String(stpc)+","+String(stlen,2)+","+String(d,2)+","+
                    String(fsrvl)+","+String(fsrvr,0)+","+
                    String(accel.acceleration.x,2)+","+String(accel.acceleration.y,2)+","+String(accel.acceleration.z,2)+","+
                    String(linmag,2)+","+
                    String(gx*G,2)+","+String(gy*G,2)+","+String(gz*G,2)+","+
                    String(gyro.gyro.x,2)+","+String(gyro.gyro.y,2)+","+String(gyro.gyro.z,2)+","+
                    String(temp.temperature,2)+"\n";
    if (!once) {bt.println("time,roll,pitch,yaw,steps,stride,dist,fsr,fsrvar,ax,ay,az,linmag,gravx,gravy,gravz,gx,gy,gz,temp"); once = 1;}
    bt.print(blestr);
  }

  delay(100);                                  //delay to avoid death
}

