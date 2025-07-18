#include <Wire.h>                         //i2c 
#include <Adafruit_AHRS_NXPFusion.h>      //ahrs
#include <FS.h>                           //filesys
#include <SPIFFS.h>                       //spiffs
#include <stdio.h>                        //stdio
#include <stdlib.h>                       //stdlib
#include <time.h>                         //time
#include <math.h>                         //math
#include <vector>                         //dynamic arr
#include <string>                         //c++ string
#include <unordered_map>                  //hash_map
#include <random>                         //for dice and flip
#include <limits.h>                       //for LLONG_MAX/INT_MAX
#include "pedometer.h"                    //step counter class
#include "bluetooth.h"                    //custom bluetooth
#define USE_MATH_DEFINES                  //math definitions
#define vec vector
#define str string
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define fi first
#define se second
#define fr front
#define bk back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) (int)(x).size()
#define rep(i, st, end) for (int i=(st); i<(end); i++)
#define arrin(a) for (auto &x:(a)) cin>>x
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front
#define uset unordered_set
#define umap unordered_map
#define umset unordered_multiset
#define hmap hash_map
#define hmset hash_multiset
#define hset hash_set
#define mset multiset
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned int ui;
typedef long double ld;
typedef long long ll;
typedef long l;
const double G = 9.851400755649225;       //gravity, std = 9.80665 but for sf its 9.851400755649225
const int del = 50;                       //main loop delay in ms
const int MOD = 1e9+7;                    //fib mod
std::random_device rd;                    //nondeterministic random num gen (for seeding)
std::mt19937 gen(rd());                   //generator of 32 bit nums with a state size of 19937 bits

//accelerometer config
Adafruit_LSM6DS3TRC lsm6ds3trc;           //accelerometer/gyro sensor
Adafruit_LIS3MDL lis3mdl;                 //magnetometer sensor
float linmag;                             //the linear magnitude of the accelerometer
float ax, ay, az;                         //unfiltered acceleration vector components
float gyx, gyy, gyz;                      //gyro angular velocity vector components

//sensor config
const int fsr = 36;                       //fsr pin 

#define FSR_WINDOW_SIZE 10                //num of samples in the window (time=size*delay) (Ex. 10 samples, 100ms delay = 1s window)
float fsrwin[FSR_WINDOW_SIZE];            //window array to store fsr values
int fsridx = 0;                           //ptr to the curr idx in the window
bool fsrfwin = 0;                         //if the window is full
int fsrvl;                                //current fsr value
float fsrvr;                              //current fsr variance

//buzzer config
const int buzzer = 25;                    //buzzer pin

const int ledcch = 0;                     //the led control channel
const int ledct = 0;                      //the led control time
const int ledcres = 8;                    //the led control resolution

//ahrs stuff
Adafruit_NXPSensorFusion ahrs;            //ahrs filter
float gx, gy, gz;                         //gravity vector components
float roll, pitch, yaw;                   //euler angles for orientation

//pedometer stuff
Pedometer pd(0.8, 200);                   //step counter
int stpc = 0;                             //the current step count

//bluetooth stuff
BluetoothSerial bt;                       //bluetooth serial

//i had no where else to put temperature
float tmp;

//matrix stuff
struct Matrix {
  ll m[2][2];
  Matrix operator*(const Matrix& b) const {
    Matrix res = {};
    for (int i=0; i<2; i++) for (int j=0; j<2; j++) for (int k=0; k<2; k++) res.m[i][j] = (res.m[i][j]+m[i][k]*b.m[k][j])%MOD;
    return res;
  }
};
Matrix matpow(Matrix b, ll e) {
  Matrix res = {{{1, 0}, {0, 1}}};
  while (e>0) {
    if (e%2==1) res = res*b;
    b = b*b;
    e/=2;
  }
  return res;
}

//cli command stuff
struct Command {
  const char* name;
  void (*func)(const String& args);
};

//cli function prototypes
void help(const String& args);
void getSteps(const String& args);
void getDist(const String& args);
void getFsrVal(const String& args);
void getAccel(const String& args);
void getGrav(const String& args);
void getGyro(const String& args);
void getOrient(const String& args);
void getTemp(const String& args);
void getFsrVar(const String& args);
void getLinMag(const String& args);
void getTime(const String& args);
void dice(const String& args);
void flip(const String& args);
void ee(const String& args);
void toggle(const String& args);
void fib(const String& args);

