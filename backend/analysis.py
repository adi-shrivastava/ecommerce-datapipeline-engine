import pandas as pd
from db import conn,cursor
query="""select userid,productid,
sum(case
 when eventtype='view' then 1 
 when eventtype ='addtocart' then 3 
 when eventtype='purchased' then 5 
 else 0
 end) 
 as score 
 from events 
 group by userid,productid;"""

df=pd.read_sql(query,conn)
print(df.head())