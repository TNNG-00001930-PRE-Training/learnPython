def print_even_length_words(input_string):
    words = input_string.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)


input_string = "This is a sample string with words of varying lengths"
print_even_length_words(input_string)
