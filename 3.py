c = input("nhap cau: ")
a = 0
b = 0
for i in c:
    if i.isdigit():
        a += 1
    elif i.isalpha():
        b += 1
    else:
        pass
print(" so chu cai la: ", a)
print(" so chu cai la: ", b)