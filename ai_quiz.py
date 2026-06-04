import os
from google import genai
from dotenv import load_model, load_dotenv

# Load variables from the hidden .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the official Google GenAI Client
client = genai.Client(api_key=API_KEY)
print("🤖 AI Study Assistant Initialized!")
topic = input("Enter a topic you want to get tested on (e.g., Photosynthesis, French Revolution): ")

print(f"\n🧠 Generating a custom quiz on '{topic}' using Gemini...")

# Request the model to build a structured quiz
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Create a 10-question multiple choice quiz about {topic} suitable for a 9th grader. Provide the correct answers at the very bottom."
)

print("\n--- YOUR CUSTOM QUIZ ---")
print(response.text)
print("------------------------")