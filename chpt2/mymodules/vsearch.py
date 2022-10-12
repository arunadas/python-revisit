def search4vowels(word: str) -> set:
        """ Display any vowels in the given word """
        vowels = set('aeiou')
        return vowels.intersection(word)
        

def search4letters(phrase: str, letters: str='aeiou') -> set:
        """ Display any letters in the given phrase """
        return set(letters).intersection(phrase)