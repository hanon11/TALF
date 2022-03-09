quijote = open('ElQuijote.txt','r') 
lista = []
for linea in quijote:
    frase = linea.split()
    for pal in frase:
        lista.append(pal)
lista_lower = []
for elemento in lista:
    lista_lower.append(elemento.lower())

alfabeto = ['a', 'd', 'l', 'h', 'i', 'g' , 'o'] 
contiene = False
final = []
for elemento in lista_lower:
    contiene = False
    for letra in elemento:
        if letra not in alfabeto:
            contiene = True
    if contiene == False:
        final.append(elemento)
convert_to_set = set(final) # sin repeticiones
print(convert_to_set)
quijote.close()