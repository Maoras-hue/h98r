from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.schemas.credit import CreditResponse
from app.services.auth_service import get_current_user
from app.services.credit_service import get_user_credits

router = APIRouter()

@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(
    current_user: User = Depends(get_current_user)
):
    """Get current user profile"""
    return current_user

@router.put("/me", response_model=UserResponse)
async def update_profile(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update user profile"""
    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)
    db.commit()
    db.refresh(current_user)
    return current_user

@router.get("/credits", response_model=CreditResponse)
async def get_credits(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get user credits"""
    credits = await get_user_credits(db, current_user.id)
    return credits
