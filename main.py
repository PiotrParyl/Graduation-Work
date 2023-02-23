import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#siema siema


while True:

    time.sleep(2)

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(f"Temperaturka{temperature:.2f} Wilgotność{humidity:.2f}")
    else:
        print("Failed to retrieve data from humidity sensor")