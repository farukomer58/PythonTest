CONVERSION = 0.45359237

weight = input("What is your weight in Pounds? ")
weightKilograms = float(weight) * CONVERSION

#weightType = type(weight)
#weightTypeKilograms = type(weightKilograms)
#print(weightType)
#print(weightTypeKilograms)

print("You weight in kilograms(kg) is: " + str(weightKilograms))