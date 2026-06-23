import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import random
from db import conn,cursor
cursor.execute("Select productid from products")
productids=[row[0] for row in cursor.fetchall()]
productid=random.choice(productids)

cursor.execute("Select userid from users")
userids=[row[0] for row in cursor.fetchall()]
for _ in range(10000):
    userid=random.choice(userids)
    quantity=random.randint(1,5)
    cursor.execute("select price from products where productid=%s",(productid,))
    price=cursor.fetchone()[0]
    total=quantity*price
    cursor.execute("""insert into purchases (userid,productid,quantity,unitprice,totalamount) values(%s,%s,%s,%s,%s)""",(userid,productid,quantity,price,total))
conn.commit()
print("purchases seeded!")
cursor.close()
conn.close()
