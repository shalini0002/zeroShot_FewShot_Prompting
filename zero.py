#zero short prompting
import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

zero_shot_prompt = """
You are a developer posting on Twitter (X).

Write a short, confident, and motivating tech-related Twitter post.

Context:
- I am returning after a 2-month break
- I work in tech and learning GenAI, backend, and frontend
- Tone: confident, positive, growth-focused
- Max 280 characters
- Use 1–2 hashtags

Generate only the tweet text.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=zero_shot_prompt
)

print(response.text)
