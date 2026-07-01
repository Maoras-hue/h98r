# Contributing to H98R

Thank you for your interest in contributing to H98R! We welcome contributions from the community.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/h98r.git`
3. Create a feature branch: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Development Setup

### Prerequisites
- Docker & Docker Compose (recommended)
- OR:
  - Python 3.11+
  - Node.js 18+
  - PostgreSQL 14+
  - Redis 6+

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

## Code Style

### Backend (Python)
- Use Black for code formatting
- Use isort for import sorting
- Follow PEP 8
- Use type hints

```bash
black .
isort .
flake8 .
mypy .
```

### Frontend (TypeScript/React)
- Use Prettier for formatting
- Use ESLint for linting
- Follow React best practices

```bash
npm run format
npm run lint
npm run type-check
```

## Testing

### Backend
```bash
cd backend
pytest
pytest --cov=app
```

### Frontend
```bash
cd frontend
npm test
npm test -- --coverage
```

## Pull Request Process

1. Ensure all tests pass: `pytest` (backend) and `npm test` (frontend)
2. Update documentation if needed
3. Add tests for new features
4. Follow the PR title format: `[Feature/Fix/Docs] Description`
5. Link related issues
6. Request review from maintainers

## Code of Conduct

Please be respectful and constructive in all interactions.

## Questions?

Open an issue or reach out to the maintainers.

Happy coding! 🚀
