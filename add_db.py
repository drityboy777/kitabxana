import sqlite3

def bazaya_elave_etmek():
    try:
        with sqlite3.connect('baza.db') as db:
            cursor = db.cursor()
            print('Database ile elaqe ugurla yaradildi!!!!')

            data_param = """INSERT INTO kitabxana(kitab_ad,muellif,janr,nesr) VALUES (?, ?, ?, ?)"""

            verilenler=[
                ("Salam Dunya","Herakl","dram","2000"),
                ("Heyatin sesi","Azad Salman","roman","1995")]
            cursor.executemany(data_param,verilenler)
            db.commit()
            print('Melumatlar bazaya ugurla elave edildi')
    except sqlite3.Error as error:
        print("Xeta bas verdi", error)

bazaya_elave_etmek()

