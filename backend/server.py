from recommend import recommend
from db import conn,cursor
import pandas as pd
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message": "Hello World"}
@app.get("/recommend/{id}")
def get_recommendations(id:int):
    recc=recommend(id)
    prodid=tuple(recc.keys())
    cursor.execute("""select productid,category,price from products where productid in %s""",(prodid,))
    rows=cursor.fetchall()
    result=[]
    for productid,category,price in rows:
        result.append({"Product ID : ":productid,
        "Category : ":category,
        "Price : ":price,
        "Recommendation Score : ":recc[productid]})
    return {"message":"That's recommendation endpoint", "recommendations": result}
    # result=[]
    # for product,score in recc.items():
    #     query=("""select productid,category,price from products where productid=%s""")
    #     result.append((product,score,pd.read_sql(query,conn,params=(product,))))
    # return{"message": "This is the recommendation endpoint","recommendations ":result}
