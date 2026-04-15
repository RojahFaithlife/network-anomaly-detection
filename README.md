# 🔐 Network Traffic Anomaly Detection System

## 📌 Overview
This project is a machine learning-based intrusion detection system (IDS) that analyzes network traffic and detects abnormal behavior using anomaly detection techniques.

It compares normal network traffic with simulated attack traffic generated through port scanning activity.

---

## 🎯 Goal
- Detect anomalies in network traffic
- Compare normal vs attack behavior
- Explore limitations of packet-level detection

---

## 🧠 How It Works
1. Network traffic is captured and exported as CSV
2. Features are extracted from packet data
3. An Isolation Forest model is trained
4. The model classifies traffic as:
   - Normal
   - Anomaly
5. Results are compared between datasets

---

## ⚙️ Tools Used
- Python
- Pandas
- Scikit-learn
- Wireshark (packet capture)
- Nmap (attack simulation)

---

## 📊 Key Insight
Packet-level features alone are not always sufficient to clearly distinguish between normal traffic and scan-based attack traffic. Behavioral and time-based features improve detection accuracy.

---

## 📁 Project Structure
- anomaly_detector.py → ML model
- compare_results.py → analysis script
- visualize.py → graphs
- normal_results.csv → normal traffic results
- attack_results.csv → attack traffic results

---

## 🚀 Future Improvements
- Add time-based features
- Real-time traffic monitoring
- Web dashboard for visualization
- Advanced anomaly detection models

---

## 👨‍💻 Author
Kokou Eklou Agnide | 
Computer Science Student | 
Focus: Networking, Security, Machine Learning