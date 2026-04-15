import pandas as pd

# Load both result files
normal_df = pd.read_csv("normal_results.csv")
attack_df = pd.read_csv("attack_results.csv")

# Count anomalies
normal_anomalies = (normal_df["Result"] == "Anomaly").sum()
attack_anomalies = (attack_df["Result"] == "Anomaly").sum()

# Total rows
normal_total = len(normal_df)
attack_total = len(attack_df)

# Percentages
normal_percent = (normal_anomalies / normal_total) * 100
attack_percent = (attack_anomalies / attack_total) * 100

# Print results
print("=== COMPARISON RESULTS ===\n")

print(f"Normal Traffic:")
print(f"Total Packets: {normal_total}")
print(f"Anomalies: {normal_anomalies}")
print(f"Anomaly Rate: {normal_percent:.2f}%\n")

print(f"Attack Traffic:")
print(f"Total Packets: {attack_total}")
print(f"Anomalies: {attack_anomalies}")
print(f"Anomaly Rate: {attack_percent:.2f}%\n")

# Final conclusion
if attack_percent > normal_percent:
    print("Conclusion: Attack traffic shows MORE anomalies ✅")
else:
    print("Conclusion: No significant difference ❌")