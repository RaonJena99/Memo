from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

class Memo(BaseModel):
    id:int
    content:str
    
memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '[Add Memo]'

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{id}")
def put_memo(memo:Memo):
    for i in memos:
        if i.id==memo.id:
            i.content=memo.content
            return '[Edit Memo]'
    return '[No Memo]'
        
@app.delete("/memos/{id}")
def del_memo(id):
    for i,j in enumerate(memos):
        if j.id==int(id):
            memos.pop(i)  
            return '[Delete Memo]'
    return '[No Memo]'

app.mount("/", StaticFiles(directory="static",html=True), name="static") 