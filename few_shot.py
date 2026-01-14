#few short prompting
from google import genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

client = genai.Client(api_key=API_KEY)

few_shot_prompt = """
You are a developer posting on Twitter (X).

Tone rules:
- Confident
- Calm comeback energy
- Learning-focused
- Max 280 characters
- Use 1–2 hashtags

Examples:

Tweet 1:
"Took a short pause. Came back with better clarity.
Learning, building, and moving forward — one commit at a time. 🚀
#TechJourney"

Tweet 2:
"Breaks don’t stop growth — they sharpen it.
Back to building, back to learning, back to leveling up. 💻
#DeveloperLife"

Tweet 3:
"Stepping back gave me perspective.
Now it’s time to build smarter and ship better. ⚡
#BuildInPublic"

Now generate a similar tweet for:
A developer returning after a 2-month break.
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=few_shot_prompt
)

print(response.text)
