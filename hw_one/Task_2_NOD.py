a = input('enter first number ')
b = input('enter second number ')
 
while a <> b:
    if a > b:
        a = a - b
    else:
        b = b - a
 
print (a)