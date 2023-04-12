num = int(input("Enter a number: "))
a, b = 0, 1
while b < num:
    print(b)
    a, b = b, a + b
