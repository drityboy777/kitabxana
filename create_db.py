import sqlite3


with sqlite3.connect('baza.db') as db:
    cursor=db.cursor()

    query="""CREATE TABLE IF NOT EXISTS kitabxana(
    id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    kitab_ad TEXT,
    muellif TEXT,
    janr TEXT,
    nesr TEXT)"""

    cursor.execute(query)
db.commit()

print("Database ugurla yaradildi")


