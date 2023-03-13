"""
Write the Python statements needed to input the following string and display at least five
meaningful words constructed from it.
“Machine learning is a growing technology” (For example one word that you can construct is 'chin')
"""

text = input("Enter your string: ")

all = f"{text[8:13]} \n{text[-15:-11]} \n{text[23:26]} \n{text[-4:-1]} \n{text[9:13]}"

print(all)









# print(text[2:6])
# print(text[8:13])
# print(text[-15:-11])
# print(text[23:26])
# print(text[-6:-4])
# print(text[-4:-1])
# print(text[9:13])
