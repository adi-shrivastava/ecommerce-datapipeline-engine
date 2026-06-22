import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="enginedb",
    user="postgres",
    password="adi"
)
cursor=conn.cursor()
print("postgres connected!")
