import numpy as np


matrix = np.random.random((3, 3, 3))

c = z = 0
mid = []

while z <= len(matrix[-1])-1:
    mid.append(matrix[z, c, c])
    c += 1
    if c >= 3:
        c = 0
        z += 1

print(sum(mid)/len(mid))