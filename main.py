import random
def numbers():
  listOfNumbers=[1,2,3,4,5,6,7,8,9,10]
  randomNumber=random.randint(0,9)
  item=listOfNumbers[randomNumber]

  i=0

  while(i<3): 
    guess=input("what is ur guess? ")
    guess=int(guess)
    if (guess>=1 and guess<=10):
      if item==int(guess):
        print("you are correct.")
        return
      else:
        print("you're wrong.") 
        diff=abs(int(guess)-item)
        if diff==5:
          print("your guess is warm.")
        elif diff<5:
          print ("your guess is hot.")
        else:
          print("Not even close >:(")
      i=i+1
    else:
      guess=input("Do another guess between 1 and 10: ")
      guess=int(guess)
  if i==3:
    print("Sorry, you're wrong, but here is the correct answer; "+ str(item))
     
numbers()