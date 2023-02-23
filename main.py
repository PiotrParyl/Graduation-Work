import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#siema siema


while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(f"Temperaturka{temperature} Wilgotność{humidity}")
    else:
        print("Failed to retrieve data from humidity sensor")