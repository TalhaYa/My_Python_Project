tum_siparis = {"Siparisleriniz": [], "Hesabınız": []}
aperatif = {"Kasarlı Tost": 6, "Kıymalı Tost": 8,
          "Sucuklu Yumurta": 10,"Karışık Tost": 10,
          "Sucuklu Tost": 7,"Soguk Sandvic":7}
print("*****Aperatif ÇEŞİTLERİMİZ*****")
print(aperatif)


def siparis(yemek):
    siparis_listesi = []
    adet = int(input("Kaç porsiyon sipariş edeceksiniz?"))

    def hesap(adisyon):
        adi_list = []
        if yemek == 'Kasarlı Tost':
            adisyon += 6 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Kıymalı Tost':
            adisyon += 8 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Sucuklu Yumurta':
            adisyon += 10 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Karışık Tost':
            adisyon += 10 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Sucuklu Tost':
            adisyon += 7 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)
        elif yemek == 'Soguk Sandvic':
            adisyon += 7 * adet
            adi_list.append(adisyon)
            tum_siparis["Hesabınız"].append(adisyon)

        return adi_list

    for i in range(0, adet):
        siparis_listesi.append(yemek)
    print(hesap(adisyon=0))
    return siparis_listesi


while True:
    yemek = input("İstediğiniz Aperatif Çeşiti nedir?")
    print(siparis(yemek))
    tum_siparis["Siparisleriniz"].append(yemek)
    print(tum_siparis)
    exit=int(input("Sipariş sizin için yeterli mi?(Evet=1 Hayır =2)"))
    if exit == 1:
        print("Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
        break
    elif exit ==2 :
        continue
