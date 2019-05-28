x = '0101010'

for y in x:
    if int(y) == 0 or int(y) == 1:
        v = True
    else:
        v = False
        print("Not a binary number")
        break
if v:
    print("binary number")

