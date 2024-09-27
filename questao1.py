# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    indice = 0
    lista_fib = [0,1]

    while indice < n - 2:
        lista_fib.append(lista_fib[indice] + lista_fib[indice + 1])
        indice += 1
    
    return lista_fib


def is_fib(n):
    lista_fib = fibonacci(n+2)
    if n in lista_fib:
        return("Este número pertence a sequência de fibonacci!")
    else:
        return("Este número NÃO pertence a sequência de fibonacci")


numero = int(input("Digite o número que gostaria de verificar: "))
print(is_fib(numero))
