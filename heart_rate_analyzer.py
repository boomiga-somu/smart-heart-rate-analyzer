import pandas as pd
import matplotlib.pyplot as plt

def analyze_heart_rate(avg_hr):
    if avg_hr < 60:
        return "Low Heart Rate (Bradycardia)"
    elif 60 <= avg_hr <= 100:
        return "Normal Heart Rate"
    else:
        return "High Heart Rate (Tachycardia)"

# Load data
data = pd.read_csv("data/sample_heart_rate.csv")

time = data["time"]
heart_rate = data["heart_rate"]

average_hr = heart_rate.mean()
status = analyze_heart_rate(average_hr)

print("🫀 Smart Heart Rate Analyzer")
print("----------------------------")
print(f"Average Heart Rate: {average_hr:.2f} bpm")
print(f"Health Status     : {status}")

plt.figure(figsize=(8,4))
plt.plot(time, heart_rate, marker='o')
plt.xlabel("Time (seconds)")
plt.ylabel("Heart Rate (bpm)")
plt.title("Heart Rate Analysis")
plt.grid(True)
plt.show()
