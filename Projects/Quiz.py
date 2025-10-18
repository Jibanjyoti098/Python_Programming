print("WLC to Quiz :)")

choice=input("Do you want to play? ")
if choice.lower() != "yes":
    quit()

print("OK! lets play:)")
score=0

ans=input("CPU stands for: ")
if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
ans=input("GPU stands for: ")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans=input("RAM stands for: ")
if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans=input("ROM stands for: ")
if ans.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans=input("Which one is an input device? \n1.Keyboard\n2.Mouse\n3.Joystick\n4.all the above\n")
if ans.lower() == "all the above":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got "+str(score)+" Score")