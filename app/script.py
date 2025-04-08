import psycopg2
import time

time.sleep(5)  # Ждем инициализацию БД

conn = psycopg2.connect(
    dbname="testdb",
    user="user",
    password="password",
    host="database"
)

cur = conn.cursor()
cur.execute("SELECT * FROM messages;")
print("Data from database:")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
