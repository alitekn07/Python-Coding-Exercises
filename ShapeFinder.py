
shape = input("Which shape do you want to know ? : ")

if (shape == "quadrilateral"):

    print("Please enter the edges in order.")

    a = int(input("First Edge: "))
    b = int(input("Second Edge: "))
    c = int(input("Third Edge: "))
    d = int(input("Fourth Edge: "))

    if (a == b and a == c and a == d):
        print("Square")

    elif (a == c and b == d):
        print("Rectangle")
    else:
        print("Quadrilateral")


elif (shape == "triangle"):

    a = int(input("First Edge: "))
    b = int(input("Second Edge: "))
    c = int(input("Third Edge: "))

    if (abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):

        if (a == b and a == c):
            print("equilateral triangle")

        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Isosceles Triangle")

        else:
            print("Scalene Triangle")
    else:
        print("Doesn't indicate triangle")
else:
    print("Geçersiz Şekil")