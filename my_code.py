#!/usr/bin/python3
#!/usr/bin/env python

import ev3dev.ev3 as ev3
import signal


# Connect two motors and two (different) light sensors
mA = ev3.LargeMotor('outA')
mB = ev3.LargeMotor('outB')

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.colorSensor('in2')

while True:
    