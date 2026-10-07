import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="harsh_pds"
)

cursor = con.cursor()

cursor.execute("INSERT INTO students VALUES (17, 'Harsh', 20, 'SSASIT', 'Computer Engineering', 85)")
con.commit()
print("Record inserted")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE students SET marks = 90 WHERE enrollment_no = 17")
con.commit()
print("Record updated")

cursor.execute("DELETE FROM students WHERE enrollment_no = 17")
con.commit()
print("Record deleted")

cursor.close()
con.close()

