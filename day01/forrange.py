# range(0,10,1) 补偿

for a in range(10):
    print("loop:", a)

for b in range(0, 10, 2):
    print("loop1:", b)

for i in range(10):
    print("-------------", i)
    for j in range(10):
        print(j)
        if j > 5:
            break

for x in range(0, 10):
    if x < 3:
        print("lookx:", x)
    else:
        continue
    print("hehe")
