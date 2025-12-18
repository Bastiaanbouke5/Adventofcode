import math
from itertools import zip_longest 

def part1():
    with open("Event 2025/Day 6/data.txt","r") as f:
        GridWrong=[]
        while Line := f.readline():
            if Line.split()[0] in ['*','+']:
                Row = Line.split()
            else: Row = list(map(int, Line.split()))
            GridWrong.append(Row)
        Grid = list(map(list, zip(*GridWrong)))
        # print(Grid)

    total = 0
    for i in Grid:
        if i[-1] == '*':
            total += math.prod(i[:-1])
        elif i[-1] == '+':
            total += sum(i[:-1])
    return total

def part_2_example(Width):
    with open("Event 2025/Day 6/data example.txt") as f:
        Grid = [[line[i:i+Width] for i in range(0, len(line), Width+1)]for line in f]

    total = 0
    for index,Operator in enumerate(Grid[len(Grid)-1]):
        Operator = Operator[0]
        NumbersRevs = [str(n).zfill(Width)[::-1] for n in [Number[index] for Number in Grid[:-1]]]
        Cephalopod = ['']*Width
        for i in NumbersRevs:
            for digit in zip([0,1,2],[*i]):
                if digit[1] == ' ':
                    continue
                Cephalopod[digit[0]] += digit[1]
        Cephalopod = list(map(int, Cephalopod))
        total += solver(Cephalopod,Operator)
    return total

def solver(Input,Operator):
    if Operator == '*':
        return math.prod(Input)
    else: 
        return sum(Input)

def part_2():
    # read lines
    with open("Event 2025/Day 6/data.txt") as f:
        Lines = [Line.rstrip("\n") for Line in f]

    LENGTH = max(len(Line) for Line in Lines)
    Lines = [Line.ljust(LENGTH) for Line in Lines]

    Grid = [[] for _ in Lines]
    Index = 0
    while Index < LENGTH:
        SliceCol = [Line[Index] for Line in Lines]
        if all(Char == ' ' for Char in SliceCol):
            Index += 1
            continue
        Width = 1
        while Index + Width < LENGTH and not all(Line[Index + Width] == ' ' for Line in Lines):
            Width += 1
        for RowIndex, Line in enumerate(Lines):
            Cell = Line[Index:Index + Width]
            Grid[RowIndex].append(Cell)
        Index += Width

    #solver parser
    total = []
    for index,Operator in enumerate(Grid[len(Grid)-1]):
        Operator = Operator[0]
        NumbersRevs = [str(n)[::-1] for n in [Number[index] for Number in Grid[:-1]]]
        Width = len(max(NumbersRevs, key=len))
        Cephalopod = ['']*Width
        for i in NumbersRevs:
            for digit in zip(range(Width),[*i]):
                if digit[1] == ' ':
                    continue
                Cephalopod[digit[0]] += digit[1]
        Cephalopod = [int(x) for x in Cephalopod if x.strip() != '']
        Cephalopod = list(map(int, Cephalopod))
        total.append(solver(Cephalopod,Operator))
    total = sum(total)
    return total

print(part_2())

