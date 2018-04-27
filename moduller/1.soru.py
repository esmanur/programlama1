
iyG=int(input("İlk altı aylık yazılım gelirinizi yazınız:"))
ifG=int(input("İlk altı aylık finansman gelirinizi yazınız:"))
iusG=int(input("İlk altı aylık ürün satış gelirinizi yazınız:"))
icmG=int(input("İlk altı aylık çalışan maaşları giderinizi yazınız:"))
ikG=int(input("İlk altı aylık kira giderinizi yazınız:"))
idmG=int(input("İlk altı aylık donanım maliyetinizi yazınız:"))
syG=int(input("Son altı aylık yazılım gelirinizi yazınız:"))
ssG=int(input("Son altı aylık sponsorluk gelirinizi yazınız:"))
setG=int(input("Son altı aylık e-ticaret gelirinizi yazınız:"))
susG=int(input("Son altı aylık ürün satış gelirinizi yazınız:"))
scmG=int(input("Son altı aylık çalışan maaşları giderinizi yazınız:"))
skG=int(input("Son altı aylık kira giderinizi yazınız:"))
sbmG=int(input("Son altı aylık bakım maliyetinizi yazınız:"))


def itgHesapla(iyG,ifG,iusG):
    global itopGelir
    itopGelir=iyG+ifG+iusG
    return itopGelir

def itopgiderHesapla(icmG,ikG,idmG):
    global itopGider
    itopGider=icmG+ikG+idmG
    return itopGider

def stopgelirHesapla(syG,ssG,setG,susG):
    global stopgelir
    stopgelir=syG+ssG+setG+susG
    return stopgelir

def stopgiderHesapla(scmG,skG,sbmG):
    global stopgider
    stopgider=scmG+skG+sbmG
    return stopgider

def iikHesapla(itopGelir,itopGider):
    global iikari
    iikari=itopGelir-itopGider
    print("İlk dönem karınız:",iikari)

def sonikar(stopgelir,stopgider):
    global sonikari
    sonikari=stopgelir-stopgider
    print("Son dönem karınız:",sonikari)

def farkAL(iikari,sonikari):
    fark=sonikari-iikari
    if(fark>5000):
        print("İşletmeniz çok karlı. Kar= ",fark)
    elif(fark>=1000) and (fark<=5000):
        print("İşletmenizin Karı Normal. Kar= ",fark)
    else:
        print("Üzgünüm İşletmeniz Yeterince Karda Değil")

itgHesapla(iyG,ifG,iusG)
itopgiderHesapla(icmG,ikG,idmG)
stopgelirHesapla(syG,ssG,setG,susG)
stopgiderHesapla(scmG,skG,sbmG)
iikHesapla(itopGelir,itopGider)
sonikar(stopgelir,stopgider)
farkAL(iikari,sonikari)

def adam_basiciroHesapla(x,y) :
    adambasiciro =(x*y)/25
    print("Adam Başı Cironuz =",adambasiciro)


x= float(input("Satış miktarını giriniz: "))
y = float(input("Birim satış fiyatını giriniz: "))
adam_basiciroHesapla(x,y)

# modülün çağırılması
import modul1

modul1.adam_basiciroHesapla(x,y)
modul1.itgHesapla(iyG,ifG,iusG)
modul1.itopgiderHesapla(icmG,ikG,idmG)
modul1.stopgelirHesapla(syG,ssG,setG,susG)
modul1.stopgiderHesapla(scmG,skG,sbmG)
modul1.iikHesapla(itopGelir,itopGider)
modul1.sonikar(stopgelir,stopgider)
modul1.farkAL(iikari,sonikari)