def contar_as(frase):
    """
    Conta o número de vezes que a letra 'a' aparece em uma frase.

    Esta função recebe uma frase como entrada, converte todas as letras para minúsculas
    para garantir que tanto 'a' maiúsculo quanto 'a' minúsculo sejam contados, e então
    conta quantas vezes a letra 'a' aparece na frase.

    Args:
        frase (str): A frase a ser analisada.

    Returns:
        int: O número de ocorrências da letra 'a' na frase.
    """
    return frase.lower().count('a')

def main():
    """
    Função principal que solicita ao usuário uma frase e exibe o número de vezes que a letra 'a' aparece.

    Esta função pede ao usuário para digitar uma frase, chama a função contar_as para contar
    as ocorrências da letra 'a' na frase fornecida, e então imprime o resultado.
    """
    frase = input("Digite uma frase: ")
    quantidade_as = contar_as(frase)
    print(f"A letra 'a' aparece {quantidade_as} vezes na frase.")

if __name__ == "__main__":
    main()
