import time

def descobrir_interruptores():
    # Estado inicial das lâmpadas (todas desligadas e frias)
    lampadas = {'A': 'desligada', 'B': 'desligada', 'C': 'desligada'}
    temperatura = {'A': 'fria', 'B': 'fria', 'C': 'fria'}

    # Primeira ida: ligar o interruptor A por alguns minutos
    lampadas['A'] = 'ligada'
    temperatura['A'] = 'quente'
    time.sleep(2)  # Simula o tempo de espera

    # Desligar o interruptor A e ligar o interruptor B
    lampadas['A'] = 'desligada'
    lampadas['B'] = 'ligada'
    time.sleep(1)  # Simula o tempo de espera

    # Primeira observação
    print("Primeira ida à sala das lâmpadas:")
    for lampada, estado in lampadas.items():
        print(f"Lâmpada {lampada}: {estado}, {temperatura[lampada]}")

    # Determinar qual interruptor controla qual lâmpada
    if lampadas['B'] == 'ligada':
        print("A lâmpada acesa é controlada pelo interruptor B.")
    if temperatura['A'] == 'quente' and lampadas['A'] == 'desligada':
        print("A lâmpada quente e apagada é controlada pelo interruptor A.")
    if temperatura['C'] == 'fria' and lampadas['C'] == 'desligada':
        print("A lâmpada fria e apagada é controlada pelo interruptor C.")

descobrir_interruptores()
