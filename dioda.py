import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.0.11",
    user="maczo1928",
    password="Pomidor13",
    database="test123"
)
    # utworzenie kursora


mycursor = mydb.cursor()

# wykonujemy zapytanie SQL do pobrania danych z tabeli
mycursor.execute("SELECT * FROM czujnik")

# pobieramy wyniki zapytania
myresult = mycursor.fetchall()

# wyświetlamy wyniki
for row in myresult:
  print(row)