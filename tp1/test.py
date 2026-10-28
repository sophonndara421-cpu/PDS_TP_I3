import pandas as pd
ages = pd.Series([21, 22, 20],
 index=["Sokha", "Dara", "Lina"])
print(ages)
print(ages["Dara"]) # by label
print(ages + 1) # vectorized: no loop
print(ages.mean(), ages.max(), ages.idxmax())