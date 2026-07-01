from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from datetime import datetime, timedelta
from app.models.credit import UserCredit, CreditTransaction, TransactionType
from app.models.user import User
from fastapi import HTTPException, status

async def get_or_create_user_credits(db: Session, user_id: int) -> UserCredit:
    """Get or create user credits"""
    credits = db.query(UserCredit).filter(UserCredit.user_id == user_id).first()
    
    if not credits:
        next_reset = datetime.utcnow() + timedelta(days=30)
        credits = UserCredit(
            user_id=user_id,
            total_credits=10.0,
            available_credits=10.0,
            next_reset=next_reset
        )
        db.add(credits)
        db.commit()
        db.refresh(credits)
    
    return credits

async def get_user_credits(db: Session, user_id: int) -> UserCredit:
    """Get user credits"""
    credits = await get_or_create_user_credits(db, user_id)
    return credits

async def deduct_credits(db: Session, user_id: int, amount: float, reason: str = None):
    """Deduct credits from user"""
    credits = await get_or_create_user_credits(db, user_id)
    
    if credits.available_credits < amount:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail="Insufficient credits"
        )
    
    credits.used_credits += amount
    credits.available_credits -= amount
    
    # Create transaction
    transaction = CreditTransaction(
        user_id=user_id,
        transaction_type=TransactionType.USE,
        amount=-amount,
        reason=reason
    )
    
    db.add(transaction)
    db.commit()
    db.refresh(credits)

async def add_credits(db: Session, user_id: int, amount: float, reason: str = None):
    """Add credits to user"""
    credits = await get_or_create_user_credits(db, user_id)
    
    credits.total_credits += amount
    credits.available_credits += amount
    
    # Create transaction
    transaction = CreditTransaction(
        user_id=user_id,
        transaction_type=TransactionType.PURCHASE,
        amount=amount,
        reason=reason
    )
    
    db.add(transaction)
    db.commit()
    db.refresh(credits)

async def reset_monthly_credits(db: Session, user_id: int):
    """Reset monthly credits"""
    credits = await get_or_create_user_credits(db, user_id)
    
    credits.total_credits = 10.0
    credits.available_credits = 10.0
    credits.used_credits = 0.0
    credits.last_reset = datetime.utcnow()
    credits.next_reset = datetime.utcnow() + timedelta(days=30)
    
    db.commit()
    db.refresh(credits)
