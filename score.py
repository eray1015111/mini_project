import numpy as np
import pandas as pd
data=pd.DataFrame({
    "name":[],
    "score":[],
    "check":[]
})
i=0
p=1
flunk=0
print(data)
while True:
  name=input("Enter names:")
  if name=='quit':
    break
  s=input("Score:")
  name=str(name)
  s=int(s)
  if s<60:
    p=0
    flunk+=1
  else:
    p=1
  p=int(p)
  data.loc[i]=[name,s,p]
  i+=1
print(data)
n=0
i=i//2
if flunk>i:
  for n in range(0,i+1):
    data.at[n,'score']=np.sqrt(data.at[n,'score'])
    data.at[n,'score']=data.at[n,'score']*10
    n+=1
print(data.sort_values(by=["name"],ascending=False))
print(data)
