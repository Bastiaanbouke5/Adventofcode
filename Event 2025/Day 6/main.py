import math

with open("Event 2025/Day 6/data.txt","r") as f:
    GridWrong=[]
    while Line := f.readline():
        if Line.split()[0] in ['*','+']:
            Row = Line.split()
        else: Row = list(map(int, Line.split()))
        GridWrong.append(Row)
    Grid = list(map(list, zip(*GridWrong)))
    print(Grid)

# total = 0
# for i in Grid:
#     if i[-1] == '*':
#         total += math.prod(i[:-1])
#     elif i[-1] == '+':
#         total += sum(i[:-1])

# print(total)