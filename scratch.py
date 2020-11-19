import pandas as pd 

# data = [1,2,3,4,5]

# data = [['Alex',10], ['Bob',12], ['Clarke',13]]

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])


print(df)