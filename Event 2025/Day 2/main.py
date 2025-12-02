with open("Event 2025/Day 2/data.txt") as f:
    Ranges = [Range.split("-") for Range in f.read().split(",")]


Answer = 0
for Range in Ranges:
    for ID in range(int(Range[0]),int(Range[1])+1):
        ID = str(ID)
        # if ID == len(ID) * ID[0]: #catch fully repeating IDs
        #     print(ID)
        #     continue
        # elif len(ID)%2 == 0:
        #     strLen=len(ID)
        #     IDstr1,IDstr2 = ID[:strLen//2],ID[strLen//2:]
        #     if IDstr1 == IDstr2:
        #         print(ID)
        #         continue
        # if ID[0:int(len(ID)/6*2)-1] == ID[(int(len(ID)/6*2)*-1):]:
        #     print(ID)
        #     continue
        for ChunkSize in range(1,len(ID)//2+1): #i refers to an increasing amount of characters from the ID
            Chunks = [ID[i:i+ChunkSize] for i in range(0, len(ID), ChunkSize)]
            if all(x == Chunks[0] for x in Chunks):
                Answer += int(ID)
                # print(ID)
                break

print(Answer)