from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator API Running"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: int, b: int):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}

@app.get("/divide")
def divide(a: int, b: int):
    return {"result": a / b}

@app.get("/pecentage")
def pecentage(a: int, b: int):
    return {"result": a % b}