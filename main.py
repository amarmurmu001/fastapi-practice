from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import random

# ---------------------- Database Setup ----------------------
DATABASE_URL = "sqlite:///./quotes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# ---------------------- Models ----------------------
class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    author = Column(String)

Base.metadata.create_all(bind=engine)

# ---------------------- Schemas ----------------------
class QuoteCreate(BaseModel):
    text: str
    author: str

class QuoteOut(BaseModel):
    id: int
    text: str
    author: str

    class Config:
        from_attributes = True  # For Pydantic v2

# ---------------------- FastAPI App ----------------------
app = FastAPI(title="Quotes API (Single File)")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------- Routes ----------------------
@app.post("/quotes", response_model=QuoteOut)
def create_quote(quote: QuoteCreate, db: Session = Depends(get_db)):
    db_quote = Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

@app.get("/quotes", response_model=List[QuoteOut])
def get_all_quotes(db: Session = Depends(get_db)):
    return db.query(Quote).all()

@app.get("/quotes/{quote_id}", response_model=QuoteOut)
def get_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@app.get("/quotes/search", response_model=List[QuoteOut])
def search_quotes(author: str = Query(...), db: Session = Depends(get_db)):
    return db.query(Quote).filter(Quote.author.ilike(f"%{author}%")).all()

@app.get("/quotes/random", response_model=QuoteOut)
def get_random_quote(db: Session = Depends(get_db)):
    quotes = db.query(Quote).all()
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes available")
    return random.choice(quotes)
