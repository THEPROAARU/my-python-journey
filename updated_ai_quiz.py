import os
from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv

# Load variables from the hidden .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Define our data schemas
class Question(BaseModel):
    question_text: str
    options: list[str]
    correct_option: str

class Quiz(BaseModel):
    topic: str
    questions: list[Question]

print("🤖 Smart AI Quiz Engine Initialized Securely!")
topic = input("Enter a topic to play an interactive quiz on: ")

print(f"\n🧠 Gemini is building your game data for '{topic}'...")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Create a 10-question multiple choice quiz about {topic} suitable for a 9th grader.",
    config={
        'response_mime_type': 'application/json',
        'response_schema': Quiz,
    },
)

quiz_data = Quiz.model_validate_json(response.text)

# --- THE GAME LOOP ---
print("\n🎮 GAME START! Answer by typing A, B, C, or D.\n" + "="*100)
score = 0
wrong_questions = [] # List to hold questions you missed

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
        # Record the missed question details
        wrong_questions.append({
            'question': q.question_text,
            'options': q.options,
            'correct': q.correct_option
        })

print("\n" + "="*100)
print(f"🏁 GAME OVER! Final Score: {score}/10")

# --- SAVE SCORECARD ---
filename = f"{topic.lower().replace(' ', '_')}_results.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Quiz Performance Tracking\nTopic: {topic}\nScore: {score}/10\n")
print(f"💾 Scorecard saved locally as: {filename}")

# --- NEW FEATURE: SAVE REVIEW SHEET IF YOU MISSED ANY ---
if wrong_questions:
    review_file = "needs_review.txt"
    # 'a' mode means APPEND so it adds to the file instead of overwriting old mistakes!
    with open(review_file, "a", encoding="utf-8") as file:
        file.write(f"\n=== Review Study Guide: {topic.upper()} ===\n")
        for w in wrong_questions:
            file.write(f"❓ Question: {w['question']}\n")
            file.write(f"💡 Correct Answer was: {w['correct']}\n")
            file.write("-" * 20 + "\n")
    print(f"📚 Missing concepts saved to study list: {review_file}")
else:
    print("🏆 Perfect score! No review sheet needed for this topic.")