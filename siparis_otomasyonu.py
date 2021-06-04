# Sipariş Otomasyonu
"""
3-herhangi bir restorana girdiklerinde hoşgeldiniz isminiz soyisminiz eğer ekleyebilirsem yaşa göre indirim.
"""
adisyon = []
class Adisyon:
    def adisyonpideci(self):
        pide = [pideci.tum_siparis]
        adisyon.append(pide)
    def adisyonaperatif(self):
        ape = [MehmetAbiAperatif.tum_siparis]
        adisyon.append(ape)
    def adisyonsulu(self):
            ape = [AnnemYemek.tum_siparis]
            adisyon.append(ape)
    def adisyoncorba(self):
            ape = [corbacicuma.tum_siparis]
            adisyon.append(ape)
    def adisyonham(self):
            ape = [mcking.tum_siparis]
            adisyon.append(ape)
a = Adisyon()
import data
data

restoranlar = {"Kardeşler Pide": 1, "Annem Sulu Yemek": 2, "Mehmet Abiden Aperatif": 3,"Çorbacı Cuma":4,"Mc King":5}
print(restoranlar)
while True:
    sec = int(input("Nereden yemek isterdiniz (cıkıs(7)):"))
    if (sec == 1):
        import pideci
        pideci
        a.adisyonpideci()
        continue
    elif (sec == 2):
        import AnnemYemek
        AnnemYemek
        a.adisyonsulu()
        continue
    elif (sec == 3):
        import MehmetAbiAperatif
        MehmetAbiAperatif
        a.adisyonaperatif()
        continue
    elif (sec == 4):
        import corbacicuma
        corbacicuma
        a.adisyoncorba()
        continue
    elif (sec == 5):
        import mcking
        mcking
        a.adisyonham()
        continue
    elif (sec == 6):
        break

print(data.kisi_bilgisi)
print(adisyon)
sepet = open("sepet.txt", "w")
sepet.write(str(adisyon))
sepet.close()