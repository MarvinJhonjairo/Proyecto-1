#!/usr/bin/env python
import tweepy
import RPi.GPIO as GPIO
import time

#Puertos de entrada y salida
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(10, GPIO.IN)

#Coloca dentro de las comillas tus claves...
CONSUMER_KEY = 'S9Tw7CnZCRWtjzPC0ZLzmKwwq'
CONSUMER_SECRET = '135h3fOF662hGneAMTSBVvOh4Bq9RIbF7i0hqpXPYJlGugHZg0'
ACCESS_KEY = '2815404050-huITDbiIcS6oaVJ6DyfFnlbVJEOIHnGHukseoUw'
ACCESS_SECRET = 'yp5GgjLAnaaD3srr7w8Nd0nvnt2wxCAYtUzFsHhfVOn20'

#En esta parte nos identifica para poder realizar operaciones
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#update_status('mensaje' o variable) es para actualizar nuestro estado
x = tweepy.API(auth)
x.update_status('Publique mi primer tweet ')

#Turn LEDs on
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
#Turn LEDs on
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
GPIO.cleanup

print("------------------")
print(" Button + GPIO ")
print("------------------")
print GPIO.input(10)

while True:
    if ( GPIO.input(10) == False ):
        print("Button Pressed")
        os.system('date')
        print GPIO.input(10)
        time.sleep(1)
    else:
        os.system('clear')
        print ("Waiting for you to press a button")
        time.sleep(0.5) 
# conectar push, a negativo
# conectar el otro lado al pin y a resistencia a positivo
