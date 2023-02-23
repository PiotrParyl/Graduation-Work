import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import mysql.connector
from datetime import datetime


# Konfiguracja
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)


def regulacja_wilgotnosci():

    mydb = mysql.connector.connect(
    host="localhost",
    user="maczo1928",
    password="Pomidor13",
    database="test123"
)
    # utworzenie kursora
    mycursor = mydb.cursor()



    while True:
        
        max = input("Podaj maksymalną wilgotność ")

        max = int(max)

        while True:

            time.sleep(5)

            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

            temp = round(temperature,2)
            wilg = round(humidity,2)
            data = datetime.now()

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

          
            # Wykonanie polecenia INSERT, aby dodać dane do tabeli
            sql = "INSERT INTO czujniki (temp, wilg, data) VALUES (%s, %s, %s)"
            val = (temp, wilg, data)
            mycursor.execute(sql, val)

            # Zatwierdzenie zmian i zamknięcie połączenia z bazą danych
            mydb.commit()


regulacja_wilgotnosci()