Command cmd[] = {                         //to register more commands just make new entries here <"name", function>
  {"help", help},                         //function parameter = const String& args and must be return type void
  {"steps", getSteps},
  {"distance", getDist},
  {"force", getFsrVal},
  {"gravity", getGrav},
  {"gyro", getGyro},
  {"orient", getOrient},
  {"temp", getTemp},
  {"forcevar", getFsrVar},
  {"linmag", getLinMag},
  {"accel", getAccel},
  {"time", getTime},
  {"dice", dice},
  {"flip", flip},
  {"toggle", toggle},
  {"fib", fib},
  {"ee", ee},
};
const int cmdc = sizeof(cmd)/sizeof(cmd[0]);

//flags
bool sound = 0;                           //play sound on buzzer
bool ble = 0;                             //print data to bluetooth
bool once = 0;                            //print legend only once
bool cli = 1;                             //create cli

//movement detection
bool ismov = 0;                           //are we moving flag
ul lupd = 0;                              //last update time ms

//dist tracking
float stlen = 0.7f;                       //default stride length in meters
float d = 0.0f;                           //distance travelled so far
int lstpc = 0;                            //last step count

//funcs
void playTone(int freq) {ledcWriteTone(ledcch, freq);}
void stopTone() {ledcWriteTone(ledcch, 0);}
ll stoll(const String& s) {               //convert an Arduino String to a long long (can be used for unsigned ints)
  ll res = 0;                             //resultant long long
  int sn = 1;                             //signage
  int i = 0;                              //where in the string are we
  while (s[i]==' '||s[i]=='\t'||s[i]=='\n'||s[i]=='\r'||s[i]=='\f'||s[i]=='\v') i++; //if its ANYTHING other than 0-9 we skip
  if (s[i]=='-') {sn = -1; i++;}          //if its neg swap sign
  else if (s[i]=='+') i++;                //if its positive dont do anything
  while (s[i]>='0'&&s[i]<='9') {          //if curr num is 0-9
    if (res>(LONG_LONG_MAX/10)||(res==(LONG_LONG_MAX/10)&&(s[i]-'0')>(LONG_LONG_MAX%10))) {
      res = LONG_LONG_MAX;                //if we have overflow, return llong_max
    }
    res = res*10+(s[i]-'0'); i++;         //we just basically do a push_back to the ll ex. s[i] = 9, and res = 10; res = 109
  }
  return sn*res;                          //return the proper signed number since we're converting a signed num
}

