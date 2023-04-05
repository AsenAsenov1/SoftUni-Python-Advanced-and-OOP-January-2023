def vowel_filter(function):
    vowels = "aeouiy"

    def wrapper():
        vowel_letters = [letter for letter in function() if letter.lower() in vowels]
        return vowel_letters

    return wrapper
