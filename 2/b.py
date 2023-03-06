""" 
Write a Python application to input any word and find the ratio of the frequency of a given
letter in the word to the length of the word. Provide five different outputs.
"""

word = input("Enter a word: ")
letter = input("Enter a letter: ")

count = word.count(letter)
ratio = count / len(word)

print(f"The ratio of '{letter}' in '{word}' is {ratio:.2f}")

