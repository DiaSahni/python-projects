import random
import time
print ("Welcome to a game of cards. You are competing with a computer to see who has the higher deck.")
MyPoints=0
CompPoints=0
Deck=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
time.sleep(1)
MyDeck=[]
CompDeck=[]
money=(50)
for x in range(5):
  card=random.choice(Deck)
  MyDeck.append(card)
  #this picks a card and saves it#
print ("here is your deck:")
print (MyDeck)
choice=input("Do you want to keep or exchange your cards?")
if choice=="exchange":
  exchange=input("Which cards do you want to exchange? Say done when finished.")
  while exchange!=("done"):
    MyDeck.remove(exchange)
    card=random.choice(Deck)
    MyDeck.append(card)
    exchange=input("Which cards do you want to exchange? Say done when finished.")
  time.sleep(1)
  #this exchanges cards#
  print (MyDeck)
print ("You have",money,"dollars.")
betting=input("How much do you want to bet?")
for i in MyDeck:
  if i=="A":
    MyPoints+=1
  elif i=="J":
    MyPoints+=11
  elif i=="Q":
    MyPoints+=12
  elif i=="K":
    MyPoints+=13
  else:
    MyPoints+=int(i)

#this calculates your points#

for x in range(5):
  card=random.choice(Deck)
  CompDeck.append(card)
print ("This is the computer's deck.")
print (CompDeck)
for i in CompDeck:
  if i=="A":
    CompPoints+=1
  elif i=="J":
    CompPoints+=11
  elif i=="Q":
   CompPoints+=12
  elif i=="K":
    CompPoints+=13
  else:
    CompPoints+=int(i)
    

#this calculates the computer's points#
computerTotal=(CompPoints)
playerTotal=(MyPoints)
print ("calculating...")
time.sleep(4)
if playerTotal>computerTotal:
  print (f"You win. Crongats. The comp has this many points: {CompPoints}, and u had this many points: {MyPoints}")
  money+=int(betting)
  print ("This is how much you have left:", money)
elif playerTotal<computerTotal:
  print ("You lose.")
  money-=int(betting)
  print (f"You lose. Tyr again. The comp has this many points: {CompPoints}, and u had this many points: {MyPoints}")
  print ("this is how much you have left:",money)
else:
  print ("You tied.")
  print (f"You tied. You didn't gain nor lose. You both tied with: {CompPoints}, and {MyPoints}")