import sqlite3

def bazaya_yaz(records):
    try:
        with sqlite3.connect('baza.db') as db:
            cursor=db.cursor()
            print('Baza ile elaqe yaradildi')

            data_param="""INSERT INTO kitabxana (kitab_ad,muellif,janr,nesr) VALUES (?, ?, ?, ?)"""
            cursor.executemany(data_param,records)
            db.commit()
            print('Melumat bazaya ugurla elave edildi')
            cursor.close()
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)
    finally:
        if db:
            db.close()
            print('Baza baglandi')

records=[
    ('English','Henry','derslik','2022'),
    ('Tebiet','Samir Aslan', 'derslik','2023')

]

bazaya_yaz(records)