import numpy as np
import matplotlib.pyplot as plt
#畫i(t)圖
C=10e-4
L=10
Q=50
x=L*C
w=np.sqrt(x)
da=[]
db=[]

dt=np.linspace(0,5,200)
def current():
  for t in dt:
    i=(Q/w)*np.sin(t/w)
    da.append(i)
def charge():
  for t in dt:
    q=Q*np.cos(t/w)
    db.append(q)
current()
charge()

plt.plot(dt1,da,color="Red",label="I(t)")
plt.ylim([-550,550])
plt.xlabel("time(sec)")
plt.ylabel("Amplitude(V)")
plt.legend(loc="best")
plt.title("LC Circuit")
plt.show()

plt.plot(dt1,db,color="Blue",label="Q(t)")
plt.ylim([-55,55])
plt.xlabel("time(sec)")
plt.ylabel("Amplitude(C)")
plt.legend(loc="best")
plt.title("LC Circuit")
plt.show()
