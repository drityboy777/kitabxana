import sqlite3

def baza_yenile_qrup(record_list):
    try:
        with sqlite3.connect('baza.db') as db:
            cursor = db.cursor()
            print('Baza ile elaqe yaradildi')

            query="""UPDATE kitabxana set nesr=? where id=?"""
            cursor.executemany(query,record_list)
            db.commit()
            print('Bazada',cursor.rowcount,' data yenilendi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)
    finally:
        if db:
            db.close()
            print('Bazaz ile elaqe kesildi')

verilenler=[
    ("4444",3),
    ("5555",4),
    ("6666",5)
]

baza_yenile_qrup(verilenler)