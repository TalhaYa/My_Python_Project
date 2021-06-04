import sqlite3 as sql

vt= sql.connect('kisi.db')
imlec = vt.cursor()
imlec.execute("Create Table IF NOT EXISTS Giris(ad,soyad,yas,hes)")

kisi_bilgisi = []


ad = input("Adiniz:")
kisi_bilgisi.append(ad)
soyad = input("Soyadiniz: ")
kisi_bilgisi.append(soyad)
yas = int(input("Yasiniz: "))
kisi_bilgisi.append(yas)
hes = input("Hes kodunuz: ")
kisi_bilgisi.append(hes)

imlec.execute("Insert Into Giris values(?,?,?,?)", (ad, soyad, yas, hes))
vt.commit()
print("Sisteme Giren Kisi Kimdir? ")


