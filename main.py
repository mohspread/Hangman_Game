import os, random


filehandle = open("wordsdb.txt","r")
get_text = filehandle.read()
get_text_array = get_text.split("\n")
randomline = random.randrange(int(len(get_text_array)))

readytext = get_text_array[randomline]

print(" _ " * int(len(get_text_array[randomline])))
x = 0
trueguess = []
while x < len(readytext) and int(len(readytext)) != int(len(trueguess)):
    guessed_letter = input("\n" + "Enter Letter!")
    for i in range(int(len(readytext))):
        if readytext[i] == guessed_letter:
            print(guessed_letter,end="")
            trueguess.append(i)
        else:
            if i in trueguess:
                print(readytext[i],end="")
            else:
                print(" _ ",end="")
    x = x + 1

if len(trueguess) < len(readytext):
    print("\nFailed")
else:
    print("\nYou did it !!!")

filehandle.close()
