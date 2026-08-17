import numpy as np

Max_Pulse= full_health_data["Max_Pulse"]
percentile10 = np.percentile(Max_Pulse, 10)
print(percentile10)
"""
Max_Pulse = full_health_data["Max_Pulse"] - Isolate the variable Max_Pulse from the full health data set.
np.percentile() is used to define that we want the 10% percentile from Max_Pulse.
The 10% percentile of Max_Pulse is 120. This means that 10% of all the training sessions have a Max_Pulse of 120 or lower.
"""