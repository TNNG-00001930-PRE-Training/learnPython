def sortWord():
    input_word = input("Enter the word : ")
    s = sorted(input_word.split(','))
    print(*s, sep=',')

sortWord()    