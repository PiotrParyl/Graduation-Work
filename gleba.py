import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()  # utworzenie obiektu klasy ADS1115

GAIN = 1  # wzmocnienie przetwornika
CHANNEL = 14  # numer kanału analogowego

while True:
    value = adc.read_adc(CHANNEL, gain=GAIN)  # odczyt wartości analogowej
    print('Wartość: {} V'.format(value / 32767.0 * 4.096))  # wyświetlenie wartości napięcia
    time.sleep(1)  # opóźnienie 1 sekundy