import numpy as np

std = np.std(full_health_data)
print(std)
"""
Co eff of variance
"""
import numpy as np

cv = np.std(full_health_data) / np.mean(full_health_data)
print(cv)

"""
The coefficient of variation is used to get an idea of how large the standard deviation is.

Mathematically, the coefficient of variation is defined as:

Coefficient of Variation = Standard Deviation / Mean
 We can do this in Python if we proceed with the following code:
 """