const {Pool}=require("./db");

users=[]
async function seedusers(){
    for(let i=1; i<=1000; i++){
        const user='User${i}';
        const age=(Math.floor(Math.random*40)+18);
        const cities=['Indore','Agra','Bangalore','Pune','Mumbai','Chennai','Delhi'];
        const city=randomitem(cities);
        await pool.query('INSERT INTO USERS (name,age,city)')
    }
}

