import numpy as np
from scipy.signal import convolve2d

with open("Event 2025/Day 4/data.txt") as f:
    Array = np.array([[c == '@' for c in row] for row in [line.strip() for line in f if line.strip()]], dtype=int)

accesibble = np.array([[c == True for c in row] for row in (Array == 1) & (convolve2d(Array,np.ones((3,3),dtype=int),'same') - Array < 4)],dtype=int)
AccesibbleRolls = 0

while accesibble.sum() != 0:
    AccesibbleRolls += accesibble.sum()
    Array = Array-accesibble
    accesibble = np.array([[c == True for c in row] for row in (Array == 1) & (convolve2d(Array,np.ones((3,3),dtype=int),'same') - Array < 4)],dtype=int)
print(AccesibbleRolls)