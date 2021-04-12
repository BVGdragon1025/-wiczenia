import sqlite3

conn = sqlite3.connect('test.db')

"""conn.execute('''CREATE TABLE company(
            ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL);''')
print("Tabela utworzona")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES (1, 'Adam', 32, 'Wroclaw', 2000.00 );")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES (2, 'Marcin', 50, 'Wroclaw', 2000.00 );")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES (3, 'Jan', 19, 'Berlin', 6000.00 );")
conn.commit()
print("Rekordy zostały dodane")
"""

cursor = conn.execute("Select id, name, address, salary FROM company;")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
