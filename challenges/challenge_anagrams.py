# feito com o link a seguir:
# https://www.geeksforgeeks.org/python-sorted-check-two-strings-anagram-not/

def is_anagram(first_string, second_string):
    first_word = first_string.lower()
    second_word = second_string.lower()

    # se o comprimento de duas frases não forem o mesmo, não são anagramas.
    if len(first_word) != len(second_word):
        return False
 
    # inicia o dicionário
    counts = {}
 
    # percorre simultaneamente pelos caracteres das duas strings.
    for c1, c2 in zip(first_word, second_word):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1
        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1
    
    print(counts)

    # Percorre os valores do dicionário.
    # se o dicionário contém ao menos um valor
    # que é diferente de 0, a string não é um anagrama
    for count in counts.values():
        if count != 0:
            return False
    return True

print(is_anagram("pedra", "perda"))