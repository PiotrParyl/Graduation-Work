import Adafruit_DHT
import time
import RPi.GPIO as GPIO

# Konfiguracja
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def regulacja_wilgotnosci():

    while True:
        min = input("Podaj minimalną wilgotność: ")
        max = input("Podaj maksymalną wilgotność ")

        min = int(min)
        max = int(max)

        seterowanie_wiatrakiem(max,min)



def seterowanie_wiatrakiem (max,min):
    while True:
        time.sleep(2)

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        temp = round(temperature,2)
        wilg = round(humidity,2)

        if humidity is not None and temperature is not None:
            print(f"Temperaturka{temp} Wilgotność{wilg}")
        else:
            print("Failed to retrieve data from humidity sensor")

        if wilg > max:
            print("ZA WILGOTNO")
            GPIO.output(23,GPIO.HIGH)

        if wilg <= min:
            print("OK")
            GPIO.output(23,GPIO.LOW)

        

regulacja_wilgotnosci()