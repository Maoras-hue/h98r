import openai
from app.config import settings
from app.models.content import ContentType, ContentTone
from typing import Dict, Optional

class AIService:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def generate_with_openai(self, prompt: str, content_type: ContentType, tone: ContentTone) -> Dict:
        """Generate content using OpenAI"""
        system_prompt = f"""You are a professional content writer. 
Generate high-quality content for {content_type.value} in a {tone.value} tone.
Make sure the content is engaging, well-structured, and SEO-optimized.
"""
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            content = response.choices[0].message.content
            tokens = response.usage.total_tokens
            
            return {
                "content": content,
                "model": "gpt-4",
                "tokens": tokens,
                "meta_description": content[:160]
            }
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
    
    async def rewrite_with_openai(self, content: str, tone: ContentTone, style: Optional[str] = None) -> Dict:
        """Rewrite content using OpenAI"""
        system_prompt = f"""You are a professional content editor.
Rewrite the given content in a {tone.value} tone.
{f'Apply {style} style.' if style else ''}
Keep the main message but make it more engaging.
"""
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": content}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            rewritten = response.choices[0].message.content
            tokens = response.usage.total_tokens
            
            return {
                "content": rewritten,
                "model": "gpt-4",
                "tokens": tokens
            }
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

ai_service = AIService()

async def generate_with_ai(prompt: str, content_type: ContentType, tone: ContentTone, language: str) -> Dict:
    """Generate content using AI"""
    return await ai_service.generate_with_openai(prompt, content_type, tone)

async def rewrite_with_ai(content: str, tone: ContentTone, style: Optional[str] = None) -> Dict:
    """Rewrite content using AI"""
    return await ai_service.rewrite_with_openai(content, tone, style)
