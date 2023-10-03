import sqlite3

with sqlite3.connect("baza.db") as db:
    cursor=db.cursor()

kitab_adi=input("Kitabın adını daxil edin: ")
muellif=input("Müəllifin adı: ")
janr=input("Janrın adı: ")
nesr=input("Nəşrin ili: ")

cursor.execute("INSERT INTO kitabxana (kitab_ad, muellif, janr, nesr) VALUES (?, ?, ?, ?)", (kitab_adi, muellif, janr, nesr))
db.commit()

for value in cursor.execute("SELECT * FROM kitabxana"):
    print(value)

db.close()
