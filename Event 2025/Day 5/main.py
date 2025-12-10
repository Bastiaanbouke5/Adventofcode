FreshIngredientRanges = []
AvailableIngredients = []

with open("Event 2025/Day 5/data.txt") as f:
    for line in f:
        if not line.strip(): break
        FreshIngredientRanges.append([int(line.split("-")[0]),int(line.split("-")[1])])
    for line in f:
        AvailableIngredients.append(int(line))

def part1():
    FreshIngredients = 0
    for Ingredient in AvailableIngredients:
        for FreshRange in FreshIngredientRanges:
            if Ingredient in range(FreshRange[0],FreshRange[1]+1):
                # print("Ingredient: ",Ingredient," is fresh")
                FreshIngredients += 1
                break
    return FreshIngredients

def part2Slow(): #An extremely slow method but it works after a gallion years I guess.. 
    FreshIDs = []
    FreshIDAmount = 0
    for FreshRange in FreshIngredientRanges:
        for ID in range(FreshRange[0],FreshRange[1]+1):
            if ID not in FreshIDs:
                FreshIDs.append(ID)
                FreshIDAmount += 1
    return FreshIDAmount

def part2():
    FreshIngredientRanges.sort()
    NewRanges = [FreshIngredientRanges[0]]
    Itterator = 0
    for Range in FreshIngredientRanges:
        if Range[0] <= NewRanges[Itterator][1] + 1 and Range[1] > NewRanges[Itterator][1]:
            NewRanges[Itterator][1] = Range[1]
        elif Range[1] <= NewRanges[Itterator][1] and Range[0] >= NewRanges[Itterator][0]: continue
        else:
            NewRanges.append(Range)
            Itterator += 1
    IDAmount = 0
    for Range in NewRanges:
        IDAmount += (Range[1]-Range[0]+1)
    return IDAmount

# print(part1())
print(part2())