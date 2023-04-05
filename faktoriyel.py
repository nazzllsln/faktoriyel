def faktoriyel(N):
    if N==1:
        return 1
    else:
        return N*faktoriyel(N-1)

sayi = int(input("sayı giriniz."))
sonuc = faktoriyel(sayi)
print(sonuc)

