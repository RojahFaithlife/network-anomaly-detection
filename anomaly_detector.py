import pandas as pd
from sklearn.ensemble import IsolationForest

# Load data (normal OR attack file)
df = pd.read_csv("attack_data.csv", encoding="latin1")# -----------------------------
# FEATURE ENGINEERING (IMPORTANT UPGRADE)
# -----------------------------

# 1. Convert protocol into numbers
df["Protocol_num"] = df["Protocol"].astype("category").cat.codes

# 2. Create simple traffic behavior feature (IP activity)
df["Packet_Count"] = df.groupby("Source")["Source"].transform("count")

# 3. Select better features
X = df[["Length", "Protocol_num", "Packet_Count"]]

# -----------------------------
# MODEL
# -----------------------------
model = IsolationForest(
    contamination=0.08,   # slightly higher sensitivity
    random_state=42
)

model.fit(X)

df["Result"] = model.predict(X)
df["Result"] = df["Result"].map({1: "Normal", -1: "Anomaly"})

# Save results
df.to_csv("attack_results.csv", index=False)
print("DONE — Check results.csv")