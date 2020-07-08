number = input("Number: ")
numbersDictonarie = {
    "1" : "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

outputString = ""
for ch in number:
    outputString += numbersDictonarie.get(ch,"!") + " "

print(outputString)