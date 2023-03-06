'''
Write two Python statements in the interactive mode to display the acronym 'RADAR' form
the string "Radio Detecting and Ranging"

'''

name = "Radio Detecting and Ranging"
acronym = name[0:2] + name[6] + name[16] + name[-7]
print(acronym.upper())
