def Pow(x, y):
    p = 1;
    for i in range(y+1):
        p *= x
    return p
x = int(input("x="))
y = int(input("y="))
print('%d' % Pow(x, y))
