import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_data.csv")

print("Original Data:")
print(df)

# Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Annual_Income"].fillna(df["Annual_Income"].mean(), inplace=True)

# Remove duplicates (if any)
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

df["Income_Level"] = df["Annual_Income"].apply(
    lambda x: "Low" if x < 55000 else ("Medium" if x < 65000 else "High")
)

df["Gender_Encoded"] = df["Gender"].map({"Male": 0, "Female": 1})

print("\nFeature Engineered Data:")
print(df)

plt.figure()
plt.scatter(df["Annual_Income"], df["Spending_Score"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Income vs Spending Score")
plt.show()

# Histogram: Age Distribution
plt.figure()
plt.hist(df["Age"])
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()

print("\nSummary Statistics:")
print(df.describe())