#!/usr/bin/python3
#!/usr/bin/env python

import ev3dev.ev3 as ev3

#from implementation import *


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

BASE_SPEED = 80
TURN_SPEED = 300
BASE_TURN_SPEED = 30
CalI_TURN_SPEED = 50
CALI_SPEED = 15

mA.run_direct()
mB.run_direct()

lightSensorRight.mode = 'COL-COLOR'
lightSensorLeft.mode = 'COL-COLOR'
lightSensorFront.mode = 'REFLECT'


White_front = lightSensorFront.reflected_light_intensity
white_right = lightSensorRight.reflected_light_intensity

white_left = lightSensorLeft.reflected_light_intensity


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



def callibrate(Wf, Wr, Wl):
    Wf = lightSensorFront.reflected_light_intensity
    Wr = lightSensorRight.reflected_light_intensity
    Wl = lightSensorLeft.reflected_light_intensity

def forward_Calibration_RLI(Wf, Wr, Wl):
    is_black = 1
    mA.run_direct()
    mB.run_direct()
    while True:
        sensorFront = lightSensorFront.reflected_light_intensity
        sensorLeft = lightSensorLeft.reflected_light_intensity
        sensorRight = lightSensorRight.reflected_light_intensity

        #taking the difference between white and black

        diff_W_B_f = Wf - sensorFront
        diff_W_B_r = Wr - sensorRight
        diff_W_B_l = Wl - sensorLeft
        threshold_v = 10

        if diff_W_B_r < threshold_v and diff_W_B_l < threshold_v:
            mB.duty_cycle_sp = BASE_SPEED
            mA.duty_cycle_sp = BASE_SPEED

        # One sensor_L sees black and Right sees white
        if diff_W_B_l > threshold_v and diff_W_B_r  < threshold_v:
            mA.duty_cycle_sp = CalI_TURN_SPEED
            mB.duty_cycle_sp = CALI_SPEED

         #Vice vers
        if diff_W_B_l < threshold_v and diff_W_B_r > threshold_v:
            mB.duty_cycle_sp = CalI_TURN_SPEED
            mA.duty_cycle_sp = CALI_SPEED
        # Stop when black
        if diff_W_B_f > threshold_v:
            mB.duty_cycle_sp = 0
            mA.duty_cycle_sp = 0
            #is_black = 0
            break
"""
        if is_black == 0:
            if diff_W_B_f < threshold_v:
                print("WHITE")
                # mB.run_times(time_sp=10, speed_sp=1)
                # mA.run_times(time_sp=10, speed_sp=1)
                #mB.stop(stop_action='brake')
                #mA.stop(stop_action='brake')
                mA.duty_cycle_sp = 0
                mB.duty_cycle_sp = 0
            #print("IS black true ")
            #mA.duty_cycle_sp = 0
            #mB.duty_cycle_sp = 0
            is_black=1
            break
"""

def right_Turn_RLI(Wf, Wr, Wl):
    mA.run_direct()
    mB.run_direct()
    while True:
        sensorFront = lightSensorFront.reflected_light_intensity
        sensorLeft = lightSensorLeft.reflected_light_intensity
        sensorRight = lightSensorRight.reflected_light_intensity

        diff_W_B_f = Wf - sensorFront
        diff_W_B_r = Wr - sensorRight
        diff_W_B_l = Wl - sensorLeft

        #diff_W_B = White - sensorFront
        #threshold_R = white_color1 - sensorRight
        #threshold_L = white_color2 - sensorLeft
        threshold_v = 10
        if diff_W_B_f > threshold_v:
            mB.run_to_rel_pos(position_sp=125, speed_sp= TURN_SPEED)
            mA.run_to_rel_pos(position_sp=-125, speed_sp=TURN_SPEED)
            mB.wait_while("running")  # Wait for the turn to finish
            mA.wait_while("running")  # Wait for the turn to finish
            """
        if sensorRight >= 60 and sensorLeft >= 13 and sensorFront > 56:
            mB.run_to_rel_pos(position_sp=98, speed_sp=350)
            mA.run_to_rel_pos(position_sp=98, speed_sp=350)

        if sensorRight >= 60 and sensorLeft >= 60 and sensorFront > 56:
            mB.run_to_rel_pos(position_sp=98, speed_sp=350)
            mA.run_to_rel_pos(position_sp=98, speed_sp=350)
            """

        if diff_W_B_l < threshold_v and diff_W_B_r < threshold_v:
            mA.run_direct()
            mB.run_direct()
            mB.duty_cycle_sp = 0
            mA.duty_cycle_sp = 0

            break

def right_Turn_Con():

    while True:
        sensorFront = lightSensorFront.reflected_light_intensity
        sensorLeft = lightSensorLeft.reflected_light_intensity
        sensorRight = lightSensorRight.reflected_light_intensity
        diff_W_B = White - sensorFront
        threshold_R = white_color1 - sensorRight
        threshold_L = white_color2 - sensorLeft
        threshold_v = 10

        if sensorLeft < sensorRight or sensorLeft == sensorRight < threshold_v:
            mB.duty_cycle_sp = BASE_SPEED
            mA.duty_cycle_sp = BASE_SPEED

        # One sensor_L sees black and Right sees white
        if threshold_L > threshold_v and threshold_R < threshold_v:
            mA.duty_cycle_sp = CalI_TURN_SPEED
            mB.duty_cycle_sp = CALI_SPEED

         #Vice vers
        if threshold_L < threshold_v and sensorRight > threshold_v:
            mB.duty_cycle_sp = CalI_TURN_SPEED
            mA.duty_cycle_sp = CALI_SPEED
        # Stop when black
        if diff_W_B > threshold_v:
            mB.duty_cycle_sp = 0
            mA.duty_cycle_sp = 0

            break


callibrate(White_front, white_right, white_left)

forward_Calibration_RLI(White_front, white_right, white_left)
#print("HI")
#forward_Calibration_RLI(White_front, white_right, white_left)
right_Turn_RLI(White_front, white_right, white_left)



