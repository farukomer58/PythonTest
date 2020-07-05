secretNumber =9
attemps = 0

while attemps < 3:
    guess = int(input("Guess: "))
    attemps += 1
    if guess == secretNumber:
        print("Good Job you got it")
        break
else:
    print("Sorry, you failled")