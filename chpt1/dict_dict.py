import pprint


people = {}
people['Ford'] = {'Name' : 'Ford Prefect',
'Gender': 'Male',
'Occupation': 'Researcher',
'Home Planet': 'Betelgeuse Seven' }

people['Arthur'] = { 'Name': 'Arthur Dent',
'Gender': 'Male',
'Occupation': 'Sandwich-Maker',
'Home Planet': 'Earth' }

print(people)
pprint.pprint(people)

#what Arthur does?
print(people['Arthur']['Occupation'])