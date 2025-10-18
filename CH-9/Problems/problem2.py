import random

def game():
    print("You areplaing the game")
    score = random.randint(1, 60)
    with open("CH-9/Problems/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore==""):
            hiscore = 0
        else:
            hiscore = int(hiscore)
    print(f"Your  score is {score}")
    if(score>hiscore):
        with open("CH-9/Problems/hiscore.txt", "w") as f:
            f.write(str(score))

game()