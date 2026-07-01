# AI Content Generator & SEO Optimizer ⭐⭐⭐⭐⭐

A comprehensive SaaS platform for generating high-quality content with built-in SEO optimization. Generate blog posts, social media content, email newsletters, and more with AI-powered tools.

## Features

✨ **Content Generation**
- Generate blog posts with proper structure
- Create social media content (Twitter, LinkedIn, Instagram)
- Compose professional email newsletters
- Multi-language support (50+ languages)

🔍 **SEO Optimization**
- Keyword density analysis
- Meta description generation
- Heading optimization
- Semantic search with pgvector
- Readability scoring

🎨 **Content Tools**
- AI-powered content rewriting
- Paraphrasing with multiple styles
- Tone adjustment (professional, casual, funny, formal)
- Grammar and plagiarism checking

💰 **Monetization**
- Freemium model: 10 free credits/month
- Premium tier: $29/month (unlimited content)
- Pay-as-you-go options

## Tech Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **Tailwind CSS** - Utility-first CSS framework
- **TypeScript** - Type-safe JavaScript
- **React Query** - Data fetching and caching
- **Zustand** - State management

### Backend
- **Python 3.11** - Core language
- **FastAPI** - High-performance async web framework
- **Pydantic** - Data validation
- **SQLAlchemy** - ORM for database

### Database & Cache
- **PostgreSQL** - Primary database
- **pgvector** - Vector similarity search
- **Redis** - Caching and rate limiting

### AI/ML
- **OpenAI GPT-4** - Primary AI model
- **Anthropic Claude API** - Secondary AI model
- **Cohere** - Semantic embeddings

### Deployment
- **Vercel** - Frontend hosting
- **Railway** - Backend hosting
- **Docker** - Containerization

## Project Structure

```
h98r/
├── frontend/              # Next.js application
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── styles/
│   └── public/
├── backend/               # FastAPI application
│   ├── app/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── routes/
│   └── config/
├── docker-compose.yml     # Development environment
├── .github/workflows/     # CI/CD pipelines
└── docs/                  # Documentation
```

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 14+
- Redis 6+
- Docker & Docker Compose (optional)

### Setup with Docker

```bash
# Clone repository
git clone https://github.com/Maoras-hue/h98r.git
cd h98r

# Start all services
docker-compose up -d

# Run migrations
docker-compose exec backend python -m alembic upgrade head

# Access applications
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Manual Setup

#### Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your configuration

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend

# Install dependencies
npm install

# Setup environment
cp .env.local.example .env.local
# Edit .env.local with your configuration

# Start development server
npm run dev
```

## API Endpoints

### Content Generation
- `POST /api/v1/content/generate` - Generate content
- `POST /api/v1/content/rewrite` - Rewrite content
- `POST /api/v1/content/paraphrase` - Paraphrase content
- `POST /api/v1/content/tone` - Adjust tone

### SEO Optimization
- `POST /api/v1/seo/analyze` - Analyze SEO
- `POST /api/v1/seo/keywords` - Extract keywords
- `POST /api/v1/seo/meta` - Generate meta tags
- `GET /api/v1/seo/readability` - Check readability

### User Management
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login
- `POST /api/v1/auth/refresh` - Refresh token
- `GET /api/v1/users/me` - Get current user
- `GET /api/v1/users/credits` - Get remaining credits

### Admin
- `GET /api/v1/admin/stats` - Platform statistics
- `GET /api/v1/admin/users` - List users
- `POST /api/v1/admin/credits` - Manage user credits

## Environment Variables

See `.env.example` files in both `frontend/` and `backend/` directories.

## Development

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Code Quality

```bash
# Backend
cd backend
black . && isort . && flake8 . && mypy .

# Frontend
cd frontend
npm run lint && npm run type-check
```

## Deployment

### Deploy to Vercel (Frontend)

```bash
cd frontend
vercel deploy --prod
```

### Deploy to Railway (Backend)

```bash
# Connect Railway to GitHub
# Configure environment variables in Railway dashboard
# Deploy automatically on push to main
```

## Contributing

1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Commit changes: `git commit -m 'Add amazing feature'`
3. Push to branch: `git push origin feature/amazing-feature`
4. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For support, email support@h98r.com or open an issue on GitHub.

---

**Made with ❤️ by Maoras-hue**
