ID = str(931931931)
for ChunkSize in range(1,len(ID)//2+1): 
    Chunks = [ID[i:i+ChunkSize] for i in range(0, len(ID), ChunkSize)]
    if all(x == Chunks[0] for x in Chunks):
        print(ID)
        continue