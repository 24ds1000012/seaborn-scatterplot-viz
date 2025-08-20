import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data
np.random.seed(42)
n = 150

# Example: Marketing spend vs customer acquisition
data = pd.DataFrame({
    "Marketing_Spend": np.random.normal(50000, 15000, n).clip(10000, 100000),
    "Customer_Acquisition": np.random.normal(500, 120, n).clip(100, 1000),
    "Channel": np.random.choice(["Social Media", "Email", "Search Ads", "Influencers"], n)
})

# Create scatterplot
plt.figure(figsize=(8, 8))  # ensures 512x512 output with dpi=64
scatter = sns.scatterplot(
    data=data,
    x="Marketing_Spend",
    y="Customer_Acquisition",
    hue="Channel",
    palette="Set2",
    s=80,
    alpha=0.8
)

# Add titles and labels
plt.title("Marketing Spend vs Customer Acquisition", fontsize=16, weight='bold')
plt.xlabel("Marketing Spend (USD)", fontsize=12)
plt.ylabel("Customers Acquired", fontsize=12)

# Improve layout
plt.legend(title="Channel", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save chart as 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
