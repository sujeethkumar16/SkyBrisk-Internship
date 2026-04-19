import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

print("Initial Data:")
print(df.head())

df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')

df["director"].fillna("Unknown", inplace=True)
df["cast"].fillna("Unknown", inplace=True)
df["country"].fillna("Unknown", inplace=True)

df.dropna(subset=["date_added"], inplace=True)

df["year_added"] = df["date_added"].dt.year

df["release_decade"] = (df["release_year"] // 10) * 10

df["is_movie"] = df["type"].apply(lambda x: 1 if x == "Movie" else 0)

df["country"] = df["country"].str.split(", ")
df = df.explode("country")

df["listed_in"] = df["listed_in"].str.split(", ")
df = df.explode("listed_in")

print("\nTop 5 Countries:")
print(df["country"].value_counts().head(5))

print("\nTop 10 Genres:")
print(df["listed_in"].value_counts().head(10))

plt.figure()
df["type"].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Movies vs TV Shows")
plt.ylabel("")
plt.show()

plt.figure()
yearly = df["release_year"].value_counts().sort_index()
plt.plot(yearly.index, yearly.values)
plt.title("Content Released Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

plt.figure()
top_genres = df["listed_in"].value_counts().head(10)
top_genres.plot(kind='bar')
plt.title("Top 10 Genres")
plt.xticks(rotation=45)
plt.show()

plt.figure()
top_countries = df["country"].value_counts().head(10)
top_countries.plot(kind='bar')
plt.title("Top 10 Countries")
plt.xticks(rotation=45)
plt.show()

plt.figure()
trend = yearly.rolling(window=3).mean()

plt.plot(yearly.index, yearly.values, label="Actual")
plt.plot(trend.index, trend.values, linestyle='--', label="Trend")

plt.title("Content Growth Trend")
plt.xlabel("Year")
plt.ylabel("Count")
plt.legend()
plt.show()

print("\nSummary Statistics:")
print(df.describe(include='all'))

df.to_csv("cleaned_netflix_data.csv", index=False)
print("\n✅ Project Completed Successfully!")