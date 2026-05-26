#  take the data from the excel file and create some charts to visualize the fee structure and payment status of students. We will use pandas to read the Excel file and matplotlib to create the charts.
import pandas as pd

df = pd.read_excel("fees_report.xlsx")

print(df.columns)

df.columns = [col.lower() for col in df.columns]


import matplotlib.pyplot as plt # pip install matplotlib

plt.figure()
plt.bar(df["class"].astype(str), df["balance"])
plt.xlabel("Class")
plt.ylabel("Balance")
plt.title("Balance by Class")
plt.show()


plt.figure()
plt.plot(df["class"], df["tuition"])
plt.plot(df["class"], df["transport"])
plt.plot(df["class"], df["hostel"])
plt.xlabel("Class")
plt.ylabel("Amount")
plt.title("Fee Components")
plt.show()


plt.figure()
plt.bar(df["class"].astype(str), df["total fees"])
plt.bar(df["class"].astype(str), df["paid"])
plt.xlabel("Class")
plt.ylabel("Amount")
plt.title("Total Fees vs Paid")
plt.show()

plt.figure()
plt.hist(df["balance"])
plt.xlabel("Balance")
plt.ylabel("Frequency")
plt.title("Balance Distribution")
plt.show()

plt.figure()
plt.scatter(df["paid"], df["balance"])
plt.xlabel("Paid")
plt.ylabel("Balance")
plt.title("Paid vs Balance")
plt.show()