



def donenHesapla(kh,ach,bh,ash,tmh):
    global donenVarlik
    donenVarlik=kh+ach+bh+ash+tmh
    return donenVarlik

def duranHesapla(bih,th,dh):
    global duranVarlik
    duranVarlik=bih+th+dh
    return duranVarlik

def kvykHesapla(bkh,sh):
    global kvyk
    kvyk=bkh+sh
    return kvyk

def uvykHesapla(bkh,bsh):
    global uvyk
    uvyk=bkh+bsh
    return uvyk

def atoplam(donenVarlik,duranVarlik):
    global atoplam
    atoplam=donenVarlik+duranVarlik
    print("Aktif Toplamınız:",atoplam)

def ptoplam(kvyk,uvyk,ok):
    global ptoplam
    ptoplam=kvyk+uvyk+ok
    print("Pasif Toplamınız:",ptoplam)

def farkAL(atoplam,ptoplam):
    fark=ptoplam-atoplam
    if(fark==0):
        print("Kapanış bilançosu doğru hesaplanmıştır",fark)
    else:
        print("Bilanço yanlış hesaplanmıştır")

kh=int(input("Kasa hesabınızı yazınız:"))
ach=int(input("Alınan çekler hesabınızı yazınız:"))
bh=int(input("Bankalar hesabınızı yazınız:"))
ash=int(input("Alınan senetler hesabınızı yazınız:"))
tmh=int(input("Ticari mallar hesabınızı yazınız:"))
bih=int(input("Binalar hesabınızı yazınız:"))
th=int(input("Taşıtlar hesabınızı yazınız:"))
dh=int(input("Demirbaş hesabınızı yazınız:"))
bkh=int(input("Banka kredileri hesabınızı yazınız:"))
sh=int(input("Satıcılar hesabınızı yazınız:"))
bkh=int(input("Banka kredileri hesabınızı yazınız:"))
bsh=int(input("Borç senetleri hesabınızı yazınız:"))
sh=int(input("Sermaye hesabınızı yazınız:"))
ok=int(input("Öz sermayeyi yazınız:"))


donenHesapla(kh,ach,bh,ash,tmh)
duranHesapla(bih,th,dh)
kvykHesapla(bkh,sh)
uvykHesapla(bkh,bsh)
atoplam(donenVarlik,duranVarlik)
ptoplam(kvyk,uvyk,ok)
farkAL(atoplam,ptoplam)

#modülün çağırılması
import modul2

modul2.donenHesapla(kh,ach,bh,ash,tmh)
modul2.duranHesapla(bih,th,dh)
modul2.kvykHesapla(bkh,sh)
modul2.uvykHesapla(bkh,bsh)
modul2.atoplam(donenVarlik,duranVarlik)
modul2.ptoplam(kvyk,uvyk,ok)
modul2.farkAL(atoplam,ptoplam)