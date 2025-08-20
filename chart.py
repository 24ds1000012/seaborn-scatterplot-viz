import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data
np.random.seed(42)
n = 150

data = pd.DataFrame({
    "Marketing_Spend": np.random.normal(50000, 15000, n).clip(10000, 100000),
    "Customer_Acquisition": np.random.normal(500, 120, n).clip(100, 1000),
    "Channel": np.random.choice(["Social Media", "Email", "Search Ads", "Influencers"], n)
})

# Create fixed-size figure
plt.figure(figsize=(8, 8), dpi=64)  # 8*64 = 512 pixels

sns.scatterplot(
    data=data,
    x="Marketing_Spend",
    y="Customer_Acquisition",
    hue="Channel",
    palette="Set2",
    s=80,
    alpha=0.8
)

# Titles and labels
plt.title("Marketing Spend vs Customer Acquisition", fontsize=16, weight='bold')
plt.xlabel("Marketing Spend (USD)", fontsize=12)
plt.ylabel("Customers Acquired", fontsize=12)

# Legend
plt.legend(title="Channel", bbox_to_anchor=(1.05, 1), loc='upper left')

# Save exact 512x512 image (no bbox_inches!)
plt.savefig("chart.png", dpi=64)
