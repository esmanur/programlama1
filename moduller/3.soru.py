def beHesapla(x, y, z, m, n):
    be = ((x + y + z) / m / n) * 100
    print("YBS-1 grubunun etkileşim oranı=", be)
    if (be > 0.20):
        print("YBS-1 grubunun etkileşim oranı başarılı!!")
    else:
        print("YBS-1 grubunun etkileşim oranı başarısız!!")


def ieHesapla(k, a, b, c, d):
    ie = ((k + a + b) / c / d) * 100
    print("YBS-2 grubunun etkileşim oranı=", ie)
    if (ie > 0.20):
        print("YBS-2 grubunun etkileşim oranı başarılı!!")
    else:
        print("YBS-2 grubunun etkileşim oranı başarısız!!")


def ueHesapla(e, f, g, h, l):
    ue = ((e + f + g) / h / l) * 100
    print("YBS-3 grubunun etkileşim oranı =", ue)
    if (ue > 0.20):
        print("YBS-3 grubunun etkileşim oranı başarılı!!")
    else:
        print("YBS-3 grubunun etkileşim oranı başarısız!!")


x = float(input("YBS-1 grubunun beğeni sayısını giriniz: "))
y = float(input("YBS-1 grubunun yorum sayısını giriniz: "))
z = float(input("YBS-1 grubunun paylaşım sayısını giriniz: "))
m = float(input("YBS-1 grubunun içerik sayısını giriniz: "))
n = float(input("YBS-1 grubunun takipçi sayısını giriniz: "))
k = float(input("YBS-2 grubunun beğeni sayısını giriniz: "))
a = float(input("YBS-2 grubunun yorum sayısını giriniz: "))
b = float(input("YBS-2 grubunun paylaşım sayısını giriniz: "))
c = float(input("YBS-2 grubunun içerik sayısını giriniz: "))
d = float(input("YBS-2 grubunun takipçi sayısını giriniz: "))
e = float(input("YBS-3 grubunun beğeni sayısını giriniz: "))
f = float(input("YBS-3 grubunun yorum sayısını giriniz: "))
g = float(input("YBS-3 grubunun paylaşım sayısını giriniz: "))
h = float(input("YBS-3 grubunun içerik sayısını giriniz: "))
l = float(input("YBS-3 grubunun takipçi sayısını giriniz: "))

beHesapla(x, y, z, m, n)
ieHesapla(k, a, b, c, d)
ueHesapla(e, f, g, h, l)