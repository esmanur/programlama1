sayi=' '
kalan=0
while(sayi!=0):
    sayi = int(input("Bir sayi girin: "))
    if sayi == 0: break
    kalan += (sayi%3)


print ("0 girene kadar girdiğim sayıların 3'e bölümünden kalanların toplamı=",kalan)