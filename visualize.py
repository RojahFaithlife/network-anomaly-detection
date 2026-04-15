import pandas as pd
import matplotlib.pyplot as plt

# Load results from Step 3
df = pd.read_csv("results.csv")

# Convert labels to colors
colors = df["Result"].map({"Normal": "green", "Anomaly": "red"})

# Plot packet lengths
plt.scatter(df.index, df["Length"], c=colors)

plt.title("Network Traffic Anomaly Detection")
plt.xlabel("Packet Index")
plt.ylabel("Packet Length")

plt.show()
