Flips = input()
FlipsArray = [*Flips]
MainArray = [1,2,3,4]
for flip in FlipsArray:
    value1 = MainArray[0]
    value2 = MainArray[1]
    value3 = MainArray[2]
    value4 = MainArray[3]
    if flip == "H":
        MainArray[0] = value3
        MainArray[1] = value4
        MainArray[2] = value1
        MainArray[3] = value2
    if flip == "V":
        MainArray[0] = value2
        MainArray[1] = value1
        MainArray[2] = value4
        MainArray[3] = value3
print(MainArray[0], MainArray[1])
print(MainArray[2], MainArray[3])
