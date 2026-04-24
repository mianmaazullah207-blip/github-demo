import random
random.randint(1,100)
y=random.randint(1,100)
guess=int(input("start guessing:"))
while guess!=y:
    if guess<y:
        print("guess higher:")
    else:
        print("guess lower.")

    guess=int(input("start guess."))

    print("correct guess")    