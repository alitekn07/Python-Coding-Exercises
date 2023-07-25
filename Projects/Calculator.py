

print("Hesap Makinesi V1\n")

print("İşlem Sırası:\n1) Toplama\n2) Çıkarma\n3) Çarpma\n4) Bölme\n")


a = int(input("1. Sayı: "))
b = int(input("2. Sayı: "))

islem = input("İşlem Numarasını Giriniz: ")

if (islem == "1"):

    print("{} ile {} sayısının toplamı: {}".format(a,b,a+b))

elif (islem == "2"):

    print("{} ile {} sayısının çıkarma sonucu: {}".format(a,b,a-b))

elif (islem == "3"):

    print("{} ile {} sayısının çarpımı: {}".format(a,b,a*b))

elif (islem == "4"):

    print("{} ile {} sayısının bölümü: {}".format(a,b,a/b))

else:

    print("Lütfen işlem sırasını doğru seçiniz!")