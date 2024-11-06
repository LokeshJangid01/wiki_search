from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import wikipediaapi
from auto_tag import get_tags_from_textrazor
from database import SessionLocal, engine
from models import FavoriteArticle, Base
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app and Wikipedia API with a user agent
app = FastAPI()
wiki = wikipediaapi.Wikipedia(language='en', user_agent="LokiTheGod")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class Article(BaseModel):
    title: str
    summary: str
    

class SearchKeyword(BaseModel):
    keyword: str

# Root endpoint
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Search for Wikipedia articles
@app.post("/search/")
async def search_articles(search: SearchKeyword):
    keyword = search.keyword
    page = wiki.page(keyword)

    if not page.exists():
        raise HTTPException(status_code=404, detail="Article not found")
    
    return {
        "title": page.title,
        "summary": page.summary[0:1000]  # Return only the first 500 characters of the summary
        
    }

# Save favorite article
@app.post("/favorites/")
async def save_favorite(article: Article, db: Session = Depends(get_db)):
    # Check if the article already exists in favorites
    db_article = db.query(FavoriteArticle).filter(FavoriteArticle.title == article.title).first()
    if db_article:
        raise HTTPException(status_code=400, detail="Article already in favorites")
    
    # Auto-tagging the article's summary
    tags = get_tags_from_textrazor(article.summary)
    
    # Create a new favorite article entry
    favorite_article = FavoriteArticle(
        title=article.title,
        summary=article.summary,
        tags=tags
        
    )
    db.add(favorite_article)
    db.commit()
    db.refresh(favorite_article)
    print(favorite_article)
    
    return {"message": f"Article '{article.title}' added to favorites", "article": favorite_article}

# Retrieve all favorite articles
@app.get("/favorites/")
async def get_favorites(db: Session = Depends(get_db)):
    favorites = db.query(FavoriteArticle).all()
    return {"favorites": favorites}
