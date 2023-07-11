import re
def remover_caracteres(texto):
    caracteres_unicos = []
    for caractere in texto:
        if caractere.isalpha() or re.match(r'[^\w\s]', caractere):
            if caractere not in caracteres_unicos:
             caracteres_unicos.append(caractere)
    return ''.join(caracteres_unicos)
entrada = input("Escreva uma frase: ")
saida = remover_caracteres(entrada)
print("Resultado:", saida)