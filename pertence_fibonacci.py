def pertence_fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci.

    Esta função utiliza um método iterativo para gerar números da sequência de Fibonacci
    até que o número gerado seja maior ou igual ao número fornecido. Se o número gerado
    for igual ao número fornecido, então ele pertence à sequência de Fibonacci.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número pertence à sequência de Fibonacci, False caso contrário.
    """
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def main():
    """
    Função principal que solicita ao usuário um número e verifica se ele pertence à sequência de Fibonacci.

    Esta função pede ao usuário para digitar um número, chama a função pertence_fibonacci para verificar
    se o número pertence à sequência de Fibonacci, e então imprime o resultado.
    """
    numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
    
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
