from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.models.content import ContentType, ContentTone

class ContentCreate(BaseModel):
    title: str
    content_type: ContentType
    tone: ContentTone = ContentTone.PROFESSIONAL
    language: str = "en"
    keywords: Optional[str] = None
    prompt: str

class ContentRewrite(BaseModel):
    content_id: int
    tone: Optional[ContentTone] = None
    style: Optional[str] = None

class ContentAnalyze(BaseModel):
    content: str
    language: str = "en"

class ContentResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    content_type: ContentType
    tone: ContentTone
    language: str
    keywords: Optional[str]
    meta_description: Optional[str]
    seo_score: float
    model_used: str
    tokens_used: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
