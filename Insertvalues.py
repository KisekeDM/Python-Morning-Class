import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")

conn.execute("INSERT INTO STAFF(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)" \
             "VALUES(1, 'DANIEL', 'MUTUNGA', 21, 45000.00, 'Employer')")
conn.execute("INSERT INTO STAFF(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)" \
             "VALUES(2, 'AMOS', 'KLEIN', 30, 15000.00, 'Manager')")
conn.execute("INSERT INTO STAFF(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)" \
             "VALUES(3, 'SIMEON', 'MUTUA', 24, 35000.00, 'Chef')")
conn.execute("INSERT INTO STAFF(ID, FIRSTNAME, LASTNAME, AGE, SALARY, TASK)" \
             "VALUES(4, 'KEVIN', 'KEVIN', 28, 20000.00, 'HR')")

conn.commit()
print("Inserted Values Successfully")

conn.close()
