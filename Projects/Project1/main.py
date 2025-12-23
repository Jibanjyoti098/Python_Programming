import random

computer = random.choice([-1, 1, 0])
youstr = input("Enter your choice: ")
youDict = {"Snake":1, "Water":-1, "Gun":0}
reversedDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youstr]
print(f"You chose {reversedDict[you]}\nComputer choose {reversedDict[computer]}")

if(computer==you):
    print("It's a Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You lose!")

    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==-1 and you==0):
        print("You Win")

    elif(computer==0 and you==-1):
        print("You Win")
    elif(computer==0 and you==10):
        print("You lose!")
    else:
        print("Something went wrong")