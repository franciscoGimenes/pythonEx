# Jogador 1 insere um número entre 1 e 10
numero_jogador1 = int(input("Jogador 1, insira um número entre 1 e 10: "))
while numero_jogador1 < 1 or numero_jogador1 > 10:
    print("Entrada inválida. Por favor, insira um número entre 1 e 10.")
    numero_jogador1 = int(input("Jogador 1, insira um número entre 1 e 10: "))

# Limpa a tela (opcional, para melhor experiência de jogo)
print("\n" * 50)

# Jogador 2 tenta adivinhar o número
print("Jogador 2, tente adivinhar o número!")
palpite_jogador2 = None
tentativas = 0
while palpite_jogador2 != numero_jogador1:
    palpite_jogador2 = int(input("Insira seu palpite: "))
    tentativas += 1
    if palpite_jogador2 < numero_jogador1:
        print("Muito baixo! Tente novamente.")
    elif palpite_jogador2 > numero_jogador1:
        print("Muito alto! Tente novamente.")

print(f"Parabéns, Jogador 2! Você adivinhou o número correto em {tentativas} tentativas!")
