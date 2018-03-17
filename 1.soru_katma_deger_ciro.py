toplamSatis=int(input(" Toplam Satış miktarını giriniz: "))
hammaddeMaliyet=int(input("Hammadde maliyetini giriniz: "))
bakimOnarim=int(input("Bakım Onarım Giderlerini giriniz: "))
sevkiyatGider=int(input("Sevkiyat Giderlerini giriniz: "))
satinAlinanHizmet=int(input("Satın Alınan Hizmet Giderlerini giriniz: "))

def giderHesapla(hammaddeMaliyet,bakimOnarim,sevkiyatGider,satinAlinanHizmet):
    global toplamGider
    toplamGider=hammaddeMaliyet+bakimOnarim+sevkiyatGider+satinAlinanHizmet
    return toplamGider

def KatmaDegerCiroHesapla(toplamSatis,toplamGider):
    katmaDegerCiro=toplamSatis-toplamGider
    print(katmaDegerCiro)

    if(katmaDegerCiro>=1000):
        print("İşletme katma değer cirosu yüksek")
    elif(500<=katmaDegerCiro<=999):
        print("işletme katma değer cirosu normal")

    else:
        print("işletme katma değer cirosu düşük")

gelir=toplamSatis
gider=giderHesapla(hammaddeMaliyet,bakimOnarim,sevkiyatGider,satinAlinanHizmet)
KatmaDegerCiroHesapla(toplamSatis,toplamGider)
