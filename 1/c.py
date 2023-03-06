'''
Write two Python statements in the interactive mode to display the acronym 'LASER' form
the string "Light amplification by stimulated emission of radiation"
'''

sentence = "Light amplification by stimulated emission of radiation"
acronym = sentence[0] + sentence[6] + sentence[23] + sentence[-21] + sentence[-9]
print(acronym.upper())

