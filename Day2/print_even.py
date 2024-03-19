def print_even_length_words(input_string):
    words = input_string.split()
    for i in words:
        if len(i) % 2 == 0:
            print(i)


input_string = "Python is a programming language"
print_even_length_words(input_string)