//cli funcs
void help(const String& args) {
  if (args.length()==0) {
    String res = "";
    bt.println("Available commands:");
    for (int i=0; i<cmdc-1; i++) {
      if (String(cmd[i].name)=="ee") continue;
      res+="- "+String(cmd[i].name)+"\n";
    }
    bt.println(res);
    return;
  }
  if (args=="steps") bt.println("steps: prints your current step count");
  else if (args=="distance") bt.println("distance: prints how far you've walked (in meters)");
  else if (args=="force") bt.println("force: prints the pressure on your foot (normalized)");
  else if (args=="help") bt.println("help [cmd]: lists commands or gives info about a specific command");
  else if (args=="temp") bt.println("temp: prints temperature data");
  else if (args=="accel") bt.println("accel: prints acceleration vector");
  else if (args=="gyro") bt.println("gyro: prints gyroscope vector");
  else if (args=="gravity") bt.println("grav: prints gravity vector");
  else if (args=="orient") bt.println("orient: prints roll, pitch, and yaw");
  else if (args=="linmag") bt.println("linmag: prints linear acceleration magnitude");
  else if (args=="forcevar") bt.println("fsrvar: prints variance in foot pressure");
  else if (args=="time") bt.println("time: prints time since boot");
  else if (args=="dice") bt.println("dice <n>: prints the outcome of rolling n dice");
  else if (args=="flip") bt.println("flip <n>: prints the outcome of n flipped coins");
  else if (args=="toggle") bt.println("toggle: toggles ble or sound (usage: toggle sound/ble)");
  else if (args=="fib") bt.println("fib <n>: prints the nth Fibonacci number");
  else bt.println("Unknown command '"+args+"'. Try 'help'.");
}
void getTemp(const String& args) {
  bt.println("Temperature is " + String(tmp)+" °C");
}
void getAccel(const String& args) {
  bt.println("Accel (x,y,z): ("+String(ax)+", "+String(ay)+", "+String(az)+")");
}
void getGyro(const String& args) {
  bt.println("Gyro (x,y,z): ("+String(gyx)+", "+String(gyy)+", "+String(gyz)+")");
}
void getGrav(const String& args) {
  bt.println("Gravity (x,y,z): ("+String(gx) + ", "+String(gy)+", "+String(gz)+")");
}
void getOrient(const String& args) {
  bt.println("Orientation (roll, pitch, yaw): ("+String(roll)+", "+String(pitch)+", "+String(yaw)+")");
}
void getLinMag(const String& args) {
  bt.println("Linear accel magnitude: "+String(linmag));
}
void getFsrVar(const String& args) {
  bt.println("FSR variance: "+String(fsrvr));
}
void getTime(const String& args) {
  bt.println("Current time: "+String(millis())+" ms since boot");
}
void getSteps(const String& args) {
  bt.println("You have taken "+String(stpc)+" steps.");
}
void getDist(const String& args) {
  bt.println("You have travelled "+String(d)+" meters");
}
void getFsrVal(const String& args) {
  bt.println("You are putting "+String(fsrvl/4095.0)+"% force on the outside of your foot.");
}
void flip(const String& args) {
  ll n = 1;
  if (args!="") n = stoll(args);
  ll h = 0, t = 0;
  std::uniform_int_distribution<int> rng(0, 9);
  for (int i=0; i<n; i++) {
    if (rng(gen)<4) h++;
    else t++;
  }
  if (n==1) {bt.println(h==1?"Heads":"Tails"); return;}
  bt.println("H: "+String(h)+" T: "+String(t));
}
void dice(const String& args) {
  ll n = 1;
  if (args!="") n = stoll(args);
  int m[6] = {};                          //we use this for tallying cuz O(1) insert
  std::uniform_int_distribution<int> rng(1, 6);
  for (int i=0; i<n; i++) {
    int d = rng(gen);
    m[d-1]++;
  }
  String res = "";
  for (int i=0; i<6; i++) res+=String(i+1)+": "+String(m[i])+"\n";
  bt.println(res);
}
void toggle(const String& args) {
  if (args=="sound") {sound^=1; bt.println("Sound is now "+String(sound?"on":"off"));}
  else if (args=="ble") {ble^=1; bt.println("Ble is now "+String(ble?"on":"off"));}
  else return;
}
void ee(const String& args) {
  int mx = args.toInt(); 
  if (mx==0) mx = 100;
  std::uniform_int_distribution<int> rng(1, mx);
  bt.println(rand()%mx);
}
void fib(const String& args) {            //https://usaco.guide/plat/matrix-expo
  ll n = stoll(args);                     //most memory/time efficient way I could think of
  if (n<=1) {bt.println(n); return;}
  Matrix b = {{{1, 1}, {1, 0}}};
  Matrix res = matpow(b, n-1);
  bt.println(res.m[0][0]);
}
void initcli(bool& st) {
  if (!st) return;
  //normally id use vec<pair<str, std::function<void()>>> 
  //as the type for this kind of map but thats a little annoying here
  //since vecs can cause memory leaks/bad alloc on an esp
  //so we just make a dedicated data structure for commands 🗣️🗣️🗣️
  for (int i=0; i<cmdc; i++) bt.addCommand(cmd[i].name, cmd[i].func);
}

