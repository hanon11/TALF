quijote = open('ElQuijote.txt', 'r')

list = []
for line in quijote:
    frase = line.split()
    for pal in frase:
        list.append(pal)
lista_lower = []
for element in list:
    lista_lower.append(element.lower())

alphabet = ['a', 'd', 'l', 'h', 'i', 'g', 'o']  # alphabet that we accept
contains = False
final = []
for element in lista_lower:
    contains = False
    for char in element:
        if char not in alphabet:  # si la palabra tiene alguna letra que no este en el alfabeto, la descarto
            contains = True
    if not contains:
        final.append(element)
converted_to_set = set(final)
print('Palabras del quijote: ' + str(converted_to_set))
transitions = {  # if any transition has the letter h, i, g or  o, I stay in the current state
    'q0': {'a': 'A', 'l': 'L', 'd': 'D', 'h': 'q0', 'i': 'q0', 'g': 'q0', 'o': 'q0'},
    'A': {'a': 'AA', 'l': 'AL', 'd': 'AD', 'h': 'A', 'i': 'A', 'g': 'A', 'o': 'A'},
    'L': {'a': 'AL', 'l': 'DEAD', 'd': 'DL', 'h': 'L', 'i': 'L', 'g': 'L', 'o': 'L'},
    'D': {'a': 'AD', 'l': 'DL', 'd': 'DEAD', 'h': 'D', 'i': 'D', 'g': 'D', 'o': 'D'},
    'AA': {'a': 'DEAD', 'l': 'AAL', 'd': 'AAD', 'h': 'AA', 'i': 'AA', 'g': 'AA', 'o': 'AA'},
    'AD': {'a': 'AAD', 'l': 'ADL', 'd': 'DEAD', 'h': 'AD', 'i': 'AD', 'g': 'AD', 'o': 'AD'},
    'AL': {'a': 'AAL', 'l': 'DEAD', 'd': 'ADL', 'h': 'AL', 'i': 'AL', 'g': 'AL', 'o': 'AL'},
    'DL': {'a': 'ADL', 'l': 'DEAD', 'd': 'DEAD', 'h': 'DL', 'i': 'DL', 'g': 'DL', 'o': 'DL'},
    'AAD': {'a': 'DEAD', 'l': 'AADL', 'd': 'DEAD', 'h': 'AAD', 'i': 'AAD', 'g': 'AAD', 'o': 'AAD'},
    'ADL': {'a': 'AADL', 'l': 'DEAD', 'd': 'DEAD', 'h': 'ADL', 'i': 'ADL', 'g': 'ADL', 'o': 'ADL'},
    'AAL': {'a': 'DEAD', 'l': 'DEAD', 'd': 'AADL', 'h': 'AAL', 'i': 'AAL', 'g': 'AAL', 'o': 'AAL'},
    'AADL': {'a': 'DEAD', 'l': 'DEAD', 'd': 'DEAD', 'h': 'AADL', 'i': 'AADL', 'g': 'AADL', 'o': 'AADL'},
    'DEAD': {'a': 'DEAD', 'l': 'DEAD', 'd': 'DEAD', 'h': 'DEAD', 'i': 'DEAD', 'g': 'DEAD', 'o': 'DEAD'}
}


accepted = []
for word in converted_to_set:
    actual_state = 'q0'
    for char in word:
        actual_state = transitions[actual_state][char]
    if actual_state != 'DEAD':
        accepted.append(word)
print('Palabras aceptadas: ' + str(accepted))

prueba = ['HALA', 'HALO', 'HADA', 'LIADA', 'GALGO', 'LADO', 'HALAGO', 'HALLA', 'DADO', 'ALADA', 'HALAGA', 'LOLA']
lista_lower = []
for element in prueba:
    lista_lower.append(element.lower())
accepted = []
not_accepted = []
for word in lista_lower:
    actual_state = 'q0'
    for char in word:
        actual_state = transitions[actual_state][char]
    if actual_state != 'DEAD':
        accepted.append(word)
    else:
        not_accepted.append(word)


print('\n*****EJEMPLO DEL CAMPUS*****')
print('Palabras aceptadas: ' + str(accepted))
print('Palabras NO aceptadas: ' + str(not_accepted))
quijote.close()
