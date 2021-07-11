
import numpy as np
import matplotlib.pyplot as plt
C=10e-5
R=8
L=1
Q=50
V=5
x=L*C
wn=1/(np.sqrt(x))
y=wn**2-(R/2*L)**2
wd=np.sqrt(y)
da=[]
db=[]
print(wn)
print('the 2L*Wn',2*L*wn)
print('Wd.real',wd.real)
print('Wd.imag',wd.imag)
print('特徵值虛部',y)
dt=np.linspace(0,0.5,200)
def charge():
  for t in dt:
    q=Q*np.exp((-R*t)/(2*L))*np.sin((wd)*t)
    da.append(q)

charge()

plt.plot(dt,da,color="Red",label="Q(t)")
plt.ylim([-50,50])
plt.xlabel("time(sec)")
plt.ylabel("Amplitude")
plt.legend(loc="best")
plt.title("RLC Circuit")
plt.show()
