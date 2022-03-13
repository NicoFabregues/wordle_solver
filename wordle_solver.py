""" Wordle solver by Nico Fabregues. """


def get_words_length_from_file(path, n):
    """ Open file and return its words of specified length. """
    with open(path, encoding="utf-8") as file:
        content = file.read().splitlines()
        return set(filter(lambda x: len(x) == n, content))


def get_words_values(words, letters_ocurrences):
    """ Returns a dict of words sorted by probability of occurrence. """
    final = dict()
    for word in words:
        final[word] = 0
        for letter in set(word):
            final[word] += letters_ocurrences.get(letter)
    return sorted(final, key=final.get, reverse=True)


def setup():
    """ Function to customize settings. """

    language = input("""\n\nSelect your language:\n\t1- English\n\t2- Spanish\n\n""")
    while language not in ['1', '2']:
        language = input("""\n\nSelect your language:\n\t1- English\n\t2- Spanish\n\n""")

    if language == '1':
        path = "./english_dict.txt"
    elif language == '2':
        path = "./spanish_dict.txt"
    # TODO: implement new languages.

    word_length = int(input("""\n\nSelect word length: """))
    while word_length < 3 or word_length > 7:
        print("\n\n--- --- Words length must be a number between 3 and 7 --- ---")
        word_length = int(input("""\n\nSelect word length: """))

    return path, word_length


def main():

    # Initial Required Inputs
    path, word_length = setup()

    words = get_words_length_from_file(path, word_length)

    print(f"\n\n--- --- Words Original Amount: {len(words)} --- ---")

    from collections import Counter
    letters_ocurrences = Counter("".join(words))

    while(True):

        valued_words = get_words_values(words, letters_ocurrences)
        if not valued_words:
            print("\n\n--- --- ERROR: No words left. --- ---")
            return

        iter_valued_words = iter(valued_words)
        best = next(iter_valued_words, False)
        print('\n\nBest Word = ', best)

        answer = ''
        while(True):
            answer = input('Enter the value of each letter in their respective order (0-Bad, 1-Wrong spot, 2-Good): ')

            if len(answer) == 5 and answer.isdigit():
                break
            elif answer == 'win':
                print("\n\n--- --- Congratulations! You win. --- ---")
                return
            elif answer == 'stop':
                print("\n\n--- --- EXIT --- ---")
                return
            elif answer == 'restart':
                print("\n\nRestarting ...")
                main()
                return
            elif answer == 'next' or answer == 'not valid':
                if answer == 'not valid' and best in words:
                    # Si no es válida la elimino.
                    words.remove(best)
                print("\n\nSearching for next word ...")
                best = next(iter_valued_words, False)
                if not best:
                    print("\n\n--- --- ERROR: No words left. --- ---")
                    return
                print('\n\nBest Word = ', best)
            elif answer == 'input':
                best = input('\n\nEnter your custom word: ')

        i = 0
        for number,letter in zip(answer, best):
            if number == '0':
                # Remove words that contain this letter only one time.
                words = set(filter(lambda x: x.count(letter) != 1, words))
            elif number == '1':
                # Keep words that contain this letter in other spot.
                words = set(filter(lambda x: x.find(letter) != -1 and x.find(letter) != i, words))
            elif number == '2':
                # Keep words that contain this letter in this spot.
                words = set(filter(lambda x: x.find(letter) == i, words))
            i += 1
        print('Words Left = ', len(words))


if __name__ == "__main__":
    main()

