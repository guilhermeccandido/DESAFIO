import re
def reverter_txt(original):
    texto = original.split()
    texto_revertido = texto[::-1]
    original_revertida = " ".join(texto_revertido)
    return original_revertida
original_ordem = input("digite aqui o que deseja reverter: ")
original_ordem = re.sub(r'\d', '', original_ordem)
original_revertida = reverter_txt(original_ordem)
print("Frase revertida:", original_revertida)
