def print_upper_words(words, starts_with=['']):
    """A function that prints each entry of a list of words in all upper case, but only if that word starts"""
    for word in words:
        if starts_with == ['']:
            print(word.upper())
        else:
            for letter in starts_with:
                if len(letter) > 1:
                    print("each entry in starts_with must be 1 letter")
                elif letter.isalpha():
                    if word.startswith(letter):
                        print(word.upper())
                else:
                    print('each entry in starts_with must be a letter')

