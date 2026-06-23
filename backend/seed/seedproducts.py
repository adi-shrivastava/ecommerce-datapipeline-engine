import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import conn,cursor
import random
from faker import Faker
categories={"Electronics":["Speakers","Laptops","AC","Washing Machines"],
            "Books":["Novel","Biography","Comics"],
            "Fashion":["Jeans","Top","Jacket","LooseFit","Sneakers","Formals"],
            "Home":["Chair","Lamp","Table"]
            }
productid=1
for category,products in categories.items():
    
    for product in products:
        price=random.randint(1000,50000)
        cursor.execute("""INSERT INTO products (productid,category,price) values(%s,%s,%s)""",(productid,category,price))
        productid+=1
conn.commit()
print("Products Seeded!")
cursor.close()
conn.close()

    