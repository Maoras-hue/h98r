from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.credit import TransactionType

class CreditResponse(BaseModel):
    id: int
    user_id: int
    total_credits: float
    used_credits: float
    available_credits: float
    last_reset: datetime
    next_reset: Optional[datetime]
    
    class Config:
        from_attributes = True

class CreditTransactionResponse(BaseModel):
    id: int
    user_id: int
    transaction_type: TransactionType
    amount: float
    reason: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True
