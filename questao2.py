# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def verifica_string(string):
    string_formatada = string.lower()
    boole = string_formatada.find('a')

    if boole != -1:
        return f'A string contém a letra "a" {string_formatada.count("a")} vezes!'
    else:
        return 'A string não contém a letra "a"'


texto = input("Digite o texto que gostaria de verificar: ")
print(verifica_string(texto))
