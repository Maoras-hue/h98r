# Deployment Guide

## Prerequisites

- GitHub account with repository access
- Vercel account (for frontend)
- Railway account (for backend)
- PostgreSQL database
- Redis instance

## Frontend Deployment (Vercel)

1. **Connect GitHub Repository**
   - Go to vercel.com
   - Click "Import Project"
   - Select your h98r repository
   - Configure build settings (defaults are fine)

2. **Set Environment Variables**
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-api.com
   ```

3. **Deploy**
   - Click "Deploy"
   - Vercel will automatically deploy on every push to main

## Backend Deployment (Railway)

1. **Connect GitHub Repository**
   - Go to railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose h98r repository

2. **Configure Environment Variables**
   ```
   DATABASE_URL=your_postgres_url
   REDIS_URL=your_redis_url
   OPENAI_API_KEY=your_key
   CLAUDE_API_KEY=your_key
   COHERE_API_KEY=your_key
   SECRET_KEY=your_secret_key
   ENVIRONMENT=production
   ```

3. **Database Setup**
   - Railway will automatically run migrations on deployment
   - Ensure database is accessible from Railway

4. **Deploy**
   - Railway will automatically deploy on every push to main

## Environment Configuration

### Production (.env)

```
ENVIRONMENT=production
DATABASE_URL=postgresql://user:password@host:5432/dbname
REDIS_URL=redis://host:6379/0
OPENAI_API_KEY=sk-...
CLAUDE_API_KEY=claude-...
COHERE_API_KEY=cohere-...
SECRET_KEY=your_super_secret_key_change_this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
CORS_ORIGINS=https://h98r.com,https://www.h98r.com
```

## Monitoring

- Monitor logs in Vercel dashboard
- Monitor logs in Railway dashboard
- Set up error tracking (Sentry, LogRocket)
- Monitor database performance

## Troubleshooting

### API Connection Issues
- Verify `NEXT_PUBLIC_API_URL` matches backend deployment URL
- Check CORS configuration in backend
- Verify firewall/network rules

### Database Connection Issues
- Verify `DATABASE_URL` is correct
- Check database permissions
- Ensure database is running and accessible

### Authentication Issues
- Verify `SECRET_KEY` is set
- Check token expiration settings
- Verify API endpoint accessibility

## CI/CD Pipeline

- Push to `develop` for staging
- Push to `main` for production
- All tests must pass before deployment
- Manual approval may be required for production
