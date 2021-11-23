print('Enter your word:')
message = input()
print("Message : " + message)
def caesar(text):
    array1 = []
    array2 = []

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for eachLetter in text:
        if eachLetter in letters:
            index = letters.index(eachLetter)
            crypting = (index + 23) % 26
            array2.append(crypting)
            newLetter = letters[crypting]
            array1.append(newLetter)
    return array1

code = caesar(message)
print(code)
