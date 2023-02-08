NumberOfFriends = input()
FriendsInput = []
#Position, Speed, Hearing range
for value in range(int(NumberOfFriends)):
    Input = input()
    FriendsInput.append(Input)
#Calculating for C
def Time(Pos):
    TotalTime = 0
    for friend in FriendsInput:
        FriendArray = friend.split(" ")
        if int(FriendArray[0]) == Pos:
            continue
        if int(FriendArray[0]) <= Pos:
            NewPos = Pos - int(FriendArray[2])
            if int(FriendArray[0]) >= NewPos:
                continue
            Distance = NewPos - int(FriendArray[0])
            Time = Distance * int(FriendArray[1])
            TotalTime = TotalTime + Time
        if int(FriendArray[0]) >= Pos:
            NewPos = Pos + int(FriendArray[2])
            if int(FriendArray[0]) <= NewPos:
                continue
            Distance = int(FriendArray[0]) - NewPos
            Time = Distance * int(FriendArray[1])
            TotalTime = TotalTime + Time
    return TotalTime

Positions = []
for friend1 in FriendsInput:
    friend1Array = friend1.split(" ")
    Positions.append(int(friend1Array[0]))
Positions.sort()

start = Time(Pos=int(0)) + 1
for value in range(Positions[-1]):
    result = Time(Pos=int(value))
    if result >= start:
        break
    if result <= start:
        start = result

print(f"Result: {start}")