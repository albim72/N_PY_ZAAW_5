import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306, database="dbtestowa")
cursorObject = db.cursor()

dane = "SELECT * FROM student"
cursorObject.execute(dane)

wynik = cursorObject.fetchall()
print(type(wynik))
for x in wynik:
    print(x)

print("___________________________________________")
dane = "SELECT * FROM student WHERE lastname = 'Kos'"
cursorObject.execute(dane)

wynik = cursorObject.fetchall()

for x in wynik:
    print(x)
db.close()

