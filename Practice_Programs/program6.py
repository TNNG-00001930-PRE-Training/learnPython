def remove_duplicate():
    input_word = input("Enter a sequence of whitespace-separated words: ")
    words_list = input_word.split()
    unique_word = sorted(set(words_list))
    print(*unique_word)

remove_duplicate()