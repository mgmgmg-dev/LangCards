from os import listdir, path
from random import randint

files = [f for f in listdir('./languages/') if path.isfile("./languages/" + f) and f.endswith(".lang")]

userInput = ""
while True:
    print("\n" * 100)
    print("Please select one of the following options.")
    for i in range(len(files)):
        print(str(i+1) + ") " + files[i][:-5].replace("_", " "))
    userInput = input("\n-> ")
    try:
        userInput = int(userInput)
        if userInput < 1 or userInput > len(files):
            raise Exception()
        break
    except:
        pass

words = {}

with open("./languages/" + files[userInput-1], "r") as file:
    del userInput

    blocks = []
    startIndex = 0
    contents = file.readlines()
    for i in range(len(contents)):
        if contents[i] == ("!SOF!\n"):
            startIndex = i+1
            break
    
    counter = 0
    for i in range(startIndex, len(contents)):
        blocks = contents[i].split("::")
        if(len(blocks) != 2): break
        words[blocks[0]] = blocks[1][:-1]

        counter += 1
        print("\r" + str(counter) + " words loaded.", end="")
    
    del blocks
    del contents
    del startIndex

del files
wordCount = len(words)-1

print(("\n"*100) + str(wordCount+1) + " words added.")
input("\nPress enter to start learning")

while True:
    print("\n"*50)
    word = list(words.keys())[randint(0, wordCount)]
    input(word)
    input(words[word])