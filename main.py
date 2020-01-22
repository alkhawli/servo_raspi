# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:11:24 2020

@author: tkw
"""
import RPi.GPIO as GPIO
import time


class ServoMotor:
    def __init__(self, pinnumber):
        self.pinnumber = pinnumber
        self.pinnumber = 22 #Pin number
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinnumber,GPIO.OUT)
        self.p=GPIO.PWM(self.pinnumber,50)# 50hz frequency
        self.p.start(1)# starting duty cycle ( it set the servo to 0 degree )

    def setangle(self, angle):
        k = (float(angle)*12/180)+1  
        self.p.ChangeDutyCycle(k)
        time.sleep(0.1)        
        
    def demofrom0to180(self):  
        i=0
        try:
            while True:
                self.setangle(i)
                if i>180:
                    i=0
                else:
                    i=i+10

        except KeyboardInterrupt:
            self.setangle(0)
            self.p.stop()
            GPIO.cleanup()

if __name__ == '__main__':
    servo=ServoMotor(22)
    servo.demofrom0to180()