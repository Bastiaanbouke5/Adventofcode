with open("Adventofcode/data.txt") as f:
    Sequence = [line.strip() for line in f if line.strip()]

def get_code_part1():
    Start = 50
    Code=0
    Line=1
    for Rotation in Sequence:
        RotationAmount = int(Rotation[1:])
        if "R" in Rotation:
            Start += RotationAmount
        else:
            Start -= RotationAmount
        Start %= 100
        if Start == 0:
            Code += 1
        Line += 1
    return Code

def get_code_part2():
    Dial = 50
    Code=0
    for Rotation in Sequence:
        RotationAmount = int(Rotation[1:])
        if Rotation[0] == "R":
            while RotationAmount > 0:
                Dial = (Dial+1)%100
                if Dial == 0:
                    Code += 1
                RotationAmount -= 1
        else:
            while RotationAmount > 0:
                Dial = (Dial-1)%100
                if Dial == 0:
                    Code += 1
                RotationAmount -= 1
    return Code

print(f"The code of part 1 is '{get_code_part1()}'")
print(f"The code of part 2 is '{get_code_part2()}'")
