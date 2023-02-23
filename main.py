import Adafruit_DHT
import time
import RPi.GPIO as GPIO


#Konfiguracja

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4



while True:

    time.sleep(2)

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    temp = round(temperature,2)
    wilg = round(humidity,2)

    if humidity is not None and temperature is not None:
        print(f"Temperaturka{temp} Wilgotność{wilg}")
    else:
        print("Failed to retrieve data from humidity sensor")

    if wilg > 60:
        print("ZA WILGOTNO")
        GPIO.output(23,GPIO.HIGH)

    else:
        print("OK")
        GPIO.output(23,GPIO.LOW)