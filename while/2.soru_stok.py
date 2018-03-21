satilanUrun=500
alinanUrun=100
stok2017=10000
i=0
while True:
    stok2017=(stok2017-satilanUrun)+alinanUrun
    i=i+1
    if(stok2017==0):
        print(i,".ayda stok sıfırlanacaktır.")
