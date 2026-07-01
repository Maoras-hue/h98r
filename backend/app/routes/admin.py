from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.auth_service import get_current_user

router = APIRouter()

async def verify_admin(current_user: User = Depends(get_current_user)):
    """Verify admin user"""
    # Add admin check logic here
    return current_user

@router.get("/stats", dependencies=[Depends(verify_admin)])
async def get_stats(db: Session = Depends(get_db)):
    """Get platform statistics"""
    from sqlalchemy import func
    from app.models.user import User
    from app.models.content import Content
    
    total_users = db.query(func.count(User.id)).scalar()
    total_content = db.query(func.count(Content.id)).scalar()
    
    return {
        "total_users": total_users,
        "total_content": total_content,
    }

@router.get("/users", dependencies=[Depends(verify_admin)])
async def list_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    """List all users"""
    from app.models.user import User
    users = db.query(User).offset(skip).limit(limit).all()
    return users
