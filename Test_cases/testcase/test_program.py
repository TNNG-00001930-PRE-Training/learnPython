"""
    String Operations:
    Test cases for string concatenation
    Test cases for string slicing
    Test cases for string formatting
    Test cases for string manipulation methods (e.g., upper(), lower(), strip(), replace())
"""


#String concatenation
def concatenate_strings(str1, str2):
    return str1 + str2

string1 = "Hello, "
string2 = "World!"
result = concatenate_strings(string1, string2)
print(result)



#String Slicing Opeartion
def slice_string(string, start, end):
    return string[start:end]

text = "Python Programming"
sliced_text = slice_string(text, 7, 18)
print(sliced_text)



#String Formatting Operation
def format_string(name, age):
    return f"My name is {name} and I am {age} years old."

name = "Alice"
age = 30
formatted_text = format_string(name, age)
print(formatted_text)



#String Manipulations
def manipulate_string(string):
    upper_case = string.upper()
    lower_case = string.lower()
    stripped = string.strip()
    replaced = string.replace("Hello", "Hi")

    return upper_case, lower_case, stripped, replaced

text = "   Hello, World!   "
upper, lower, stripped, replaced = manipulate_string(text)
print(upper)
print(lower)
print(stripped)
print(replaced)