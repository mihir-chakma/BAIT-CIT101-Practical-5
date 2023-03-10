'''
Write two Python statements in the interactive mode to display the acronym 'COVID-19'
form the string " Coronavirus disease of 2019"
'''

c = " Coronavirus disease  of  2019"
acronym = c[1:3] + c[7:9] + c[13] + '-' + c[-2:]
print(acronym.upper())

