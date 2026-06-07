import os
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv

# Load variables from the hidden .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Define the structure of how we want our quiz data to look
class Question(BaseModel):
    question_text: str
    options: list[str]  # e.g., ["A) Text", "B) Text", "C) Text", "D) Text"]
    correct_option: str # e.g., "A" or "B" or "C" or "D"

class Quiz(BaseModel):
    topic: str
    questions: list[Question]

print("🤖 Interactive AI Quiz Engine Initialized Securely!")
topic = input("Enter a topic to play an interactive quiz on: ")

print(f"\n🧠 Gemini is building your game data for '{topic}'...")

# Fetch structured JSON data directly from the AI
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Create a 10-question multiple choice quiz about {topic} suitable for a 9th grader.",
    config={
        'response_mime_type': 'application/json',
        'response_schema': Quiz,
    },
)

# Parse the AI response into our Python data structure
quiz_data = Quiz.model_validate_json(response.text)

# --- THE GAME LOOP ---
print("\n🎮 GAME START! Answer by typing A, B, C, or D.\n" + "="*30)
score = 0

for i, q in enumerate(quiz_data.questions, 1):
    print(f"\n📋 Question {i}: {q.question_text}")
    for option in q.options:
        print(option)
        
    user_answer = input("Your Answer: ").strip().upper()
    
    if user_answer == q.correct_option.upper():
        print("✅ Correct! Brilliant job.")
        score += 1
    else:
        print(f"❌ Incorrect. The right answer was {q.correct_option}.")

print("\n" + "="*30)
print(f"🏁 GAME OVER! Final Score: {score}/10")

# --- SAVE RESULTS TO FILE ---
filename = f"{topic.lower().replace(' ', '_')}_results.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Quiz Performance Tracking\nTopic: {topic}\nScore: {score}/3\n")

print(f"💾 Scorecard saved locally as: {filename}")