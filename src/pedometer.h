#pragma once
#include <Arduino.h>
#include <Adafruit_LSM6DS3TRC.h>
#include <Adafruit_LIS3MDL.h>
typedef unsigned long ul;

class Pedometer {
public: 
    Pedometer(float baseThreshold = 1.2f, ul minStepInterval = 250)
        : stpc(0), lstpt(0), bthr(baseThreshold), mstpint(minStepInterval),
          lmag(0.0f), pmag(0.0f), a(0.9f), g(0.0f), sum(0.0f), cnt(0) {}

    void update(const sensors_event_t& accel) {
        float mag = sqrt(accel.acceleration.x*accel.acceleration.x+accel.acceleration.y*accel.acceleration.y+accel.acceleration.z*accel.acceleration.z);
        g = a*g+(1-a)*mag; //lp filter for g
        float fmag = mag-g; //hp filter
        sum+=fabs(fmag), cnt++; //sum up mags for avging
        if (cnt>=50) {
            float avg = sum/cnt; //take avg
            thr = bthr+avg*0.2f; //dynamic threshold based on the avg
            sum = 0.0f; cnt = 0; //reset for next avg
        }
        ul now = millis(); //curr time
        static float lvall = 0.0f; //no valley at start
        static bool detvall = false; //flag for valley detection
        static float lpeak = 0.0f; //no peak at start
        if (pmag>lmag&&lmag<fmag&&lmag<-thr*0.5f) {lvall = lmag; detvall = true;} //if we have a valley then keep it
        bool peak = (pmag<lmag)&&(lmag>fmag)&&(lmag>thr); //check if we have a peak
        bool okamp = (lmag-lvall)>(thr*0.5f); //check if amp is above threshold
        if (peak&&okamp&&(now-lstpt)>mstpint&&detvall) {
            lstpt = now, stpc++; //step detected, upd last step time
            detvall = false; //reset valley detection
            lpeak = lmag; //store peak for next loop
        }
        pmag = lmag; lmag = fmag; //update prev and last mag
    }
    uint32_t getStepCount() const {return stpc;} //to get step count
    void reset() {stpc = 0;} //to reset step count

private:
    uint32_t stpc;      //step count
    ul lstpt;           //last step time
    float bthr;         //base threshold
    float thr = 1.2f;   //current threshold
    ul mstpint;         //minimum step interval in ms
    float lmag, pmag;   //last and previous magnitude
    float a;            //alpha for low-pass filter
    float g;            //gravity component
    float sum;          //sum of magnitudes for averaging
    int cnt;            //count of magnitudes for averaging
};
