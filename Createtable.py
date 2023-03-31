import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected Successfully")

conn.execute("""CREATE TABLE Staff(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL NOT NULL,
TASK TEXT CHAR(50))""")

print("Successfully created Staff Table")
conn.close()
