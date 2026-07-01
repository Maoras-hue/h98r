from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Enum
from sqlalchemy.sql import func
from datetime import datetime
from app.database import Base
import enum

class TransactionType(str, enum.Enum):
    PURCHASE = "purchase"
    USE = "use"
    REFUND = "refund"
    BONUS = "bonus"
    MONTHLY_RESET = "monthly_reset"

class UserCredit(Base):
    __tablename__ = "user_credits"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    total_credits = Column(Float, default=10.0)  # Free tier
    used_credits = Column(Float, default=0.0)
    available_credits = Column(Float, default=10.0)
    
    last_reset = Column(DateTime(timezone=True), server_default=func.now())
    next_reset = Column(DateTime(timezone=True))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<UserCredit {self.user_id}>"

class CreditTransaction(Base):
    __tablename__ = "credit_transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Float, nullable=False)
    reason = Column(String, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<CreditTransaction {self.id}>"
