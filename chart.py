import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
np.random.seed(42)
n = 150
data = pd.DataFrame({
    "Marketing_Spend": np.random.normal(50000, 15000, n).clip(10000, 100000),
    "Customer_Acquisition": np.random.normal(500, 120, n).clip(100, 1000),
    "Channel": np.random.choice(["Social Media", "Email", "Search Ads", "Influencers"], n)
})

# Explicitly force 512x512 px
target_size = 512
dpi = 100  # pixels per inch
figsize = (target_size / dpi, target_size / dpi)  # (5.12, 5.12) inches

plt.figure(figsize=figsize, dpi=dpi)

sns.scatterplot(
    data=data,
    x="Marketing_Spend",
    y="Customer_Acquisition",
    hue="Channel",
    palette="Set2",
    s=80,
    alpha=0.8
)

plt.title("Marketing Spend vs Customer Acquisition", fontsize=14, weight="bold")
plt.xlabel("Marketing Spend (USD)", fontsize=12)
plt.ylabel("Customers Acquired", fontsize=12)
plt.legend(title="Channel", bbox_to_anchor=(1.05, 1), loc="upper left")

# Save image as EXACT 512x512 px
plt.savefig("chart.png", dpi=dpi)

