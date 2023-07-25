

islem = int(input("Hangi İşlemi Yapmak İstiyorsunuz?\n1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme\nSeçim Yapınız: "))

if islem == 1:
    print("Toplama işlemi için 2 sayı yazın")

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    toplama = n1 + n2

    print("Toplama işleminin sonucu: ",format(toplama))

elif islem == 2:
    print("Çıkarma işlemi için 2 sayı yazın")

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    cıkarma = n1 - n2

    print("Çıkarma işleminin sonucu: ",format(cıkarma))

elif islem == 3:
    print("Çaprma işlemi için 2 sayı yazın")

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    carpma = n1 * n2

    print("Çarpma işleminin sonucu: ",format(carpma))

elif islem == 4:
    print("Bölme işlemi için 2 sayı yazın")

    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    bölme = n1 / n2

    print("Bölme işleminin sonucu: ",format(bölme))

else:

    print("Lütfen geçerli bir sayı giriniz!")