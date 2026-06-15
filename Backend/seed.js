events=[]
for(let i=0; i<=100000; i++){
    events.push({
        userId:randomUser(),
        productId:randomproduct(),
        eventtype:randomevent(),
        timestamp:randomtime()
    });
}