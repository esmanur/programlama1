i=1 #Çalışan sayısı

butunPersonellereToplamAylikOdeme=0

while (i < 51):
    j=1 #hafta sayısı
    aylikToplamMesaiSaati=0

    while (j<=4):
        soru = i,".çalışan",j,".hafta kaç saat mesai yaptı?"
        haftalikMesaiSaati = int(input(soru))
        aylikToplamMesaiSaati += haftalikMesaiSaati

        j+=1

        if (aylikToplamMesaiSaati > 22):

            print("Bir personel aylık 22 saatten fazla çalışamaz!")
            aylikToplamMesaiSaati -= haftalikMesaiSaati
            #aylikToplamMesaiSaati=aylikToplamMesaiSaati-haftalikMesaiSaati


    personelAylikMaasi=((90*30)+(aylikToplamMesaiSaati*(90*10/100)))
    print("",i,".çalışan bu ay",personelAylikMaasi,"TL maaş alacaktır")

    butunPersonellereToplamAylikOdeme += personelAylikMaasi

    i+=1

print("İşletme bu ay bütün personellere toplam",personelAylikMaasi,"TL ödeme yapacaktır.")
