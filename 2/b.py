""" 
Write a Python application to input any word and find the ratio of the frequency of a given
letter in the word to the length of the word. Provide five different outputs.
"""

word = input("Input a word: ")
letter = input("Input a letter to find the frequency: ")

word_length = len(word)

letter_count = word.count(letter)

print(f"Frequency of letter {letter}: and Word Length = {letter_count}:{word_length}")


