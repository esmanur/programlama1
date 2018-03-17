koltukSayisi=int(input("Koltuk Sayısını giriniz: "))
yatakSayisi=int(input("Yatak Sayısını giriniz: "))
dolapSayisi=int(input("Dolap Sayısını giriniz: "))

def donembasiStokHesapla(koltukSayisi,yatakSayisi,dolapSayisi):
    global donembasiStok
    donembasiStok=koltukSayisi+yatakSayisi+dolapSayisi
    return donembasiStok


dsonu_koltuk=25
dsonu_yatak=20
dsonu_dolap=10

def donemsonuStokHesapla(dsonu_koltuk,dsonu_yatak,dsonu_dolap):
    global donemsonuStok
    donemsonuStok=dsonu_koltuk+dsonu_yatak+dsonu_dolap
    return donemsonuStok

def ortalamaStokHesapla(donembasi,donemsonu):
    global ortalamaStok
    ortalamaStok=(donembasi + donemsonu) / 2
    print(ortalamaStok)

donembasi=donembasiStokHesapla(koltukSayisi,yatakSayisi,dolapSayisi)
donemsonu=donemsonuStokHesapla(dsonu_koltuk,dsonu_yatak,dsonu_dolap)
ortalamaStokHesapla(donembasi,donemsonu)