import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for temperature trends
days = np.arange(1, 8)
temperatures = [22, 24, 21, 19, 23, 25, 22]
rainfall = [5, 0, 8, 12, 0, 3, 7]
wind_speeds = [10, 15, 12, 8, 14, 18, 11]

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Weather Dashboard', fontsize=16)

# Temperature Trend Plot
sns.lineplot(x=days, y=temperatures, marker='o', ax=axes[0, 0], color='red')
axes[0, 0].set_title("Temperature Trends (°C)")
axes[0, 0].set_xlabel("Days")
axes[0, 0].set_ylabel("Temperature")

# Rainfall Analysis
sns.barplot(x=days, y=rainfall, ax=axes[0, 1], color='blue')
axes[0, 1].set_title("Rainfall (mm)")
axes[0, 1].set_xlabel("Days")
axes[0, 1].set_ylabel("Rainfall")

# Wind Speed Visualization
sns.barplot(x=days, y=wind_speeds, ax=axes[1, 0], color='green')
axes[1, 0].set_title("Wind Speed (km/h)")
axes[1, 0].set_xlabel("Days")
axes[1, 0].set_ylabel("Wind Speed")

# Calendar Heatmap (Simulated)
calendar_data = np.random.randint(0, 3, size=(5, 7))  # 5 weeks x 7 days (random weather states)
sns.heatmap(calendar_data, cmap="coolwarm", annot=True, ax=axes[1, 1])
axes[1, 1].set_title("Weather Pattern Heatmap")

# Adjust layout and save as an image
plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.savefig("weather_dashboard.png")  # Saves as an image
plt.show()
