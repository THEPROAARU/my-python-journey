import os
from google import genai
from dotenv import load_dotenv

# Load variables from the hidden .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the official Google GenAI Client
client = genai.Client(api_key=API_KEY)

print("🤖 AI Study Assistant Initialized Securely!")
topic = input("Enter a topic you want to get tested on (e.g., Photosynthesis, Fractions): ")

print(f"\n🧠 Generating a custom quiz on '{topic}' using Gemini...")

# Request the model to build a structured quiz
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Create a 10-question multiple choice quiz about {topic} suitable for a 9th grader. Provide the correct answers at the very bottom."
)

quiz_text = response.text

print("\n--- YOUR CUSTOM QUIZ ---")
print(quiz_text)
print("------------------------")

# --- NEW FEATURE: SAVE TO FILE ---
# Clean up the topic name to create a safe filename (e.g., "World War 2" -> "world_war_2_quiz.txt")
filename = f"{topic.lower().replace(' ', '_')}_quiz.txt"

# 'w' means open the file in "write" mode (creates the file if it doesn't exist)
with open(filename, "w", encoding="utf-8") as file:
    file.write(f"=== QUIZ TOPIC: {topic.upper()} ===\n\n")
    file.write(quiz_text)

print(f"💾 Success! Your quiz has been saved locally as: {filename}")