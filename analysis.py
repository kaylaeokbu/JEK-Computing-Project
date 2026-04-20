import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

print("Script is running...")

conn = sqlite3.connect("experiment.db")
df = pd.read_sql_query("SELECT * FROM results", conn)

df["average"] = df[["trial1", "trial2", "trial3"]].mean(axis=1)

print(df)

plt.figure()
plt.bar(df["treatment"], df["average"])
plt.xticks(rotation=45)
plt.show()