tum_siparis = {"Siparisleriniz": [], "Hesabınız": []}
hamburg = {"huupir": 22, "Köfteburger": 24,
          "Etli Master": 27,
          "Chicken King": 17,
          "Buyuk Kral": 23,}
print("*****Hamburger CESITLERIMIZ*****")
print(hamburg)


def siparis(yemek):
    siparis_listesi = []
    adet = int(input("Kaç adet pide sipariş edeceksiniz?"))

    def hesap(adisyon):
        adi_list = []
        if yemek == 'huupir':
            adisyon += 22 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Köfteburger':
            adisyon += 24 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Etli Master':
            adisyon += 27 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Chicken King':
            adisyon += 17 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Buyuk Kral':
            adisyon += 23 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        return adi_list

    siparis_listesi.append(yemek)
    print(hesap(adisyon=0))
    return siparis_listesi


while True:
    yemek = input("İstediğiniz Hamburger Çeşiti nedir?")
    print(siparis(yemek))
    tum_siparis["Siparisleriniz"].append(yemek)
    print(tum_siparis)
    exit = int(input("Sipariş sizin için yeterli mi?(Evet=1 Hayır =2)"))
    if exit == 1:
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        break
    elif exit == 2:
        continue