void setup() {
  Serial.begin(115200); delay(1000); bt.begin();
  Serial.print("Free heap (before): ");
  Serial.println(ESP.getFreeHeap());
  if (!ledcSetup(ledcch, 2000, ledcres)) {Serial.println("Failed to setup LEDC"); while (1) delay(10);} ledcAttachPin(buzzer, ledcch);
  if (!SPIFFS.begin(1)) {Serial.println("SPIFFS Mount Failed"); while (1) delay(10);}
  if (!lsm6ds3trc.begin_I2C()) {Serial.println("Failed to find LSM6DS3TRC chip"); while (1) delay(10);} Serial.println("LSM6DS3TRC Found!");
  if (!lis3mdl.begin_I2C()) {Serial.println("Failed to find LIS3MDL chip"); while (1) delay(10);} Serial.println("LIS3MDL Found!");
  ahrs.begin(1000.0f/del);
  initcli(cli);
  Serial.print("Free heap (after): ");
  Serial.println(ESP.getFreeHeap());
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
    mag.magnetic.y*G,
    mag.magnetic.z*G
  );

  roll = ahrs.getRoll();
  pitch = ahrs.getPitch();
  yaw = ahrs.getYaw();

  ahrs.getGravityVector(&gx, &gy, &gz);

  float lax, lay, laz;
  ahrs.getLinearAcceleration(&lax, &lay, &laz);
  lax*=G; lay*=G; laz*=G;

  linmag = sqrt(lax*lax+lay*lay+laz*laz);

  sensors_event_t lin_accel = accel;
  lin_accel.acceleration.x = lax;
  lin_accel.acceleration.y = lay;
  lin_accel.acceleration.z = laz;

  pd.update(lin_accel);

  //estimate distance
  stpc = pd.getStepCount();
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
  const float emthr = 15.0f;                          //deg
  float droll = fabs(roll-lroll);
  float dpitch = fabs(pitch-lpitch);

  if (droll>emthr||dpitch>emthr) {
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

  fsrvl = analogRead(fsr);                            //0-4095
  fsrwin[fsridx++] = fsrvl;
  if (fsridx>=FSR_WINDOW_SIZE) {
    fsridx = 0; fsrfwin = 1;
  }

  float fsravg = 0; fsrvr = 0;
  int n = fsrfwin?FSR_WINDOW_SIZE:fsridx;
  for (int i=0; i<n; i++) fsravg+=fsrwin[i];
  fsravg/=n;
  for (int i=0; i<n; i++) fsrvr+=(fsrwin[i]-fsravg)*(fsrwin[i]-fsravg);
  fsrvr/=n;

  bool fsrstable = 1;
  for (int i=0; i<n; i++) {
    if (abs(fsrwin[i]-fsrvl)>500) {
      fsrstable = 0;
      break;
    }
  }
  if (fsrstable&&fsrfwin) {
    for (int i=0; i<FSR_WINDOW_SIZE; i++) fsrwin[i] = fsrvl;
    fsravg = fsrvl;
    fsrvr = 0;
  }

  const float FSR_VAR_THRESHOLD = 175175.0f;          //tune later
  if (fsrfwin&&fsrvr>FSR_VAR_THRESHOLD) if (sound) playTone(750);
  else stopTone();

  static int ffc = 0;
  const int ffthr = 4095, ffdc = 10;
  if (fsrfwin) {
    if (fsrvl<ffthr) {
      ffc++;
      if (ffc>ffdc&&fsrvr!=0) {
        if (ble) bt.println("Put more pressure on the outside of your foot");
        ffc = 0;
      }
    } else ffc = 0;
  }

  float mx = mag.magnetic.x, my = mag.magnetic.y;
  float hd = atan2(my, mx);
  hd = hd*(180/PI);                                   //heading in degrees

  tmp = temp.temperature;

  Serial.print("Free heap (at "+String(now)+"): "+String(ESP.getFreeHeap())+"\n");

  // Serial.println("time,roll,pitch,yaw,steps,stride,dist,fsr,fsrvar,ax,ay,az,linmag,gravx,gravy,gravz,gx,gy,gz,mx,my,mz,temp");
  // String output = String(now)+","+String(roll,1)+","+String(pitch,1)+","+String(yaw,1)+","+
  //                   String(stpc)+","+String(stlen,2)+","+String(d,2)+","+
  //                   String(fsrvl)+","+String(fsrvr,0)+","+
  //                   String(accel.acceleration.x,2)+","+String(accel.acceleration.y,2)+","+String(accel.acceleration.z,2)+","+
  //                   String(linmag,2)+","+
  //                   String(gx*G,2)+","+String(gy*G,2)+","+String(gz*G,2)+","+
  //                   String(gyro.gyro.x,2)+","+String(gyro.gyro.y,2)+","+String(gyro.gyro.z,2)+","+
  //                   String(mag.magnetic.x)+","+String(mag.magnetic.y)+","+String(mag.magnetic.z)+","+String(temp.temperature,2)+"\n";
  // Serial.print(output);
  //   s q u a r e

  // if (ble) {
  //   String out = "FSR Value: "+String(fsrvl)+", FSR Variance: "+String(fsrvr, 2)+", Step Count: "+String(stpc)+", Stride Length: "+String(stlen, 2)+", Distance: "+String(d, 2)+", Linear Acceleration:"+String(linmag, 2);
  //   bt.println(out);
  // }

  //bluetooth logging
  if (ble) {                                 //dev logging
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

  delay(del);                                //delay to avoid death
}
