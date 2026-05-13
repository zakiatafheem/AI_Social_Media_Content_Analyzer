from groq import Groq
from dotenv import load_dotenv
import os

# -------------------------------
# LOAD ENV VARIABLES
# -------------------------------
load_dotenv()

# -------------------------------
# GET API KEY
# -------------------------------
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# -------------------------------
# CONFIGURE GROQ CLIENT
# -------------------------------
client = Groq(api_key=API_KEY)

# -------------------------------
# ANALYZE FUNCTION
# -------------------------------
def analyze_text(text):

    prompt = f"""
You are a social media content analyzer.

Analyze the following text and return:

1. Sentiment (Positive/Negative/Neutral)
2. Topic (Tech, Business, Sports, Entertainment, Other)
3. Content Type (Informative/Promotional/Opinion)
4. Short Summary (2 lines)
5. Engagement Suggestion (1 line)
6. Hashtags (3 hashtags)
7. Engagement Score (0–100)

TEXT:
{text}

Return in structured format.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].message.content