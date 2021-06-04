tum_siparis = {"Siparisleriniz": [], "Hesabınız": []}
annem = {"Musakka": 12, "Kuru Fasulye": 9,
          "Taze Fasulye": 9,
          "Tavuklu Pilav": 10,
          "Ciger": 18}
print("*****Annem Yemek*****")
print(annem)


def siparis(yemek):
    siparis_listesi = []
    adet = int(input("Kaç adet pide sipariş edeceksiniz?"))

    def hesap(adisyon):
        adi_list = []
        if yemek == 'Musakka':
            adisyon += 12 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Kuru Fasulye':
            adisyon += 9 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Taze Fasulye':
            adisyon += 9 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Tavuklu Pilav':
            adisyon += 10 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Ciger':
            adisyon += 18 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        return adi_list

    for i in range(0, adet):
        siparis_listesi.append(yemek)
    print(hesap(adisyon=0))
    return siparis_listesi


while True:
    yemek = input("Menümüzden İstediginiz Çeşit nedir?")
    print(siparis(yemek))
    tum_siparis["Siparisleriniz"].append(yemek)
    print(tum_siparis)
    exit = int(input("Sipariş sizin için yeterli mi?(Evet=1 Hayır =2)"))
    if exit == 1:
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        break
    elif exit == 2:
        continue