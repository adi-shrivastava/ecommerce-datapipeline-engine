import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from db import conn,cursor
query="""Select userid,productid,sum(
case
when eventtype='view' then 1
when eventtype='addtocart' then 3
when eventtype='purchased' then 5
ELSE 0
end) as score from events group by userid,productid"""

df=pd.read_sql(query,conn)
matrix=df.pivot_table(
    index="userid",
    columns="productid",
    values="score",
    fill_value=0
)
similiarity=cosine_similarity(matrix)
df1=pd.DataFrame(similiarity,index=matrix.index,columns=matrix.index) ## User-user similarity matrix 
def recommend(userid):
    similiarusers=(df1.loc[userid].sort_values(ascending=False).index[1:6])
    prodscores={}
    for user in similiarusers:
        products=(matrix.loc[user].sort_values(ascending=False).head(5))
        for product,scores in products.items():
            if(matrix.loc[userid,product] !=0):
                continue
            if(product not in prodscores):
                prodscores[product]=scores
            else:
                prodscores[product]+=scores
    return prodscores
value=recommend(68)
for product,score in value.items():
    query=("""select productid,category,price from products where productid=%s""")
    print("Recommendation Score : ",score)
    
    print(pd.read_sql(query,conn,params=(product,)))

