import pandas as pd

# 1. Create a quick, mock dataset
data = {
    'Player': ['Aarush', 'Alex', 'Sophia', 'Ryan', 'Emma'],
    'Score': [185, 95, 210, 140, 165],
    'Game': ['Minecraft', 'Fortnite', 'Minecraft', 'Valorant', 'Fortnite']
}

df = pd.DataFrame(data)
print("📊 THE FULL DATAFRAME:")
print(df)
print("-" * 40)

# 2. Under the Hood: How filtering actually works
# This creates a list of True/False values based on our condition
score_filter = df['Score'] > 150

print("🧠 STEP 1: What the condition actually looks like to Python:")
print(score_filter)
print("-" * 40)

# 3. Apply the filter to select data
# Passing the True/False list into df[] tells Pandas: "Only keep rows that are True"
high_scorers = df[score_filter]

print("🏆 STEP 2: The filtered data (Score > 150):")
print(high_scorers)