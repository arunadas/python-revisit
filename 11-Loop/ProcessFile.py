# Read raw data
import os
os.chdir('/Users/prakash/Desktop/python/aruna-learning/code/11-Loop')

with open('buzzers.csv') as raw_data:
    print(raw_data.read())

# Read CSV data as lists
import csv

with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)  

# Read csv as dictionary
with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)        

# Reading file as single dictionary
from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

flights2 = {}

for k,v in flights.items():
    flights2[convert2ampm(k)] =  v.title()

pprint.pprint(flights2)  

# pattern in list

flight_times =[]
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))
print(flight_times)    

destinations = []
for desc in flights.values():
    destinations.append(desc.title())
print(destinations)    

# list comprehension 
more_dests = [desc.title() for desc in flights.values()]
print(more_dests)

# dict comprehension
more_dests = { convert2ampm(k) :  v.title() for k,v in flights.items()}
pprint.pprint(more_dests)

# using filter in comprehension
just_freeport = {}
for k, v in flights.items():
    if v == 'FREEPORT':
        just_freeport[convert2ampm(k)] = v.title()
print(just_freeport) 

just_freeport = { convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
print(just_freeport)

# Rewriting solution using comprehension
fts = { convert2ampm(k): v.title() for k,v in flights.items()}
pprint.pprint(fts)

# More comprehension examples
data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
evens = []
for num in data:
    if not num % 2:
      evens.append(num)

print(evens)      

evens = [ num for num in data if not num % 2]
print(evens)

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four' ]
words = []
for num in data:
   if isinstance(num, str):
       words.append(num)
print(words)       

words = [ num for num in data if isinstance(num, str)]  
print(words)     

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
     title.append(word.title())
print(title)

title = [ word.title() for word in data]
print(title)

dests = set(fts.values())
print(dests)

wests = []
for k, v in fts.items():
    if v == 'West End':
        wests.append(k)
print(wests) 

wests = [k for k, v in fts.items() if v== 'West End']
print(wests)

for dest in set(fts.values()):
    print(dest , '->' , [k for k, v in fts.items() if v == dest] )
 

when = {}
for dest in set(fts.values()):
    when[dest] =  [k for k, v in fts.items() if v == dest] 
pprint.pprint(when)

when2 = { dest:[k for k, v in fts.items() if v == dest] for dest in set(fts.values())}
pprint.pprint(when2)

#set comprehension

vowels = {'a', 'e', 'i','o','u'}
message = "Don't forget to pack your towel."

found = set() 
for v in vowels:
   if v in message:
     found.add(v)

print(found) 

found2 = { v for v in vowels if v in message }
print(found2)

#Listcomp vs generators
for i in [x*3 for x in [1, 2, 3, 4, 5]]:
     print(i)

for i in (x*3 for x in [1, 2, 3, 4, 5]):
     print(i)

