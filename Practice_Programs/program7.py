def find_even_digit():
    even_digit_number = []
    for i in range(1000, 3001):
        d = [int(digit) for digit in str(i)]
        if all(digit % 2 == 0 for digit in d):
            even_digit_number.append(str(i))
    print(','.join(even_digit_number))

find_even_digit()