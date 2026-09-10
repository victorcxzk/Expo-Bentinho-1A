import os

# Ativa suporte a formatação ANSI no terminal do Windows
os.system("")

# Expo Bentinho - Sala A (Estação 1: Brejo)
SENHA = "FOGOBABA"

# Estilo para destacar textos no terminal
NEGRITO = "\033[1m"
RESET = "\033[0m"


def exibir_desafio():
    # Mostra a história e as alternativas do desafio
    print("=" * 50)
    print(f"{NEGRITO}A LENDA DE NESSA - ESTAÇÃO 1: O BREJO{RESET}")
    print("=" * 50)
    print("Você adentra o brejo sombrio e encontra o Monstro do Musgo,")
    print("uma criatura ancestral feita de folhagens, raízes e lodo.\n")
    print("Para conquistar a palavra do seu diário e seguir jornada,")
    print("o Guardião exige que você revele as fraquezas da criatura.\n")
    print("Dizem os antigos viajantes:")
    print('"Criaturas de folhas e lama temem o calor que as consome,')
    print('combinado a um segredo bizarro que nenhum mago esperaria."\n')
    print(f"{NEGRITO}Quais são as fraquezas do Monstro do Musgo?{RESET}")
    print(f"{NEGRITO}A){RESET} Gelo e veneno")
    print(f"{NEGRITO}B){RESET} Água benta e trovão")
    print(f"{NEGRITO}C){RESET} Vento e luz do sol")
    print(f"{NEGRITO}D){RESET} Fogo e baba de cavalo")
    print("=" * 50)


def pedir_resposta():
    # Valida a resposta do visitante (aceita variações como 'd)' ou 'd.')
    while True:
        resposta = input(f"{NEGRITO}Digite a letra da resposta (A, B, C ou D): {RESET}").strip().lower()
        resposta = resposta.replace(")", "").replace(".", "").strip()

        if resposta in ["a", "b", "c", "d"]:
            return resposta
        
        print("\nOpção inválida! Escolha apenas A, B, C ou D.\n")


def iniciar_estacao():
    # Controla o fluxo da estação, tentativas e dicas
    exibir_desafio()

    tentativas = 0
    limite_tentativas = 2

    while tentativas < limite_tentativas:
        tentativas += 1
        print(f"\n{NEGRITO}[Tentativa {tentativas} de {limite_tentativas}]{RESET}")
        escolha = pedir_resposta()

        if escolha == "d":
            print(f"\n{NEGRITO}Resposta correta!{RESET}")
            print(f"Você conhece bem o brejo! Aqui está sua palavra: {NEGRITO}{SENHA}{RESET}")
            print("Anote no diário e siga para a próxima estação, à sua direita.")
            break
        else:
            if tentativas < limite_tentativas:
                # Dica para a segunda tentativa
                print(f"\n{NEGRITO}Resposta incorreta.{RESET}")
                print(f"{NEGRITO}DICA:{RESET} Uma das fraquezas é algo que queima.")
                print("A outra vem de um animal que relincha.\n")
            else:
                # Regra para não travar a fila da Expo
                print(f"\n{NEGRITO}Tentativas esgotadas! Mas o Guardião reconhece seu esforço.{RESET}")
                print(f"A palavra-chave é: {NEGRITO}{SENHA}{RESET}")
                print("Anote no diário e siga para a próxima estação, à sua direita.")


# Loop contínuo para o estande na feira
if __name__ == "__main__":
    while True:
        os.system("cls")
        iniciar_estacao()
        print("\n" + "-" * 50)
        input("Pressione [ENTER] para o próximo visitante...")
