import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306, database="dbtestowa")
cursorObject = db.cursor()

idata = """
INSERT INTO student(firstname,lastname,kierunek) VALUES(%s,%s,%s);
"""
val = ("Jan","Nowak","Budowlany")
morestud = [
    ("Anna","Kos","Informatyka"),
    ("Olga","Nowik","Informatyka"),
    ("Mariusz","Rync","Fizyka"),
    ("Nadia","Kłos","Pedagogika"),
    ("Bartek","Kowal","Ekomomia"),
    ("Olaf","Nowik","Prawo"),
    ("Gienek","Owczar","Prawo"),
]
cursorObject.execute(idata,val)
cursorObject.executemany(idata,morestud)
db.commit()
db.close()
