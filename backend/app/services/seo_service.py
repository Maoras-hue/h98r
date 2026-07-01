from typing import Dict, List
import re
from collections import Counter

async def analyze_seo(content: str) -> Dict:
    """Analyze SEO score of content"""
    score = 0
    issues = []
    
    # Check length
    word_count = len(content.split())
    if word_count < 300:
        issues.append("Content is too short (minimum 300 words recommended)")
    else:
        score += 10
    
    # Check headings
    heading_count = len(re.findall(r'^#+', content, re.MULTILINE))
    if heading_count < 2:
        issues.append("Add more headings for better structure")
    else:
        score += 10
    
    # Check meta tags
    score += 5
    
    # Check readability
    readability = await check_readability(content)
    if readability["flesch_kincaid_grade"] > 8:
        issues.append("Content is too complex for readability")
    else:
        score += 10
    
    return {
        "seo_score": min(score, 100),
        "word_count": word_count,
        "heading_count": heading_count,
        "issues": issues,
        "recommendations": [
            "Use focus keywords naturally throughout the content",
            "Ensure proper heading hierarchy (H1, H2, H3)",
            "Add internal and external links",
            "Optimize meta description (150-160 characters)",
            "Use descriptive image alt texts"
        ]
    }

async def extract_keywords(content: str) -> List[str]:
    """Extract keywords from content"""
    # Simple keyword extraction
    words = re.findall(r'\b\w+\b', content.lower())
    # Filter stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'was'}
    keywords = [w for w in words if w not in stop_words and len(w) > 3]
    # Get most common
    counter = Counter(keywords)
    return [k for k, v in counter.most_common(10)]

async def generate_meta_tags(title: str, content: str) -> Dict:
    """Generate meta tags for content"""
    # Extract description from content
    sentences = content.split('.')
    description = sentences[0][:160] if sentences else ""
    
    # Extract keywords
    keywords = await extract_keywords(content)
    
    return {
        "title": title[:60],
        "description": description,
        "keywords": ",".join(keywords),
        "og_title": title[:60],
        "og_description": description[:120]
    }

async def check_readability(content: str) -> Dict:
    """Check readability metrics"""
    words = content.split()
    sentences = content.split('.')
    paragraphs = content.split('\n\n')
    
    word_count = len(words)
    sentence_count = len(sentences) - 1
    
    # Calculate Flesch Kincaid Grade
    syllables = 0
    for word in words:
        syllables += count_syllables(word)
    
    if sentence_count == 0:
        sentence_count = 1
    
    grade = (0.39 * (word_count / sentence_count) + 11.8 * (syllables / word_count) - 15.59)
    grade = max(0, grade)  # Ensure non-negative
    
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": len(paragraphs),
        "avg_words_per_sentence": round(word_count / sentence_count, 2) if sentence_count > 0 else 0,
        "flesch_kincaid_grade": round(grade, 2),
        "readability_level": "Easy" if grade < 6 else "Medium" if grade < 12 else "Hard"
    }

def count_syllables(word: str) -> int:
    """Count syllables in a word"""
    word = word.lower()
    syllable_count = 0
    vowels = "aeiou"
    previous_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel
    
    if word.endswith("e"):
        syllable_count -= 1
    if word.endswith("le") and len(word) > 2 and word[-3] not in vowels:
        syllable_count += 1
    
    return max(1, syllable_count)
