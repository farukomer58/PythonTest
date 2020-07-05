weight = float(input("Weight: "))
lbs_or_kgs = input("(L)bs or (K)gs ")

if lbs_or_kgs.upper() == "L":
    convertedWeight =  weight * 0.45359
    print(f"You weight {convertedWeight} Kilograms")
elif lbs_or_kgs.upper() == "K":
    convertedWeight = weight /  0.45359
    print(f"You weight {convertedWeight} Pounds")
else:
    print("Type either L or K")

