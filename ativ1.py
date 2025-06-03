import os


populacaoA = 98000000
taxaCrescimentoA = 1.035
populacaoB = 200000000
taxaCrescimentoB = 1.015
ano = 0

def formatacao(numero):
        return f'{int(numero):,}'.replace(',', '.')
os.system('cls')

print(f'população A atual: {formatacao(populacaoA)}')
print(f'população B atual: {formatacao(populacaoB)}')

while populacaoA < populacaoB:
    populacaoA = populacaoA * taxaCrescimentoA
    populacaoB = populacaoB * taxaCrescimentoB
    ano += 1

print(f'em {ano} anos, a população A será de {formatacao(populacaoA)}, e a população B de {formatacao(populacaoB)}')