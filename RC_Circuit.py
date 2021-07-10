import numpy as np
import matplotlib.pyplot as plt

R=10000
C=900e-7
da=[]
db=[]
da1=[]
db1=[]

dt1=np.linspace(-1,5,200)
dt2=np.linspace(0,5,200)
dt3=np.linspace(-1,5,400)
def charge():
  for t in dt1:
    if t<0:
      V1=0
    else:
      V1=10
    V2=V1*(1-np.exp(-t/(R*C)))
    da.append(V1)
    db.append(V2)

def discharge():
  V3=10
  for t in dt2:
    V4=V3*(np.exp(-t/(R*C)))
    da.append(V3)
    db.append(V4)

charge()
discharge()
plt.plot(dt3,da,color="Red",label="V1")
plt.plot(dt3,db,color="Blue",label="V2")
plt.ylim([-1,11])
plt.xlabel("time(sec)")
plt.ylabel("Amplitude(V)")
plt.legend(loc="best")
plt.title("RC Circuit")
plt.show()
