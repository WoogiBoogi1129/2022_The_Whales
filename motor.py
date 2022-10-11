#! /usr/bin/python3
import serial
import RPi.GPIO as GPIO
import time
import warnings
warnings.filterwarnings('ignore')

#Default PWM Speed
undoSpeed = 40

def stMtrCntrlFrwrd(speed):
    pi_pwm1.ChangeDutyCycle(speed)
    pi_pwm2.ChangeDutyCycle(speed)

def stMtrCntrlRight(speed):
    pi_pwm1.ChangeDutyCycle(speed)
    pi_pwm2.ChangeDutyCycle(40)

def stMtrCntrlLeft(speed):
    pi_pwm1.ChangeDutyCycle(40)
    pi_pwm2.ChangeDutyCycle(speed)

def waterCraftSpeed(inputData):
    global undoSpeed
    
    if inputData == 'p\n':
        stMtrCntrlFrwrd(70)
        undoSpeed = 70
                    
    elif inputData == 'q\n':
        stMtrCntrlFrwrd(65)
        undoSpeed = 65
                    
    elif inputData == 'r\n':
        stMtrCntrlFrwrd(60)
        undoSpeed = 60
                    
    elif inputData == 's\n':
        stMtrCntrlFrwrd(40)
        undoSpeed = 40
            
    elif inputData =='t\n':
        stMtrCntrlFrwrd(undoSpeed)

    else:
        return

def waterCraftAngle(inputData):
    global undoSpeed
    
    if(undoSpeed != 40):
        if inputData == 'n\n':
            stMtrCntrlRight(70)
                    
        elif inputData == 'm\n':
            stMtrCntrlRight(68)
                    
        elif inputData == 'l\n':
            stMtrCntrlRight(66)
                    
        elif inputData == 'k\n':
            stMtrCntrlRight(64)
                    
        elif inputData == 'j\n':
            stMtrCntrlRight(62)
                    
        elif inputData == 'i\n':
            stMtrCntrlRight(60)
                    
        elif inputData == 'h\n':
            stMtrCntrlRight(58)
                    
        elif inputData == 'g\n':
            stMtrCntrlLeft(70)
                    
        elif inputData == 'f\n':
            stMtrCntrlLeft(68)
                    
        elif inputData == 'e\n':
            stMtrCntrlLeft(66)
                    
        elif inputData == 'd\n':
            stMtrCntrlLeft(64)
                    
        elif inputData == 'c\n':
            stMtrCntrlLeft(62)
                    
        elif inputData == 'b\n':
            stMtrCntrlLeft(60)
                    
        elif inputData == 'a\n':
            stMtrCntrlLeft(58)
        
        elif inputData == 'HOME\n':
            stMtrCntrlFrwrd(undoSpeed)        
    else:
         return           

# BLDC motor pin set
pin1 = 32
pin2 = 33

#GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)

#BLDC motor PWM set
pi_pwm1 = GPIO.PWM(pin1,500)
pi_pwm2 = GPIO.PWM(pin2,500)   
pi_pwm1.start(40)
pi_pwm2.start(40)

#Serial monitor display
raspiSerial = serial.Serial(timeout=3)
raspiSerial.port ='/dev/ttyAMA0'
raspiSerial.baudrate = 115200

if __name__ == "__main__":
    while True:

        try:
            raspiSerial.open()
            raspiSerial.flushInput()
            time.sleep(0.01)

            inputData = raspiSerial.readline().decode()
            print(inputData)

            if(inputData == 'v\n'):
                raspiSerial.close()
                break

            elif(inputData =='u\n'):
                continue

            elif(inputData =='p\n' or inputData =='q\n' or inputData =='r\n' or inputData =='s\n'or inputData =='t\n' ):
                waterCraftSpeed(inputData)
                
            else:
                waterCraftAngle(inputData)
    
                               
        except Exception as e:
            print('Error:'+str(e))

        finally:
            raspiSerial.close()


    GPIO.cleanup()            
    pi_pwm1.stop()
    pi_pwm2.stop()
    exit(0)