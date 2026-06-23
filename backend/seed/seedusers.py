import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db import conn,cursor
import random
from faker import Faker
fake=Faker()
cities=["Indore","Mumbai","Delhi","Chennai"]
userid=1
for i in range(1000):
    
    name=fake.name()
    age=random.randint(18,60)
    city=random.choice(cities)
    cursor.execute("""INSERT INTO users (userid,name,age,city) values(%s,%s,%s,%s)""",(userid,name,age,city))
    userid+=1
conn.commit()
print("USERS SEEDED")
cursor.close()
conn.close()