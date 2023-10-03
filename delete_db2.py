import sqlite3

def bazadan_silmek(id_list):
    try:
        with sqlite3.connect('baza.db') as db:
            cursor=db.cursor()
            print('Baza ile elaqe yaradildi')

            query="DELETE FROM kitabxana where id=?"
            cursor.executemany(query,id_list)
            db.commit()
            print('Bazadan', cursor.rowcount,' data silindi')
    except sqlite3.Error as error:
        print('Xeta bas verdi: ', error)
    finally:
        if db:
            db.close()
            print('Baza ile elaqe kesildi')

verilenler=[(5,),(6,)]

bazadan_silmek(verilenler)