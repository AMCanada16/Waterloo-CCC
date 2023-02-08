RowHight = input()
ColumnHight = input()
AmountOfFlips = input()
Flips = []
for flipvalue in range(int(AmountOfFlips)):
    FlipInput = input()
    Flips.append(FlipInput)
TotalSquares = int(RowHight) * int(ColumnHight)
Canvas = []
for Square in range(TotalSquares):
    Canvas.append(0)
for flip in Flips:
    flipArray = flip.split(" ")
    if flipArray[0] == "R":
        rowNumber = ((int(flipArray[1])) - 1)
        for column in range(int(RowHight)):
            NewColumn = int(column) * int(ColumnHight)
            if Canvas[NewColumn + rowNumber] == 0:
                Canvas[NewColumn + rowNumber] = 1
            elif Canvas[NewColumn + rowNumber] == 1:
                Canvas[NewColumn + rowNumber] = 0
    if flipArray[0] == "C":
        for row in range(int(RowHight)):
            rowidx = (int(flipArray[1])) * int(row) 
            if Canvas[rowidx] == 0:
                Canvas[rowidx] = 1
            elif Canvas[rowidx] == 1:
                Canvas[rowidx] = 0
GoldSpots = 0
for Spot in Canvas:
    if Spot == 0:
        continue
    if Spot == 1:
        GoldSpots += 1
print(GoldSpots)