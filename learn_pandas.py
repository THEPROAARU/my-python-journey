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
# 4. SORTING DATA
# We want to rank scores from HIGHEST to LOWEST
# ascending=False means go backwards (highest first)
sorted_df = df.sort_values(by='Score', ascending=False)

print("🏆 1. SORTED BY HIGHEST SCORE:")
print(sorted_df)
print("-" * 50)

# 5. GROUPING DATA (The part that makes Kaggle look tough)
# We want to see the AVERAGE score for each game type
# .groupby('Game') bundles matching games together, and ['Score'].mean() finds the average
game_stats = df.groupby('Game')['Score'].mean()

print("🎮 2. AVERAGE SCORE BY GAME TYPE:")
print(game_stats)