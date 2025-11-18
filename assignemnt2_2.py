import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for temperature trends
days = np.arange(1, 8)
temperatures = [22, 24, 21, 19, 23, 25, 22]
rainfall = [5, 0, 8, 12, 0, 3, 7]
wind_speeds = [10, 15, 12, 8, 14, 18, 11]

# Historical Overview: Simulated month-long data
np.random.seed(0)
month_days = np.arange(1, 31)
weather_types = np.random.choice(['Sunny', 'Cloudy', 'Rainy'], size=30)
weather_colors = {'Sunny': 'yellow', 'Cloudy': 'gray', 'Rainy': 'blue'}
weather_colors_map = [weather_colors[w] for w in weather_types]

# Create a figure with multiple subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 15))
fig.suptitle('Weather Dashboard', fontsize=16)

# Temperature Trend Plot
sns.lineplot(x=days, y=temperatures, marker='o', ax=axes[0, 0], color='red', label='Temperature')
axes[0, 0].set_title("Temperature Trends (°C)")
axes[0, 0].set_xlabel("Days")
axes[0, 0].set_ylabel("Temperature")
axes[0, 0].legend()

# Rainfall Analysis
sns.barplot(x=days, y=rainfall, ax=axes[0, 1], color='blue', label='Rainfall')
axes[0, 1].set_title("Rainfall (mm)")
axes[0, 1].set_xlabel("Days")
axes[0, 1].set_ylabel("Rainfall")
axes[0, 1].legend()

# Wind Speed Visualization
sns.barplot(x=days, y=wind_speeds, ax=axes[1, 0], color='green', label='Wind Speed')
axes[1, 0].set_title("Wind Speed (km/h)")
axes[1, 0].set_xlabel("Days")
axes[1, 0].set_ylabel("Wind Speed")
axes[1, 0].legend()

# Calendar Heatmap for Historical Overview
calendar_data = np.random.randint(0, 3, size=(5, 7))  # 5 weeks x 7 days (random weather states)
sns.heatmap(calendar_data, cmap="coolwarm", annot=True, ax=axes[1, 1])
axes[1, 1].set_title("Weather Pattern Heatmap")

# Historical Overview - Month-long View
axes[2, 0].bar(month_days, np.ones_like(month_days), color=weather_colors_map, edgecolor='black')
axes[2, 0].set_title("Historical Overview")
axes[2, 0].set_xlabel("Days")
axes[2, 0].set_ylabel("Weather Type")

# Add a legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=color, label=label) for label, color in weather_colors.items()]
axes[2, 0].legend(handles=legend_elements, title="Weather Types")

# Placeholder for Interactive Elements (Conceptual)
axes[2, 1].text(0.5, 0.5, "Interactive Features Placeholder:\n- Click to View Details\n- Apply Filters\n- Compare Trends", ha='center', va='center', fontsize=12)
axes[2, 1].axis('off')
axes[2, 1].set_title("Interactive Features")

# Adjust layout and save as an image
plt.tight_layout()
plt.subplots_adjust(top=0.95)
plt.savefig("weather_dashboard.png", dpi=300)  # Saves as a high-quality image
plt.show()
