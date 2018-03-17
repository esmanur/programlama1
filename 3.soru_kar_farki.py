yazilimGeliri = int(input("İlk 6 Aydaki Yazılım Gelirini giriniz: "))
finansmanGeliri=int(input("İlk 6 Aydaki Finansman Gelirini giriniz: "))
urunSatisGeliri=int(input("İlk 6 Aydaki Ürün Satış Gelirini giriniz: "))
calisanMaaslari=int(input("İlk 6 Aydaki Çalışan Maaşlarını giriniz: "))
kiraGideri=int(input("İlk 6 Aydaki Kira Giderini giriniz: "))
donanimMaliyeti=int(input("İlk 6 Aydaki Donanım Maliyetini giriniz: "))


def ilk_alti_ayGelirHesapla (yazilimGeliri,finansmanGeliri,urunSatisGeliri):
    global ilk_toplamGelir
    ilk_toplamGelir=yazilimGeliri+finansmanGeliri+urunSatisGeliri
    return ilk_toplamGelir

def ilk_alti_ayGiderHesapla(calisanMaaslari,kiraGideri,donanimMaliyeti):
    global ilk_toplamGider
    ilk_toplamGider=calisanMaaslari+kiraGideri+donanimMaliyeti
    return ilk_toplamGider

def ilk_altiay_karHesapla(ilk_gelir,ilk_gider):
    ilk_altiay_kar=ilk_gelir-ilk_gider
    return ilk_altiay_kar

ilk_gelir=ilk_alti_ayGelirHesapla(yazilimGeliri,finansmanGeliri,urunSatisGeliri)
ilk_gider=ilk_alti_ayGiderHesapla(calisanMaaslari,kiraGideri,donanimMaliyeti)
ilk_altiay_karHesapla(ilk_gelir,ilk_gider)


ikinciyazilimGeliri = int(input("Son 6 Aydaki Yazılım Gelirini giriniz: "))
sponsorlukGeliri=int(input("Son 6 Aydaki Sponsorluk Gelirini giriniz: "))
eTicaretGeliri=int(input("Son 6 Aydaki E-Ticaret Gelirini giriniz: "))
ikinciurunSatisGeliri=int(input("Son 6 Aydaki Ürün Satış Gelirini giriniz: "))
ikincicalisanMaaslari=int(input("Son 6 Aydaki Çalışan Maaşlarını giriniz: "))
ikincikiraGideri=int(input("Son 6 Aydaki Kira Giderini giriniz: "))
bakimMaliyeti=int(input("Son 6 Aydaki Bakım Maliyetini giriniz: "))


def son_alti_ayGelirHesapla(ikinciyazilimGeliri,sponsorlukGeliri,eTicaretGeliri,ikinciurunSatisGeliri):
    global son_toplamGelir
    son_toplamGelir=ikinciyazilimGeliri+sponsorlukGeliri+eTicaretGeliri+ikinciurunSatisGeliri
    return son_toplamGelir

def son_alti_ayGiderHesapla(ikincicalisanMaaslari,ikincikiraGideri,bakimMaliyeti):
    global son_toplamGider
    son_toplamGider=ikincicalisanMaaslari+ikincikiraGideri+bakimMaliyeti
    return son_toplamGider

def son_altiay_karHesapla(son_gelir,son_gider):
    son_altiay_kar=son_gelir-son_gider
    return son_altiay_kar

son_gelir=son_alti_ayGelirHesapla(ikinciyazilimGeliri,sponsorlukGeliri,eTicaretGeliri,ikinciurunSatisGeliri)
son_gider=son_alti_ayGiderHesapla(ikincicalisanMaaslari,ikincikiraGideri,bakimMaliyeti)
ilk_altiay_karHesapla(son_gelir,son_gider)

def kar_farkiHesapla(ilk_kar,son_kar):
    global karfarki
    karfarki=son_kar-ilk_kar
    print(karfarki)

    if (karfarki>= 5000):
        print("İşletme çok karlı")
    elif (1000<=karfarki<=5000):
        print("İşletme karı normal")
    else:
        print("İşletme yeterince karda değil")

ilk_kar = ilk_altiay_karHesapla(ilk_gelir, ilk_gider)
son_kar = son_altiay_karHesapla(son_gelir, son_gider)
kar_farkiHesapla(ilk_kar, son_kar)


