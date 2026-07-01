# Setup Guide

## Quick Start with Docker

The easiest way to get started is using Docker Compose:

```bash
# Clone the repository
git clone https://github.com/Maoras-hue/h98r.git
cd h98r

# Start all services
docker-compose up -d

# Run database migrations
docker-compose exec backend python -m alembic upgrade head

# Access the applications
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

## Manual Setup

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis 6+

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run database migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Setup environment variables
cp .env.local.example .env.local
# Edit .env.local with your configuration

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Configuration

### Backend Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Application
ENVIRONMENT=development
DEBUG=true

# Database
DATABASE_URL=postgresql://h98r_user:h98r_password@localhost:5432/h98r
DATABASE_POOL_SIZE=10
DATABASE_MAX_OVERFLOW=20

# Redis
REDIS_URL=redis://localhost:6379/0

# API Keys
OPENAI_API_KEY=sk-your-key-here
CLAUDE_API_KEY=your-key-here
COHERE_API_KEY=your-key-here

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
CORS_ORIGINS=http://localhost:3000

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password

# Credits
FREE_CREDITS_PER_MONTH=10
CREDIT_COST_GENERATE=1
CREDIT_COST_REWRITE=0.5
CREDIT_COST_ANALYZE=0.5
```

### Frontend Environment Variables

Create a `.env.local` file in the `frontend/` directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=AI Content Generator
```

## Database Setup

### PostgreSQL

```bash
# Create database and user (if not using Docker)
createuser h98r_user
createdb -O h98r_user h98r

# Run migrations
cd backend
alembic upgrade head
```

### Redis

```bash
# Start Redis (if not using Docker)
redis-server
```

## Testing

### Backend Tests

```bash
cd backend
pytest
pytest --cov=app  # With coverage
```

### Frontend Tests

```bash
cd frontend
npm test
npm test -- --coverage  # With coverage
```

## Development

### Running Both Services

```bash
# Terminal 1: Backend
cd backend
source venv/bin/activate
uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm run dev
```

### Code Formatting

```bash
# Backend
cd backend
black .
isort .

# Frontend
cd frontend
npm run format
```

### Linting

```bash
# Backend
cd backend
flake8 .
mypy .

# Frontend
cd frontend
npm run lint
```

## Troubleshooting

### Port Already in Use

```bash
# Backend (8000)
lsof -i :8000
kill -9 <PID>

# Frontend (3000)
lsof -i :3000
kill -9 <PID>
```

### Database Connection Issues

```bash
# Check PostgreSQL is running
psql -U h98r_user -d h98r

# Check Redis is running
redis-cli ping
```

### Node Modules Issues

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Python Dependencies Issues

```bash
cd backend
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Support

For issues or questions:
1. Check the [CONTRIBUTING.md](CONTRIBUTING.md) guide
2. Open an issue on GitHub
3. Check existing issues for solutions

Happy coding! 🚀
