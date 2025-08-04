import math
import numpy as np
import matplotlib.pyplot as plt
Aliquot = []
def getsum(n):
    if (n == 1):
        return 1
    result = 0
    for i in range(2, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            if (i == (n / i)):
                result = result + i
            else:
                result = result + (i + n // i)
    return (result+1)
N = 276
while N!=1:
 Aliquot.append(N)
 N = getsum(N)
print(Aliquot)
Aliquot = np.array(Aliquot)
plt.plot(Aliquot)
plt.title(f'Aliquot Sequence')
plt.xlabel('Term Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()