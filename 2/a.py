"""
Write the Python statements needed to input the following string and display at least five
meaningful words constructed from it.
“Machine learning is a growing technology” (For example one word that you can construct is 'chin')
"""

input_string = input("Enter your string: ")
five_words = input_string.split(sep=" ", maxsplit=4)
print(five_words)

