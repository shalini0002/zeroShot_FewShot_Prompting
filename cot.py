from google import genai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in environment variables")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an expert AI assistant.

Solve the user's query correctly.
Think step-by-step internally, but DO NOT reveal your chain of thought.

Return ONLY valid JSON in the following format:
{
  "result": "final answer as a string",
  "explanation": "short, clear explanation for the user"
}

No markdown.
No extra text.
"""

USER_INPUT = "Solve: 2 + 3 * 5 / 10"

# Generate response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{SYSTEM_PROMPT}\nUser input: {USER_INPUT}"
    # messages=[
    #     {"role": "system", "content": SYSTEM_PROMPT},
    #     {"role": "user", "content": USER_INPUT},
    # ]
)

# Print raw output
print("Raw model output:")
print(response.text)

# Parse JSON safely
try:
    parsed = json.loads(response.text)
    print("\nParsed Output:")
    print("Result:", parsed["result"])
    print("Explanation:", parsed["explanation"])
except json.JSONDecodeError:
    print("\n❌ Model did not return valid JSON")
