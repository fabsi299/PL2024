import re
import sys


def somar_sequencias(texto):
    sequencias = re.findall(r'-?\d+', texto)  # Encontrar todas as sequências de dígitos
    soma_total = sum(map(int, sequencias))
    return soma_total


def processar_texto(texto):
    partes = re.split(r'(\bOff\b|\bOn\b|=)', texto, flags=re.IGNORECASE)  # Dividir o texto com base em "Off", "On" e "="

    somar = False
    soma_total = 0

    for parte in partes:
        parte = parte.strip()
        if parte.lower() == 'off':
            somar = False  # Desliga a soma quando "Off" é encontrado
        elif parte.lower() == 'on':
            somar = True
        elif parte == '=':
            print(soma_total)
        elif somar:
            soma_total += somar_sequencias(parte)


if len(sys.argv) < 2:
    print("Por favor, especifique o nome do arquivo como argumento.")
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    processar_texto(file.read())

