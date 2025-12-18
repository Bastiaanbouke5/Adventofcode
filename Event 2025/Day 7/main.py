with open("Event 2025/Day 7/data example.xt","r") as f:
    Manifold = [list(line.rstrip("\n")) for line in f]

Count = [0] * len(Manifold[0])
Count[Manifold[0].index("S")] = 1
Start = Manifold[0].index("S")
SplitCount = 0
for RowIndex,Row in enumerate(Manifold):
    if RowIndex == 0:
        Manifold[1][Start] = "|"
    else:
        for BeamIndex,Beam in enumerate(Manifold[RowIndex]):
            if Beam == "." and Manifold[RowIndex-1][BeamIndex] == "|":
                Manifold[RowIndex][BeamIndex] = "|"
            elif Beam == "^" and Manifold[RowIndex-1][BeamIndex] == "|":
                Manifold[RowIndex][BeamIndex+1] = "|"
                Manifold[RowIndex][BeamIndex-1] = "|"
                Count[BeamIndex-1] += Count[BeamIndex]
                Count[BeamIndex+1] += Count[BeamIndex]
                Count[BeamIndex] = 0
                SplitCount += 1
    print(Count)

TotalCount = sum(Count)
# for RowCheck in Manifold:
#     print(RowCheck)
print(SplitCount,TotalCount-2)