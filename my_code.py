#!/usr/bin/python3
#!/usr/bin/env python

import ev3dev.ev3 as ev3
import signal
import numpy as np


# Connect two motors and color and light sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')
lightSensorRight = ev3.ColorSensor('in1')
lightSensorLeft = ev3.ColorSensor('in2')
lightSensorFront = ev3.LightSensor('in3')


print(mA.connected)
print(mB.connected)
print(lightSensorLeft.connected)
print(lightSensorRight.connected)
print(lightSensorFront.connected)

BASE_SPEED = 60
TURN_SPEED = 80
BASE_TURN_SPEED = 30
CalI_TURN_SPEED = 50
CALI_SPEED = 15

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
        sensorFront = lightSensorFront.reflected_light_intensity
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color
        print("sensorFront")
        print(sensorFront)
        print("sensorRight")
        print(sensorRight)



def forwardSF():
    while True:
        sensorFront = lightSensorFront.value()
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color


        white = sensorFront

        if sensorLeft == 6 and sensorRight == 6:
            mA.duty_cycle_sp = BASE_SPEED
            mB.duty_cycle_sp = BASE_SPEED
            black = sensorFront / 2
        elif black < sensorFront:
            mA.duty_cycle_sp = 0
            mB.duty_cycle_sp = 0
            break


def forward_Calibration():
    while True:
        sensorFront = lightSensorFront.reflected_light_intensity
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color

        if sensorLeft == 6 and sensorRight == 6:
            mB.duty_cycle_sp = BASE_SPEED
            mA.duty_cycle_sp = BASE_SPEED

        if sensorLeft == 1 and sensorRight == 6:
            mA.duty_cycle_sp = CalI_TURN_SPEED
            mB.duty_cycle_sp = CALI_SPEED

        if sensorLeft == 6 and sensorRight == 1:
            mB.duty_cycle_sp = CalI_TURN_SPEED
            mA.duty_cycle_sp = CALI_SPEED
        if sensorFront < 50:
            mB.duty_cycle_sp = 0
            mA.duty_cycle_sp = 0
            break


def right_Turn():
    forward_Calibration()
    while True:
        sensorFront = lightSensorFront.reflected_light_intensity
        sensorLeft = lightSensorLeft.color
        sensorRight = lightSensorRight.color

        if sensorFront < 50:
            mB.duty_cycle_sp = TURN_SPEED
            mB.duty_cycle_sp = BASE_TURN_SPEED

        if sensorLeft ==

        if sensorLeft == sensorRight == 1:
            mB.duty_cycle_sp = BASE_SPEED
            mA.duty_cycle_sp = BASE_SPEED
        if sensorLeft == 6 and sensorRight == 6:
            forward_Calibration()

