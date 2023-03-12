'''
Write two Python statements in the interactive mode to display the acronym 'RADAR' form
the string "Radio Detecting and Ranging"

'''

text = "Radio Detecting and Ranging"
acronym = text[0:2] + text[6] + text[16] + text[-7]
print(acronym.upper())
