tum_siparis = {"Siparisleriniz": [], "Hesabınız": []}
pideci = {"Kasarlı": 15, "Kıymalı Kasarlı": 18,
          "Kıymalı": 16,
          "Sucuklu Kasarlı": 15,
          "Kusbasılı": 18}
print("*****PİDE ÇEŞİTLERİMİZ*****")
print(pideci)


def siparis(yemek):
    siparis_listesi = []
    adet = int(input("Kaç adet pide sipariş edeceksiniz?"))

    def hesap(adisyon):
        adi_list = []
        if yemek == 'Kasarlı':
            adisyon += 15 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Kıymalı':
            adisyon += 16 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Kıymalı Kasarlı':
            adisyon += 18 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Sucuklu Kasarlı':
            adisyon += 15 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Kusbasılı':
            adisyon += 18 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        return adi_list

    siparis_listesi.append(yemek)
    print(hesap(adisyon=0))
    return siparis_listesi


while True:
    yemek = input("İstediğiniz Pide Çeşiti nedir?")
    print(siparis(yemek))
    tum_siparis["Siparisleriniz"].append(yemek)
    print(tum_siparis)
    exit = int(input("Sipariş sizin için yeterli mi?(Evet=1 Hayır =2)"))
    if exit == 1:
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        break
    elif exit == 2:
        continue
