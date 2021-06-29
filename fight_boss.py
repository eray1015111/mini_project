import random

class player:
  def __init__(self,name):
    self.name=name
    self.hp=random.randrange(100,200,100)
    self.attack=random.randrange(80,100,100)
    self.life=1
  def cure(self):
    self.hp+=100
  def show(self):
    print("\n\t\t",self.name,"\t\tHP:",self.hp,"\t\tAttack",self.attack)
class boss:
  def __init__(self):
    self.hp=random.randrange(200,570,100)
    self.attack=random.randrange(50,150,100)
  def cure(self):
    self.hp+=100
  def show(self):
    print("\n\t\tBOSS","\t\tHP:",self.hp,"\t\tAttack",self.attack)

Boss=boss()
P1=player(input("\nplayer1 name:"))
P2=player(input("\nplayer2 name:"))
print("\n==========================\n")
print("Game Start!")  
print(P1.name,"&",P2.name,"fight with boss!") 
print("Can't lose!")  
print("Win condition: All players should survive.")
print("\n==========================\n")
con=1
move1=0
move2=0
curecho=0
while con:
  a=random.randint(1,2)
  P1.show()
  P2.show()
  Boss.show()
  if a==1:
    print("\nBOSS want to attack",P1.name,"what should I do?")
    P1.hp-=Boss.attack
    if P1.hp<=0:
      P1.life=0
  else:
    print("\nBOSS want to attack",P2.name,"what should I do?")
    P2.hp-=Boss.attack
    if P2.hp<=0:
      P2.life=0

  if P1.life==1:
    print(P1.name,":(1:attack 2:heal 100 hp)")
    move1=int(input())
    if move1==1:
      Boss.hp-=P1.attack
      if Boss.hp<=0:
        con=0
        print("win!")
    else:
      print("\ntarget:(1)",P1.name,"(2)",P2.name,"(3)Boss")
      curecho=input()
      if curecho==1:
          P1.cure()
      elif curecho==2:
          P2.cure()
      elif curecho==3:
          Boss.cure()
      else:
          print("\nERROR")
  else:
    pass

  if P2.life==1:
    print(P2.name,":(1:attack 2:heal 100 hp)")
    move2=int(input())
    if move2==1:
      Boss.hp-=P2.attack
      if Boss.hp<=0:
        con=0
        print("win!")
    else:
      print("\ntarget:(1)",P1.name,"(2)",P2.name,"(3)Boss")
      curecho=input()
      if curecho==1:
        P1.cure()
      elif curecho==2:
        P2.cure()
      else:
        Boss.cure()
  else:
    pass
    
  if P1.life==0 and P2.life==0:
    print("LOSE")
    break
  print("\n==========================\n")
