# x=Satış miktarı y=Birim satış fiyatı

x=int(input("Satış miktarını giriniz: "))
y=int(input("Birim satış fiyatını giriniz: "))

calisan_sayisi=25

ciro=x*y

def adambasi_ciro():
    adambasi_ciro=ciro/calisan_sayisi
    return adambasi_ciro


print(adambasi_ciro())