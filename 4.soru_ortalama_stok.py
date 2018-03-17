dbasi_koltukSayisi=int(input("Koltuk Sayısını giriniz: "))
dbasi_yatakSayisi=int(input("Yatak Sayısını giriniz: "))
dbasi_dolapSayisi=int(input("Dolap Sayısını giriniz: "))

def donembasiStokHesapla(dbasi_koltukSayisi,dbasi_yatakSayisi,dbasi_dolapSayisi):
    global donembasiStok
    donembasiStok=dbasi_koltukSayisi+dbasi_yatakSayisi+dbasi_dolapSayisi
    return donembasiStok


dsonu_koltukSayisi=25
dsonu_yatakSayisi=20
dsonu_dolapSayisi=10

def donemsonuStokHesapla(dsonu_koltukSayisi,dsonu_yatakSayisi,dsonu_dolapSayisi):
    global donemsonuStok
    donemsonuStok=dsonu_koltukSayisi+dsonu_yatakSayisi+dsonu_dolapSayisi
    return donemsonuStok

def ortalamaStokHesapla(donembasi,donemsonu):
    global ortalamaStok
    ortalamaStok=(donembasi + donemsonu) / 2
    print(ortalamaStok)

donembasi=donembasiStokHesapla(dbasi_koltukSayisi,dbasi_yatakSayisi,dbasi_dolapSayisi)
donemsonu=donemsonuStokHesapla(dsonu_koltukSayisi,dsonu_yatakSayisi,dsonu_dolapSayisi)
ortalamaStokHesapla(donembasi,donemsonu)