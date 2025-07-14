
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, State

app = FastAPI()

class LoginRequest(BaseModel):
    phone: str
    password: str

@app.post("/login")
async def login(request: LoginRequest):
    if request.phone == "7760873976" and request.password == "to_share@123":
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid phone number or password")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/states")
async def get_states(db: Session = Depends(get_db)):
    states = db.query(State).all()
    return {
        "status": True,
        "message": "States fetched successfully",
        "data": [{"id": s.id, "name": s.name} for s in states]
    }