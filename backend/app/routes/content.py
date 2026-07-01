from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.user import User
from app.schemas.content import ContentCreate, ContentResponse, ContentAnalyze, ContentRewrite
from app.services.content_service import (
    generate_content,
    rewrite_content,
    analyze_content,
    get_user_contents,
    get_content
)
from app.services.auth_service import get_current_user

router = APIRouter()

@router.post("/generate", response_model=ContentResponse)
async def generate(
    content_data: ContentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Generate new content"""
    content = await generate_content(db, current_user, content_data)
    return content

@router.post("/rewrite", response_model=ContentResponse)
async def rewrite(
    rewrite_data: ContentRewrite,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Rewrite existing content"""
    content = await rewrite_content(db, current_user, rewrite_data)
    return content

@router.post("/analyze")
async def analyze(
    analyze_data: ContentAnalyze,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Analyze content"""
    analysis = await analyze_content(analyze_data.content, analyze_data.language)
    return analysis

@router.get("/", response_model=List[ContentResponse])
async def list_contents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 10
):
    """Get user's contents"""
    contents = await get_user_contents(db, current_user.id, skip, limit)
    return contents

@router.get("/{content_id}", response_model=ContentResponse)
async def get_content_detail(
    content_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get content by ID"""
    content = await get_content(db, content_id, current_user.id)
    return content
