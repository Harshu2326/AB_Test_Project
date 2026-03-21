import pandas as pd
import numpy as np

# Fix random results
np.random.seed(42)

# Total users in the experiment
n = 8000

# Simulate user data
data = {
    "user_id": range(1, n+1),
    "group": np.random.choice(['A', 'B'], n),
    "converted": np.random.choice([0, 1], n, p=[0.87, 0.13])
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("ab_test_data.csv", index=False)

# Show first 5 rows
print(df.head())
# Load the dataset
df = pd.read_csv("ab_test_data.csv")

# Basic info about dataset
print("Dataset info:")
print(df.info())

# Check first 10 rows
print("\nFirst 10 rows:")
print(df.head(10))

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Check distribution of groups
print("\nGroup counts:")
print(df['group'].value_counts())

# Check conversion rate overall
print("\nOverall conversion rate:")
print(df['converted'].mean())
# Step 3: Conversion Rates by Group
conversion_rates = df.groupby('group')['converted'].mean()
print("\n===== Conversion Rates by Group =====")
print(conversion_rates)
from statsmodels.stats.proportion import proportions_ztest

# Number of conversions per group
conversions = [
    df[df.group=='A']['converted'].sum(),
    df[df.group=='B']['converted'].sum()
]

# Number of users per group
nobs = [
    df[df.group=='A'].shape[0],
    df[df.group=='B'].shape[0]
]

# Perform Z-test
z_stat, p_value = proportions_ztest(conversions, nobs)

print("\n===== Hypothesis Testing (Z-test) =====")
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret result
if p_value < 0.05:
    print("Result: Statistically significant difference ✅")
else:
    print("Result: No significant difference ❌")
    import matplotlib.pyplot as plt

# Conversion rates bar chart
conversion_rates.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title("Conversion Rates by Group")
plt.ylabel("Conversion Rate")
plt.ylim(0, 0.2)
plt.show()
import matplotlib.pyplot as plt

# Conversion rates by group
conversion_rates = df.groupby('group')['converted'].mean()

# Plot bar chart
plt.figure(figsize=(6,4))
conversion_rates.plot(kind='bar', color=['blue', 'orange'])
plt.title("Conversion Rates by Group")
plt.ylabel("Conversion Rate")
plt.ylim(0, 0.2)

# Save chart to screenshots folder
plt.savefig("screenshots/conversion_chart.png", bbox_inches='tight')
plt.show()