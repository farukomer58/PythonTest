while True:
    numberA = float(input("Number A: "))
    numberCalcMethod = input("Do you want to * - + or / : ")
    numberB = float(input("Number B: "))
    result = 0
    if len(numberCalcMethod) > 0:
        if numberCalcMethod == "*"  or numberCalcMethod == "/":
            result = numberA * numberB
        elif numberCalcMethod == "-":
            result = numberA - numberB
        elif numberCalcMethod == "+":
            result = numberA + numberB
        elif numberCalcMethod == "/":
            result = numberA / numberB

    else:
        print("ERROR: You should specify what you want to do With the Numbers")
        break
    print(f"The result is: {result}")
