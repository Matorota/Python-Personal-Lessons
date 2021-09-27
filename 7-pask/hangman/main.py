import random
WORDS = ("tankas", "python", "bear", "lada", "apartment")
word = random.choice(WORDS)


print("The word is", len(word), "letters long.")
temp = len(word)
guessed = dict.fromkeys(word, 0) #https://www.w3schools.com/python/ref_dictionary_fromkeys.asp
print("_ "*temp)
correct = 0


for i in range(1, 9):
    letter = input("Guess the letter ")
    if letter in word:
        print ("Correct! {} is in the word".format(letter))
        guessed[letter] = 1
        correct += 1
        if correct == temp:
            print("Congratulations! you win.\n The word was {}".format(word))
            break
    else:
        print("Incorrect! {} is not in the word".format(letter))
    print(" ".join([x if guessed[x] else "_" for x in word]))
else:
    print("You lose!\nThe word was {}".format(word))
