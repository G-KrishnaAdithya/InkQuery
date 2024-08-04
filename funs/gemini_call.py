
from config import GOOGLE_API_KEY
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)
def call_gemini_api(text): 
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(text)
    return response.text
    
    