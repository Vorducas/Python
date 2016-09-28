#Alex Hadfield, B day, Block 4
#9/23/16
#Pig Latin Translator

vowels = "AEIOU"
realLetters = "abcdefghijklmnopqrstuvwxyz"


while True:
    isRealWord = True
    word = raw_input("Please tell me a word to translate: ")
    for letter in range(len(word)):
        if word[letter] in realLetters:
            continue
        else:
            print "Error: Word contained invalid characters"
            isRealWord = False

    if isRealWord == True:        
        firstLetter = word[0]
        if firstLetter.upper() not in vowels:
            theRestOfTheWord = word[1:]
            pigWord = theRestOfTheWord + firstLetter + "ay"
            print pigWord.lower()
        else:
            print word + "ay"

