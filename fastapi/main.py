from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
async def add_numbers(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}