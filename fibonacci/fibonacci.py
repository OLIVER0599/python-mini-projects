from functools import lru_cache

import numpy as np
import matplotlib.pyplot as plt


@lru_cache(maxsize=None)

def r1_discrete(n):

    # initial condition
    if n < 1: return 0

    return 1/20 * (0.1 - r1_discrete(n-1)) + r1_discrete(n-1)

# Generate values
r1_values = [r1_discrete(i) for i in range(60)]

def r2_discrete(n):
    if n<1: return 0
    return 1/10 * (r1_discrete(n-1) - r2_discrete(n-1)) + r2_discrete(n-1)

r2_values = [r2_discrete(i) for i in range(len(r1_values))]

t_values = np.arange(60)


plt.plot(t_values, r1_values, label='R1', marker='o')
plt.plot(t_values, r2_values, label='R2', linestyle=':')

plt.xlabel('Time (s)')
plt.ylabel('Flow rate m^3/s')
plt.title('R1 vs R2')
plt.legend()
plt.grid(True)
plt.show()


         




