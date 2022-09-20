/*
  Arduino LSM9DS1 - Simple Accelerometer

  This example reads the acceleration values from the LSM9DS1
  sensor and continuously prints them to the Serial Monitor
  or Serial Plotter.

  The circuit:
  - Arduino Nano 33 BLE Sense

  created 10 Jul 2019
  by Riccardo Rizzo

  This example code is in the public domain.
*/
#include <Arduino.h>
#include <Arduino_LSM9DS1.h>


void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  /*Accelerometer initiation*/
  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Acceleration in G's");
  Serial.println("X\tY\tZ");

  /*Magnetometer initiation*/
  Serial.print("Magnetic field sample rate = ");
  Serial.print(IMU.magneticFieldSampleRate());
  Serial.println(" uT");
  Serial.println();
  Serial.println("Magnetic Field in uT");
  Serial.println("X\tY\tZ");
}

void loop() {
  /*Accelerometer data x,y,z*/
  float x, y, z;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);

  Serial.print(x);
  Serial.print(','); 
  Serial.print(y); 
  Serial.print(','); 
  Serial.print(z);
  Serial.print(',');

  }
  delay(10);

  /*Magnetometer data Bx,By,Bz*/
  float Bx, By, Bz;

  if (IMU.magneticFieldAvailable()) {
    IMU.readMagneticField(Bx, By, Bz);

  Serial.print(Bx);
  Serial.print(','); 
  Serial.print(By); 
  Serial.print(','); 
  Serial.println(Bz);
  }

  delay(100);


}
