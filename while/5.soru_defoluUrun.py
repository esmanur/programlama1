i = 1 # gun sayaci
toplamDefoluUrunSayisi=0

#while'da döngü verilen karşılaştırma doğru olana kadar devam eder

while 1:
    gunlukDefoluUrunSayisi=int(input("Bugün kaç defolu ürün çıktı?"))
    toplamDefoluUrunSayisi+=gunlukDefoluUrunSayisi

#defolu ürün sorusu 200den fazlaysa

    if (toplamDefoluUrunSayisi > (200 * i)):
        print("Bugüne kadar ürettiğiniz defolu ürün oranı toplam üretiminizin %20'sinden fazla daha fazla üretim yapamazsınız!")

#döngü durdurmak için break komutu
        break
    print(i,"gün boyunca toplam",(i * 200),"adet ürün ürettiniz.Bunlardan",toplamDefoluUrunSayisi," adedi defoludur")


#Günlük defolu ürün sayısı günlük üretilen ürün sayısından %20 fazla olduğunda
    if (gunlukDefoluUrunSayisi > (200 * 20 / 100)):
        print("Dikkat bugün ürettiğiniz defolu ürün sayısı çok fazladır.")

    i += 1






