import random
score = 0

print("Enter Run")
comp =random.randint(0,6)

choice = int(input())
score = score +choice
while choice != comp:
    print("Enter Run")
    comp =random.randint(0,6)
    
    choice = int(input())
    score = score +choice
if choice == comp:
    print("Game over. Your Score is:"+str(score))
    score = score - choice
    
    


