"""
Count the number of times the first letter of the English alphabet appears in the following
paragraph.

"A machine is a great moral educator. If a horse or a donkey won't go, men lose their
tempers and beat it; if a machine won't go, there is no use beating it. You have to think and
try till you find what is wrong. That is real education."

- Gilbert Murray

"""

paragraph = "A machine is a great moral educator. If a horse or a donkey won't go, men lose their tempers and beat it; if a machine won't go, there is no use beating it. You have to think and try till you find what is wrong. That is real education."

count = 0
for letter in paragraph:
    if letter == 'A' or letter == 'a':
        count += 1

print(f"The letter 'A' appears {count} times in the paragraph.")

