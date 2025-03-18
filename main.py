from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv
import uvicorn
from pymongo import MongoClient
import random
from fastapi.responses import JSONResponse
load_dotenv()

app = FastAPI()
try:
    db = MongoClient(getenv("MONGO_URI"))["gaali"]["gaali"]
    print(f"Connected to database: {db.name}")
except Exception as e:
    print(f"Error connecting to database: {e}")


def format_response(data):
    data = data.get("gaali")
    data = {"gaali": data}
    return JSONResponse(content=data)



@app.get("/")
async def read_root():
    gaali_list = db.find({}).to_list(length=None)
    gaali = random.choice(gaali_list)
    return format_response(gaali)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)