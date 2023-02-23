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
        
        max = input("Podaj maksymalną wilgotność ")

        max = int(max)

        time.sleep(5)

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        temp = round(temperature,2)
        wilg = round(humidity,2)

        if humidity is not None and temperature is not None:
            print(f"Temperaturka {temp}   Wilgotność {wilg}")
        else:
            print("Failed to retrieve data from humidity sensor")

        if wilg >= max:
            print("ZA WILGOTNO")
            GPIO.output(23,GPIO.HIGH)

        if wilg < max:
            print("OK")
            GPIO.output(23,GPIO.LOW)

        

regulacja_wilgotnosci()