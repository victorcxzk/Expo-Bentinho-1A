SENHA = "FOGOBABA"

def exibir_desafio():
    print("=" * 50)
    print("Nas profundezas do brejo sombrio vive o Monstro do Musgo,")
    print("uma criatura lendária coberta por lodo e vegetação.")
    print("Apenas quem conhece suas fraquezas pode passar.\n")
    print("Quais são as fraquezas do Monstro do Musgo?")
    print("A) Gelo e veneno")
    print("B) Água benta e trovão")
    print("C) Vento e luz do sol")
    print("D) Fogo e baba de cavalo")
    print("=" * 50)


def pedir_resposta():
    while True:
        resposta = input("Digite a letra da resposta (A, B, C ou D): ").strip().lower()
        
        # Aceita caso o visitante digite "d" ou "d)"
        if resposta == "d)":
            
            resposta = "d"

        if resposta in ["a", "b", "c", "d"]:
            return resposta
        
        print("Opção inválida! Escolha apenas A, B, C ou D.\n")


# Programa principal
exibir_desafio()

tentativas = 0
limite_tentativas = 2

while tentativas < limite_tentativas:
    tentativas += 1
    escolha = pedir_resposta()

    if escolha == "d":
        print("\nResposta correta!")
        print(f"Você conhece bem o brejo! Aqui está sua palavra: {SENHA}")
        print("Anote no diário e siga para a próxima estação, à sua esquerda.")
        break
    else:
        if tentativas < limite_tentativas:
            print("\nResposta incorreta.")
            print("DICA: Uma das fraquezas é algo que queima.")
            print("A outra vem de um animal que relincha.\n")
        else:
            # Regra do roteiro para não travar a fila da Expo
            print("\nTentativas esgotadas! Mas o Guardião reconhece seu esforço.")
            print(f"A palavra-chave é: {SENHA}")
            print("Anote no diário e siga para a próxima estação, à sua esquerda.")