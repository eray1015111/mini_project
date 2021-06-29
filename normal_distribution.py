import random
import numpy as np                
import pandas as pd              
import matplotlib.pyplot as plt   
class player:
  def __init__(self,i):
    self.no=i
    self.num=0
    self.money=100
    self.play=1
  def plus(self):
    self.money+=1
  def minus(self):
    if self.money<=0:
      pass
    else:
      self.money-=1 

played=0  #已經超過一千次的人數

#判斷玩過1000次了沒
def judge(p):
  if p.num>=1000:
    data.append(p)
    p.play=0
  else:
    p.play=1
man=[]  #玩家
data=[] #數據
x=[]  #最後擁有0~100(萬)的人數陣列

#初始化人
for i in range(0,1000):
  man.append(player(i))
  #man[i]=player()

#猜拳
def game(a,b):
  judge(a)
  judge(b)
  if a.play==1 and b.play==1:
    r=random.randrange(2)
    if a.money>0 and b.money>0:
      if r==1:
        a.plus()
        b.minus()
        a.num+=1
        b.num+=1
      else:
        a.minus()
        b.plus()
        a.num+=1
        b.num+=1

#執行猜拳
while played<=100000:
  e1=random.randrange(0,1000)
  e2=random.randrange(0,1000)  
  e1=int(e1)
  e2=int(e2)
  game(man[e1],man[e2])
  if man[e1].num>=1000:
    played+=1
  if man[e2].num>=1000:
    played+=1
final =np.zeros((2,1000), dtype=np.int)
#row1是金錢 row2是人數
#資料歸類
for i in range(0,1000):
  for j in range(0,1000):
    if man[j].money==i:
      final[0][i]=i
      final[1][i]+=1


#畫圖
plt.bar(final[0],final[1],width=0.5, bottom=None, align='center',color=['blue'])
# 定義標籤
plt.ylabel("man")          # 設定y軸標題 
plt.xlabel("money")            # 設定x軸標題
plt.title("Bar chart of money", {'fontsize' : 27})  # 設定標題、文字大小

plt.ylim(0, 30)                 # 設定y軸範圍
plt.grid(True)                   # 顯示格線
plt.show()


# 儲存圖檔
plt.savefig("Bar chart of money.jpg",bbox_inches='tight',pad_inches=0.0)                     
plt.close()      # 關閉圖表
