import sqlite3

def bazadan_silme(id):
    try:
        with sqlite3.connect('baza.db') as db:
            cursor = db.cursor()
            print('Baza ile elaqe yaradildi')

            query = """DELETE from kitabxana where id=?"""
            cursor.execute(query, (id, ))
            db.commit()
            print(cursor.rowcount, 'melumat bazadan silindi')
    except sqlite3.Error as error:
        print('Xeta bas verdi',error)
    finally:
        if db:
            db.close()
            print('Baza ile elaqe kesildi')

bazadan_silme(2)
