import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import mysql.connector
from datetime import datetime
import smtplib
from email.message import EmailMessage
import ssl
import smtplib
import math


# Konfiguracja
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
email_sendet = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)




def send_email():

    email_sender = 'dr.grubylolek@gmail.com'
    email_password = 'zcxsprlzqtbkljkk'
    email_receiver = 'piotrekzrydek@gmail.com'


    subject = 'AWARJA CZUJNIKA'
    body = 'AWARJA CZUJNIKA'


    # Set up your email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,msg.as_string())


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

            

            try:
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
                sql = "INSERT INTO czujnik (temp, wilg, data) VALUES (%s, %s, %s)"
                val = (temp, wilg, data)
                mycursor.execute(sql, val)
                
                email_sendet == False
                # Zatwierdzenie zmian i zamknięcie połączenia z bazą danych
                mydb.commit()

            except:
                
                data = datetime.now()
                sql = "INSERT INTO czujnik (temp, wilg, data) VALUES (%s, %s, %s)"            
                val = (None, None, data)
                
                mycursor.execute(sql, val)
                mydb.commit()
                print("Error")

                global email_sendet
                if email_sendet == False:
                    send_email()
                    email_sendet = True


regulacja_wilgotnosci()



