import sqlite3

def baza_yenile(id,name):
    try:
        with sqlite3.connect('baza.db') as db:
            cursor = db.cursor()
            print('Baza ile elaqe yaradildi')

            query="""UPDATE kitabxana set nesr=?  where id=? """
            data=(name,id)
            cursor.execute(query,data)
            db.commit()
            print('Baza yenilendi')
            cursor.close()
    except sqlite3.Error as error:
        print('Xeta bas verdi',error)
    finally:
        if db:
            db.close()
            print('Baza baglandi')

baza_yenile(3,'3000')

