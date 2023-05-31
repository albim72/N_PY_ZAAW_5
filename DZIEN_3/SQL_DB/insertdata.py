import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1', port=3306, database="dbtestowa")
cursorObject = db.cursor()

idata = """
INSERT INTO student(firstname,lastname,kierunek) VALUES(%s,%s,%s);
"""
val = ("Jan","Nowak","Budowlany")
cursorObject.execute(idata,val)
db.commit()
db.close()
