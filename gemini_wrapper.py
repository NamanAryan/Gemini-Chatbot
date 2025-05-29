import os
import httpx
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=API_KEY)

def generate_response(prompt: str):
    try:
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
        max_output_tokens=100,
        temperature=0.1
        )   
    )
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't process your request at the moment."
    

