message = input(">")
splittedMessage = message.split(" ")

emojis = {
    ":)" : "😂",
    ":(" : "😢"
}

finalMessage = ""
for word in splittedMessage:
    finalMessage += emojis.get(word,word) + " "

print(finalMessage)