import pandas as pd

# Create a simple dataset of your study tracking
data = {
    "Day": ["Monday", "Tuesday", "Wednesday"],
    "Minutes_Coded": [30, 30, 45],
    "Topic": ["Pandas Intro", "Git Setup", "Local Test"]
}

df = pd.DataFrame(data)
print("My Progress So Far:")
print(df)
