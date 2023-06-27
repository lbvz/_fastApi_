from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello lbvz"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#query parameter
@app.get("/raspberry")
async def read_item(time:datetime = datetime.now(),light: float = 0.0, temperature: float = 0.0):
    return {
        "時間":time.strftime("%Y%m%d %H:%M:%S"),
        "光線":light,
        "溫度":temperature
    }
