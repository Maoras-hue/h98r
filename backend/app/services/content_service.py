from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.content import Content
from app.models.user import User
from app.schemas.content import ContentCreate, ContentRewrite
from app.services.ai_service import generate_with_ai, rewrite_with_ai
from app.services.credit_service import deduct_credits
from app.config import settings
from fastapi import HTTPException, status
import re

async def generate_content(db: Session, user: User, content_data: ContentCreate):
    # Check credits
    user_credit = db.query(db.query(User).filter(User.id == user.id)).first()
    if not hasattr(user, 'credit') or user.credit.available_credits < settings.CREDIT_COST_GENERATE:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Insufficient credits"
        )
    
    # Generate content using AI
    generated_content = await generate_with_ai(
        content_data.prompt,
        content_data.content_type,
        content_data.tone,
        content_data.language
    )
    
    # Create slug
    slug = re.sub(r'[^\w\s-]', '', content_data.title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    
    # Save to database
    db_content = Content(
        user_id=user.id,
        title=content_data.title,
        content=generated_content["content"],
        content_type=content_data.content_type,
        tone=content_data.tone,
        language=content_data.language,
        keywords=content_data.keywords,
        meta_description=generated_content.get("meta_description"),
        slug=slug,
        model_used=generated_content.get("model", "gpt-4"),
        tokens_used=generated_content.get("tokens", 0)
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    
    # Deduct credits
    await deduct_credits(db, user.id, settings.CREDIT_COST_GENERATE, "Content generation")
    
    return db_content

async def rewrite_content(db: Session, user: User, rewrite_data: ContentRewrite):
    # Get original content
    db_content = db.query(Content).filter(
        (Content.id == rewrite_data.content_id) & (Content.user_id == user.id)
    ).first()
    
    if not db_content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    
    # Rewrite content
    rewritten = await rewrite_with_ai(
        db_content.content,
        rewrite_data.tone or db_content.tone,
        rewrite_data.style
    )
    
    db_content.content = rewritten["content"]
    if rewrite_data.tone:
        db_content.tone = rewrite_data.tone
    db.commit()
    db.refresh(db_content)
    
    # Deduct credits
    await deduct_credits(db, user.id, settings.CREDIT_COST_REWRITE, "Content rewrite")
    
    return db_content

async def analyze_content(content: str, language: str = "en"):
    from app.services.seo_service import analyze_seo
    return await analyze_seo(content)

async def get_user_contents(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    contents = db.query(Content).filter(
        Content.user_id == user_id
    ).order_by(desc(Content.created_at)).offset(skip).limit(limit).all()
    return contents

async def get_content(db: Session, content_id: int, user_id: int):
    content = db.query(Content).filter(
        (Content.id == content_id) & (Content.user_id == user_id)
    ).first()
    
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Content not found"
        )
    return content
