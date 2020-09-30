"""
Intro to python exercises shell code
"""

def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if (x % 2 == 0):
        return True
    
    return False

print(is_odd(2))
print(is_odd(3))

def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    if (word == word[::-1]):
        return True
   
    return False

print(is_palindrome('level'))
print(is_palindrome('word'))

def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    oddlist = []
    
    for i in numlist:
        if i % 2 == 0:
            pass
        else:
            oddlist.append(i)
    
    return oddlist

print(only_odds([1,2,3,4,5,6,7,8,9]))
    
            

def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    words = text.split()
    lower_words = []
    for word in words:
        lower_word = word.lower()
        lower_words.append(lower_word)
    words_dict = dict.fromkeys(lower_words)
    for i in words_dict.keys():
        counter = 0
        for j in lower_words:
            if i == j:
                counter += 1
                
        words_dict[i] = counter
    
    return words_dict
print(count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?"))
