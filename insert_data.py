import sqlite3

conn = sqlite3.connect("experiment.db")
cursor = conn.cursor()

data = [
    ("Vancomycin alone", "0%", 20, 19, 18),
    ("Vancomycin + Honey", "30%", 20, 19, 19),
    ("Vancomycin + Garlic", "5%", 29, 29, 28),
    ("Vancomycin + Garlic", "1%", 20, 19, 18.5),
    ("Vancomycin + Honey", "20%", 19, 19, 18.5)
]

cursor.executemany("""
INSERT INTO results (treatment, concentration, trial1, trial2, trial3)
VALUES (?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()