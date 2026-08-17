"""import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data=d)

print(df)

count_column = df.shape[1]
print('the column number is ' )
print(count_column)

print('the row number is ' )
count_row = df.shape[0]
print(count_row)
"""

import pandas as pd

d={'col1': [1,2,3,4,5,6,7,8,9,0],
    'col2':[3,4,5,6,7,8,9,0,1,2],
    'col3':[3,4,5,6,7,8,9,0,1,2],
    'col4':[3,4,5,6,7,8,9,0,1,2],
    'col5':[3,4,5,6,7,8,9,0,1,2],
    'col5':[3,4,5,6,7,8,9,0,1,2]
     }
df=pd.DataFrame(data=d)
print(df)

print("The row number is ", df.shape[1])
print("The row number is ", df.shape[0])
