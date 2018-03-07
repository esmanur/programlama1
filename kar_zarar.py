#x,y,z gelirler

x=int(input('İşletmenin finansman gelirini giriniz:'))
y=int(input('İşletmenin pazar gelirini giriniz:'))
z=int(input('İşletmenin kira gelirini giriniz:'))

#a,b,c,d,e giderler

a=int(input('İşletmenin ücretini giriniz:'))
b=int(input('İşletmenin finansman giderini giriniz:'))
c=int(input('İşletmenin pazar giderini giriniz:'))
d=int(input('İşletmenin kira giderini giriniz:'))
e=int(input('İşletmenin muhasebe giderini giriniz:'))

kar=((x+y+z)-(a+b+c+d+e))
print(kar)

if kar>1000:
    print ('İşletmeniz kar etmektedir.')

else:
    print('İşletmeniz zarar etmektedir.')

