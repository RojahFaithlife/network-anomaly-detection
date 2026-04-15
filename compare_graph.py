import pandas as pd
import matplotlib.pyplot as plt

# Load data
normal_df = pd.read_csv("normal_results.csv")
attack_df = pd.read_csv("attack_results.csv")

# Count anomalies
normal_anomalies = (normal_df["Result"] == "Anomaly").sum()
attack_anomalies = (attack_df["Result"] == "Anomaly").sum()

# Total packets
normal_total = len(normal_df)
attack_total = len(attack_df)

# Convert to percentages
normal_rate = (normal_anomalies / normal_total) * 100
attack_rate = (attack_anomalies / attack_total) * 100

# Data for graph
labels = ["Normal Traffic", "Attack Traffic"]
values = [normal_rate, attack_rate]

# Create bar chart
plt.bar(labels, values)

# Labels and title
plt.title("Network Anomaly Rate Comparison")
plt.ylabel("Anomaly Rate (%)")

# Show values on top of bars
for i, v in enumerate(values):
    plt.text(i, v + 0.5, f"{v:.2f}%", ha='center')

# Show graph
plt.show()