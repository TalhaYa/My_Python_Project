tum_siparis = {"Siparisleriniz": [], "Hesabınız": []}
corba = {"Kelle Paca": 15, "İskembe": 18,
          "Mercimek": 8,
          "Ezogelin": 8,
          "Beyran": 18,}
print("*****CORBA CESITLERIMIZ*****")
print(corba)


def siparis(yemek):
    siparis_listesi = []
    adet = int(input("Kaç adet pide sipariş edeceksiniz?"))

    def hesap(adisyon):
        adi_list = []
        if yemek == 'Kelle Paca':
            adisyon += 15 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'İskembe':
            adisyon += 16 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Mercimek':
            adisyon += 8 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Ezogelin':
            adisyon += 15 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Beyran':
            adisyon += 18 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        return adi_list

    siparis_listesi.append(yemek)
    print(hesap(adisyon=0))
    return siparis_listesi


while True:
    yemek = input("İstediğiniz Çorba Çeşiti nedir?")
    print(siparis(yemek))
    tum_siparis["Siparisleriniz"].append(yemek)
    print(tum_siparis)
    exit = int(input("Sipariş sizin için yeterli mi?(Evet=1 Hayır =2)"))
    if exit == 1:
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        break
    elif exit == 2:
        continue
