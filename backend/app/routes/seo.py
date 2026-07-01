from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.auth_service import get_current_user
from app.services.seo_service import (
    analyze_seo,
    extract_keywords,
    generate_meta_tags,
    check_readability
)

router = APIRouter()

@router.post("/analyze")
async def analyze_seo_endpoint(
    content: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Analyze SEO of content"""
    seo_analysis = await analyze_seo(content)
    return seo_analysis

@router.post("/keywords")
async def extract_keywords_endpoint(
    content: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Extract keywords from content"""
    keywords = await extract_keywords(content)
    return {"keywords": keywords}

@router.post("/meta")
async def generate_meta_endpoint(
    title: str,
    content: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Generate meta tags"""
    meta = await generate_meta_tags(title, content)
    return meta

@router.post("/readability")
async def readability_endpoint(
    content: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Check content readability"""
    readability = await check_readability(content)
    return readability
