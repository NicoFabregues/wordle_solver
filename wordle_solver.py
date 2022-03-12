""" Wordle solver by Nico Fabregues. """


def get_words_length_from_file(path, n, accented_mode=False):
    with open(path, encoding="utf-8") as file:
        content = file.read().splitlines()

        def filter_words(word):
            if len(word) != n:
                return False
            elif accented_mode:
                return True
            elif 'á' not in word and 'é' not in word and \
                'í' not in word and 'ó' not in word and 'ú' not in word:
                    return True
            else: return False

        return set(filter(filter_words, content))


def get_words_values(words, letters_ocurrences):
    final = dict()
    for word in words:
        final[word] = 0
        for letter in word:
            final[word] += letters_ocurrences.get(letter)
    return sorted(final, key=final.get, reverse=True)


def main():
    # Initial Required Inputs
    path = "./diccionario.txt"
    word_length = 5

    # Busco las palabras del archivo que tengan 5 letras.
    words = get_words_length_from_file(path, word_length)

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
        best = valued_words[0]
        print('\n\nBest Word = ', best)

        input_results = ''
        while(len(input_results) != 5):
            input_results = input('Ingresa los valores de cada letra en su respectivo orden (0-Mal, 1-Maso, 2-Bien): ')

        if input_results == 'salir':
            print("\n\n--- --- EXIT --- ---")
            return
        elif input_results == '22222':
            print("\n\n--- --- Congratulations! You win. --- ---")
            return

        i = 0
        for number,letter in zip(input_results, best):
            if number == '0':
                # Elimino las palabras que tenga una unica ocurrencia de esa letra.
                words = set(filter(lambda x: x.find(letter) == -1, words))

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

