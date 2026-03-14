import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv").dropna()
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.scatter(df["Temperature"], df["Humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Scatter Plot")

plt.subplot(1,2,2)
plt.hist(df["Temperature"])
plt.xlabel("Temperature")
plt.title("Histogram")
plt.tight_layout()
plt.show()