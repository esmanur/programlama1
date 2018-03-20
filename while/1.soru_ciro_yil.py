satis_miktar=500
birim_fiyat=20
ciro=5000
i=0
while True:
    satis_miktar=satis_miktar+200
    birim_fiyat=birim_fiyat+10
    i=i+1
    ciro=satis_miktar*birim_fiyat
    if(ciro>500000):
        print("İşletme",i, "ay sonra kar eder.")
        break
