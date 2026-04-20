import sqlite3

conn = sqlite3.connect("experiment.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    treatment TEXT,
    concentration TEXT,
    trial1 REAL,
    trial2 REAL,
    trial3 REAL
)
""")

conn.commit()
conn.close()
