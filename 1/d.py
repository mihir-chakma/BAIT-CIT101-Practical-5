'''
Write two Python statements in the interactive mode to display the acronym 'SIM' form
the string " Subscriber Identity Module ". 
'''

sim = " Subscriber Identity Module "
acronym = sim[1] + sim[12] + sim[-7]
print(acronym.upper())


text = " Subscriber Identity Module "
rspace = text.split() # split and remove space
text = ''.join(rspace)
print((text[0] + text[10] + text[-6]).upper())

