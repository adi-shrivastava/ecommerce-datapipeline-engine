from recommend import recommend
from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message": "Hello World"}
@app.get("/recommend/{id}")
def get_recommendations(id:int):
    recc=recommend(id)
    return{"message": "This is the recommendation endpoint","recommendations ":recc}