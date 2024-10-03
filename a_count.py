def contar_as(frase):
  """Conta o número de vezes que a letra 'a' aparece em uma frase.

  Args:
    frase: A frase a ser analisada.

  Returns:
    O número de ocorrências da letra 'a'.
  """

  return frase.lower().count('a')

frase = input("Digite uma frase: ")
print(f"A letra 'a' aparece {contar_as(frase)} vezes na frase.")
