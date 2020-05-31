

for i in range(100,0,-1):
    if i % 3 == 0 and i % 5 == 0:
        print("Testing")
    elif i % 5 == 0:
        print("Agile")
    elif i % 3 == 0:
        print("Software")
    else:
        print(str(i))