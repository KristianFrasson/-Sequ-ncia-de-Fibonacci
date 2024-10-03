def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a+b
    return b == numero

# número que o usuario deseja saber se está presente na sequencia de fibonacci
numero = int(input("Digite um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
