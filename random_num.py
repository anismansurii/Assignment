import random
random_num = random.randint(1,3)
while True:
    num = int(input("Enter a Guess "))
    if random_num==num:
        print("You win")
        break
     