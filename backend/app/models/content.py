from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey, Enum
from sqlalchemy.sql import func
from datetime import datetime
from app.database import Base
import enum

class ContentType(str, enum.Enum):
    BLOG_POST = "blog_post"
    SOCIAL_MEDIA = "social_media"
    EMAIL = "email"
    NEWSLETTER = "newsletter"
    AD_COPY = "ad_copy"
    PRODUCT_DESCRIPTION = "product_description"

class ContentTone(str, enum.Enum):
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    FUNNY = "funny"
    FORMAL = "formal"
    FRIENDLY = "friendly"

class Content(Base):
    __tablename__ = "contents"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    content_type = Column(Enum(ContentType), default=ContentType.BLOG_POST)
    tone = Column(Enum(ContentTone), default=ContentTone.PROFESSIONAL)
    language = Column(String, default="en")
    
    # SEO
    keywords = Column(String, nullable=True)
    meta_description = Column(String, nullable=True)
    slug = Column(String, nullable=True, index=True)
    seo_score = Column(Float, default=0.0)
    
    # AI
    model_used = Column(String, default="gpt-4")
    tokens_used = Column(Integer, default=0)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Content {self.id}>"

class ContentTemplate(Base):
    __tablename__ = "content_templates"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    content_type = Column(Enum(ContentType), nullable=False)
    template = Column(Text, nullable=False)
    variables = Column(String, nullable=True)  # JSON string
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<ContentTemplate {self.name}>"
