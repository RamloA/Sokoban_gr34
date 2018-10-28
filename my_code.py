#!/usr/bin/python3
#!/usr/bin/env python

import ev3dev.ev3 as ev3
import signal


# Connect two motors and two (different) light sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in2')

BASE_SPEED = 30
TURN_SPEED = 80


mA.run_direct()
mB.run_direct()

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
            elif sensorLeft==6 and sensorRight ==6:\
                mA.duty_cycle_sp = BASE_SPEED
            mB.duty_cycle_sp = BASE_SPEED
            if sensorLeft == 1 and sensorRight == 1:
                mA.duty_cycle_sp = 0
                mB.duty_cycle_sp = 0


def sensor


while True:
    sensorLeft = lightSensorLeft.color
    sensorRight = lightSensorRight.color
    print("sensorLeft: ", sensorLeft, " sensorRight: ", sensorRight)
    if sensorLeft == 6 and sensorRight == 6:
        mA.polarity = "normal"
        mB.polarity = "normal"
        mA.duty_cycle_sp = BASE_SPEED
        mB.duty_cycle_sp = BASE_SPEED
    # elif sensorLeft == 1 and sensorRight == 1:
    # mA.duty_cycle_sp = 0
    # mB.duty_cycle_sp = 0
    # mA.polarity = "inversed"
    # mB.polarity = "inversed"
    # mA.duty_cycle_sp = BASE_SPEED
    # mB.duty_cycle_sp = BASE_SPEED
    # if sensorLeft == 1 and sensorRight == 1:
        #mA.duty_cycle_sp = 0
        #mB.duty_cycle_sp = 0





