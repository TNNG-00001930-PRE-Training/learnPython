def count_upper_lower(sentence):
    upper_count = sum(1 for char in sentence if char.isupper())
    lower_count = sum(1 for char in sentence if char.islower())
    print("UPPER CASE", upper_count)
    print("LOWER CASE", lower_count)


input= input("Enter a sentence: ")
count_upper_lower(input)