""" Wordle solver by Nico Fabregues. """


def get_words_length_from_file(path, n):
    with open(path, encoding="utf-8") as file:
        content = file.read().splitlines()
        return set(filter(lambda x: len(x) == n, content))


def get_words_values(words, letters_ocurrences):
    final = dict()
    for word in words:
        final[word] = 0
        for letter in set(word):
            final[word] += letters_ocurrences.get(letter)
    return sorted(final, key=final.get, reverse=True)


def main():
    # Initial Required Inputs
    path = "./diccionario.txt"
    # path = "./english_dict.txt"
    word_length = 5

    # Busco las palabras del archivo que tengan 5 letras.
    original_words = words = get_words_length_from_file(path, word_length)

    print("\n\n--- --- Words Original Amount: %s --- ---", len(words))

    from collections import Counter
    # Cuento la cantidad de ocurrencias de cada letra.
    letters_ocurrences = Counter("".join(words))

    while(True):
        # Punteo las palabras en base a las ocurrencias de las letras,
        # Para obtener la palabra con las mejores ocurrencias.
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
                # Elimino las palabras que tenga una unica ocurrencia de esa letra.
                words = set(filter(lambda x: x.count(letter) != 1, words))
            elif number == '1':
                # Filtro las palabras que solo tengan esa letra.
                words = set(filter(lambda x: x.find(letter) != -1 and x.find(letter) != i, words))
            elif number == '2':
                # Filtro las palabras que solo tengan esa letra en posicion.
                words = set(filter(lambda x: x.find(letter) == i, words))
            i += 1
        print('Words Left = ', len(words))


if __name__ == "__main__":
    main()

