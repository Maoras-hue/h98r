# API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All endpoints except `/auth/register` and `/auth/login` require a Bearer token in the `Authorization` header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Authentication

#### Register User
```
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "password",
  "full_name": "Full Name"
}

Response: 200 OK
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "Full Name",
  "is_active": true,
  "is_premium": false,
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### Login
```
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password"
}

Response: 200 OK
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": { ... }
}
```

#### Get Current User
```
GET /auth/me
Authorization: Bearer <token>

Response: 200 OK
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  ...
}
```

### Content Generation

#### Generate Content
```
POST /content/generate
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "My Blog Post",
  "content_type": "blog_post",
  "tone": "professional",
  "language": "en",
  "keywords": "AI, content",
  "prompt": "Write about AI and content generation"
}

Response: 200 OK
{
  "id": 1,
  "user_id": 1,
  "title": "My Blog Post",
  "content": "Generated content here...",
  "content_type": "blog_post",
  "tone": "professional",
  "seo_score": 85.5,
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### Get User Contents
```
GET /content/?skip=0&limit=10
Authorization: Bearer <token>

Response: 200 OK
[
  {
    "id": 1,
    "title": "My Blog Post",
    ...
  }
]
```

#### Get Single Content
```
GET /content/{content_id}
Authorization: Bearer <token>

Response: 200 OK
{
  "id": 1,
  "title": "My Blog Post",
  ...
}
```

#### Rewrite Content
```
POST /content/rewrite
Authorization: Bearer <token>
Content-Type: application/json

{
  "content_id": 1,
  "tone": "casual",
  "style": "informal"
}

Response: 200 OK
{
  "id": 1,
  "content": "Rewritten content here...",
  ...
}
```

### SEO Optimization

#### Analyze SEO
```
POST /seo/analyze
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "Your content here..."
}

Response: 200 OK
{
  "seo_score": 85,
  "word_count": 500,
  "heading_count": 3,
  "issues": ["Content is too short"],
  "recommendations": ["Add more headings"]
}
```

#### Extract Keywords
```
POST /seo/keywords
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "Your content here..."
}

Response: 200 OK
{
  "keywords": ["keyword1", "keyword2", "keyword3"]
}
```

#### Generate Meta Tags
```
POST /seo/meta
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Page Title",
  "content": "Page content..."
}

Response: 200 OK
{
  "title": "Page Title",
  "description": "Meta description...",
  "keywords": "keyword1,keyword2",
  "og_title": "Page Title",
  "og_description": "Meta description..."
}
```

#### Check Readability
```
POST /seo/readability
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "Your content here..."
}

Response: 200 OK
{
  "word_count": 500,
  "sentence_count": 25,
  "paragraph_count": 5,
  "avg_words_per_sentence": 20,
  "flesch_kincaid_grade": 8.5,
  "readability_level": "Medium"
}
```

### User Management

#### Get Current User Profile
```
GET /users/me
Authorization: Bearer <token>

Response: 200 OK
{
  "id": 1,
  "email": "user@example.com",
  ...
}
```

#### Update Profile
```
PUT /users/me
Authorization: Bearer <token>
Content-Type: application/json

{
  "full_name": "New Name",
  "bio": "My bio",
  "profile_picture": "url"
}

Response: 200 OK
{
  "id": 1,
  ...
}
```

#### Get Credits
```
GET /users/credits
Authorization: Bearer <token>

Response: 200 OK
{
  "id": 1,
  "user_id": 1,
  "total_credits": 10,
  "used_credits": 2,
  "available_credits": 8,
  "last_reset": "2024-01-01T00:00:00Z",
  "next_reset": "2024-02-01T00:00:00Z"
}
```

### Admin

#### Get Statistics
```
GET /admin/stats
Authorization: Bearer <admin_token>

Response: 200 OK
{
  "total_users": 100,
  "total_content": 500
}
```

#### List Users
```
GET /admin/users?skip=0&limit=10
Authorization: Bearer <admin_token>

Response: 200 OK
[
  {
    "id": 1,
    "email": "user@example.com",
    ...
  }
]
```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request data"
}
```

### 401 Unauthorized
```json
{
  "detail": "Invalid credentials"
}
```

### 402 Payment Required
```json
{
  "detail": "Insufficient credits"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

- 100 requests per hour per IP
- Returns `429 Too Many Requests` when exceeded

## Content Types

- `blog_post`
- `social_media`
- `email`
- `newsletter`
- `ad_copy`
- `product_description`

## Tones

- `professional`
- `casual`
- `funny`
- `formal`
- `friendly`

## Languages

- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- And 45+ more...
