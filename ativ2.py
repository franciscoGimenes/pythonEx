import os

lanches = [
    {
        'nome': 'Cachorro quente',
        'codigo': 100,
        'preco': 3.50
    },
    {
        'nome': 'Bauru simples',
        'codigo': 101,
        'preco': 3.80
    },
    {
        'nome': 'Bauru c/ovo',
        'codigo': 102,
        'preco': 4.50
    },
    {
        'nome': 'Hamburger',
        'codigo': 103,
        'preco': 4.70
    },
    {
        'nome': 'Cheeseburguer',
        'codigo': 104,
        'preco': 5.30
    },
    {
        'nome': 'Refrigerante',
        'codigo': 105,
        'preco': 4.00
    }
]
carrinho = []

def listarLanches():
    print(f"{'CÓDIGO':<10}{'NOME':<25}{'PREÇO':>10}")
    print('-' * 45)
    for lanche in lanches:
        print(f"{lanche['codigo']:<10}{lanche['nome']:<25}R${lanche['preco']:>7.2f}")
def listarCarrinho():
    print(f"{'CÓDIGO':<10}{'NOME':<25}{'PREÇO':>10}")
    print('-' * 45)
    precoTotal = 0
    for produto in carrinho:
        precoTotal += produto['preco']
        print(f"{produto['codigo']:<10}{produto['nome']:<25}R${produto['preco']:>7.2f}")
    print('-' * 45)
    print(f"{'TOTAL':<35}R${precoTotal:>7.2f}")

os.system('cls')



while True:
    print('MENU INICIAL')
    print('-' * 45)
    print('0 - sair')
    print('1 - começar nova compra')
    escolhaMenu1 = int(input('\nEscolha: '))
    if escolhaMenu1 == 0:
        break
    
    while True:
        print('\n')
        os.system('cls')
        if len(carrinho) > 0:
            print(f"{carrinho[len(carrinho) - 1]['nome']} adicionado ao carrinho!")
        listarLanches()
        codigo = int(input('\nDigite o codigo do produto para adiconar (digite 0 para finalizar e 1 para ver o carrinho ): '))
        if codigo == 0:
            listarCarrinho()
            print('\nNão se esqueça de cobrar o cliente!')
            input('pressione ENTER para finalizar')
            break
        if codigo == 1:
            while True:
                os.system('cls')
                if len(carrinho) < 1:
                    print('\ncarrinho vazio')
                else:
                    listarCarrinho()
                
                input('\npressione ENTER para voltar')
                break
                
        for lanche in lanches:
            if lanche['codigo'] == codigo:
                carrinho.append(lanche)
                print(f"{lanche['nome']} adicionado ao carrinho!")
                

