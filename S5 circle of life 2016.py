LengthRounds = input()
LenthroundsArray = LengthRounds.split(" ")
Circle = input()
CircleArray = [*Circle]
NewCircleArray = []

def Cirlce(Left, Right):
    if  Left == "1" and  Right == "1":
        NewCircleArray.insert(idx,"0")
        return
    if Left == "0" and Right == "1":
        NewCircleArray.insert(idx,"1")
        return
    if Left == "1" and Right == "0":
        NewCircleArray.insert(idx,"1")
        return
    if Left == "0" and Right == "0":
        NewCircleArray.insert(idx,"0")
        return
for value in range(int(LenthroundsArray[1])):
    NewCircleArray = []
    for idx, value in enumerate(CircleArray):
        newidx = idx + 1
        if newidx >= len(CircleArray):
            newidx = 0
        Left = CircleArray[int(idx - 1)]
        Right = CircleArray[int(newidx)]
        Cirlce(Left=Left, Right=Right)
    CircleArray = NewCircleArray
print("".join(CircleArray))