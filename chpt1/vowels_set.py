vowels = set('aeiou')
word = input("Provide a word to search for vowels: ")

found =  vowels.intersection(set(word))
#found_list = sorted(found)

for vowel in found:
    print(vowel)

