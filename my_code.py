#!/usr/bin/python3
#!/usr/bin/env python

import ev3dev.ev3 as ev3
import signal
import numpy as np


# Connect two motors and two (different) light sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in2')

lightSensorFront = ev3.LightSensor('in3')
US = ev3.UltrasonicSensor('in4')

BASE_SPEED = 30
TURN_SPEED = 80

mA.run_direct()
mB.run_direct()

lightSensorRight.mode = 'COL-COLOR'
lightSensorLeft.mode = 'COL-COLOR'
lightSensorFront.mode = 'REFLECT'

map = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 2, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 2, 1, 2, 1, 2, 0],
               [0, 1, 1, 0, 1, 0, 0], [0, 1, 3, 2, 1, 1, 0], [0, 0, 0, 1, 3, 1, 0], [0, 0, 0, 1, 0, 1, 0],
               [0, 1, 3, 3, 1, 1, 0], [0, 1, 3, 9, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

def forward():
    while True:
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color

        if sensorLeft == 6 and sensorRight == 6:
            mA.duty_cycle_sp = BASE_SPEED
            mB.duty_cycle_sp = BASE_SPEED
        else:
            mA.duty_cycle_sp = 0
            mB.duty_cycle_sp = 0
            break


def reverse():
    while True:
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color
        if sensorLeft == 1 and sensorRight == 1:
            mA.polarity = "inversed"
            mB.polarity = "inversed"
            mA.duty_cycle_sp = BASE_SPEED
            mB.duty_cycle_sp = BASE_SPEED
        elif sensorLeft == 6 and sensorRight == 6:
            mA.polarity = "normal"
            mB.polarity = "normal"
            mA.duty_cycle_sp = BASE_SPEED
            mB.duty_cycle_sp = BASE_SPEED
            if sensorLeft == 1 and sensorRight == 1:
                mA.duty_cycle_sp = 0
                mB.duty_cycle_sp = 0
                break


def sensor_read():
    while True:
        #us_readings = US.distance_centimeters_continuous
        sensorFront = lightSensorFront.value()

        #print("Ultrasound    " + US_readings)
        print("SensorFront   " + sensorFront)




def forwardSF():
    while True:
        sensorFront = lightSensorFront.value()
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color

        if sensorLeft == 6 and sensorRight == 6:
            mA.duty_cycle_sp = BASE_SPEED
            mB.duty_cycle_sp = BASE_SPEED
        elif sensorFront > 300  and sensorFront < 400:
            mA.duty_cycle_sp = 0
            mB.duty_cycle_sp = 0
            break






while true:
   sensorLeft = lightSensorLeft.color
   sensorRight = lightSensorRight.color
   if (sensorLeft==1 and sensorRight==1):
      reverse();


