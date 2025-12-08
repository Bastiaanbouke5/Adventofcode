with open("Event 2025/Day 3/data.txt") as f:
    Banks = [line.strip() for line in f if line.strip()]

def part1():
    joltage = 0
    for Bank in Banks:
        tempJolt = ""
        for i in range(11,0,-1):
            tempJolt += (max(Bank[:-i]))
            Bank = Bank[Bank.index(max(Bank[:-i]))+1:]
        tempJolt += (max(Bank))
        joltage += int(tempJolt)
        print(joltage)
    return joltage
        

print(part1())