from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App
    APP_NAME: str = "AI Content Generator"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "postgresql://h98r_user:h98r_password@localhost:5432/h98r"
    DATABASE_POOL_SIZE: int = 10
    DATABASE_MAX_OVERFLOW: int = 20
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    CORS_ORIGINS: str = "http://localhost:3000"
    
    # API Keys
    OPENAI_API_KEY: str = ""
    CLAUDE_API_KEY: str = ""
    COHERE_API_KEY: str = ""
    
    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "noreply@h98r.com"
    
    # Credits
    FREE_CREDITS_PER_MONTH: int = 10
    CREDIT_COST_GENERATE: float = 1.0
    CREDIT_COST_REWRITE: float = 0.5
    CREDIT_COST_ANALYZE: float = 0.5
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
