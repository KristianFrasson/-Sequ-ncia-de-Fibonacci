def calcular_soma(indice):
    """
    Calcula a soma dos números inteiros de 1 até o índice fornecido.

    Esta função utiliza um loop `while` para iterar de 1 até o índice fornecido,
    acumulando a soma dos números.

    Args:
        indice (int): O índice até o qual a soma será calculada.

    Returns:
        int: A soma dos números inteiros de 1 até o índice fornecido.
    """
    soma = 0
    k = 1

    while k < indice:
        k += 1
        soma += k

    return soma

def main():
    """
    Função principal que define o índice e calcula a soma dos números inteiros até esse índice.

    Esta função define um índice, chama a função `calcular_soma` para calcular a soma dos números
    inteiros de 1 até o índice, e então imprime o resultado.
    """
    indice = 12
    resultado = calcular_soma(indice)
    print(f"A soma dos números inteiros de 1 até {indice} é {resultado}.")

if __name__ == "__main__":
    main()
