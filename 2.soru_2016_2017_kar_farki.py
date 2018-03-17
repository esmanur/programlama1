calisilan_sure=170
toplam_musteri_sayisi=50

ikinci_calisilan_sure=calisilan_sure+50
ikinci_toplam_musteri_sayisi=toplam_musteri_sayisi+20

def ilk_yil_hesapla (calisilan_sure,toplam_musteri_sayisi):
    global musterilerle_calisma_suresi
    musterilerle_calisma_suresi=calisilan_sure/toplam_musteri_sayisi
    return musterilerle_calisma_suresi


def ikinci_yil_hesapla(ikinci_calisilan_sure,ikinci_toplam_musteri_sayisi):
    global ikinci_musterilerle_calisma_suresi
    ikinci_musterilerle_calisma_suresi=ikinci_calisilan_sure/ikinci_toplam_musteri_sayisi
    return ikinci_musterilerle_calisma_suresi

def kar_farkiHesapla(ilk_yil,ikinci_yil):
    global kar_farki
    kar_farki=ikinci_yil-ilk_yil
    print(kar_farki)


ilk_yil=ilk_yil_hesapla(calisilan_sure,toplam_musteri_sayisi)
ikinci_yil=ikinci_yil_hesapla(ikinci_calisilan_sure,ikinci_toplam_musteri_sayisi)
kar_farkiHesapla(ilk_yil,ikinci_yil)



