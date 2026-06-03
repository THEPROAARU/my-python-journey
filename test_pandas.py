# Learning Data Science and Git in 9th Grade!
import pandas as pd
import matplotlib.pyplot as plt

# Your study data
data = {
    "Day": ["Monday", "Tuesday", "Wednesday"],
    "Minutes_Coded": [30, 30, 45],
    "Topic": ["Pandas Intro", "Git Setup", "Data Viz"]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Create a bar graph
plt.bar(df["Day"], df["Minutes_Coded"], color="skyblue", edgecolor="black")

# Add labels and a title
plt.xlabel("Days of the Week")
plt.ylabel("Minutes Spent Coding")
plt.title("My Daily Coding Progress")

# Display the graph on your screen
plt.show()