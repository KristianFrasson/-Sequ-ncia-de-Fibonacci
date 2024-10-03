def proximo_elemento_a(seq):
    # Sequência de números ímpares consecutivos
    return seq[-1] + 2

def proximo_elemento_b(seq):
    # Sequência onde cada número é o dobro do anterior
    return seq[-1] * 2

def proximo_elemento_c(seq):
    # Sequência de quadrados perfeitos
    n = int(len(seq) ** 0.5) + 1
    return n * n

def proximo_elemento_d(seq):
    # Sequência de quadrados perfeitos de números pares
    n = int((seq[-1] ** 0.5) // 2 * 2 + 2)
    return n * n

def proximo_elemento_e(seq):
    # Sequência de Fibonacci
    return seq[-1] + seq[-2]

def proximo_elemento_f(seq):
    # Sequência de números que contêm o dígito '1'
    n = seq[-1] + 1
    while '1' not in str(n):
        n += 1
    return n

# Testando as funções
seq_a = [1, 3, 5, 7]
seq_b = [2, 4, 8, 16, 32, 64]
seq_c = [0, 1, 4, 9, 16, 25, 36]
seq_d = [4, 16, 36, 64]
seq_e = [1, 1, 2, 3, 5, 8]
seq_f = [2, 10, 12, 16, 17, 18, 19]

print(proximo_elemento_a(seq_a))  # 9
print(proximo_elemento_b(seq_b))  # 128
print(proximo_elemento_c(seq_c))  # 49
print(proximo_elemento_d(seq_d))  # 100
print(proximo_elemento_e(seq_e))  # 13
print(proximo_elemento_f(seq_f))  # 20
