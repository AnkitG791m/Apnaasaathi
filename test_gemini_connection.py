import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

try:
    print("Testing gemini-2.0-flash...")
    model = genai.GenerativeModel("gemini-2.0-flash")
    resp = model.generate_content("Hello, do you work?")
    print(f"Success! Response: {resp.text}")
except Exception as e:
    print(f"Failed: {e}")
