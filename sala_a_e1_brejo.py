import os

# Ativa suporte a formatação ANSI no terminal do Windows
os.system("")

# Expo Bentinho - Sala A (Estação 1: Brejo)
SENHA = "FOGOBABA"

# Cores e estilos ANSI para o terminal
AMARELO = "\033[1;33m"
CIANO = "\033[1;36m"
VERDE = "\033[1;32m"
VERMELHO = "\033[1;31m"
BRANCO = "\033[1;97m"
RESET = "\033[0m"


def exibir_desafio():
    # Mostra a história e as alternativas do desafio
    print(f"{AMARELO}{'=' * 50}{RESET}")
    print(f"{AMARELO}A LENDA DE NESSA - ESTAÇÃO 1: O BREJO{RESET}")
    print(f"{AMARELO}{'=' * 50}{RESET}")
    print("Você adentra o brejo sombrio e encontra o Monstro do Musgo,")
    print("uma criatura ancestral feita de folhagens, raízes e lodo.\n")
    print("Para conquistar a palavra do seu diário e seguir jornada,")
    print("o Guardião exige que você revele as fraquezas da criatura.\n")
    print("Dizem os antigos viajantes:")
    print('"Criaturas de folhas e lama temem o calor que as consome,')
    print('combinado a um segredo bizarro que nenhum mago esperaria."\n')
    print(f"{CIANO}Quais são as fraquezas do Monstro do Musgo?{RESET}")
    print(f"{CIANO}A){RESET} Gelo e veneno")
    print(f"{CIANO}B){RESET} Água benta e trovão")
    print(f"{CIANO}C){RESET} Vento e luz do sol")
    print(f"{CIANO}D){RESET} Fogo e baba de cavalo")
    print(f"{AMARELO}{'=' * 50}{RESET}")


def pedir_resposta():
    # Valida a resposta do visitante (aceita variações como 'd)' ou 'd.')
    while True:
        resposta = input(f"{BRANCO}Digite a letra da resposta (A, B, C ou D): {RESET}").strip().lower()
        resposta = resposta.replace(")", "").replace(".", "").strip()

        if resposta in ["a", "b", "c", "d"]:
            return resposta
        
        print(f"\n{VERMELHO}Opção inválida! Escolha apenas A, B, C ou D.{RESET}\n")


def iniciar_estacao():
    # Controla o fluxo da estação, tentativas e dicas
    exibir_desafio()

    tentativas = 0
    limite_tentativas = 2

    while tentativas < limite_tentativas:
        tentativas += 1
        print(f"\n{BRANCO}[Tentativa {tentativas} de {limite_tentativas}]{RESET}")
        escolha = pedir_resposta()

        if escolha == "d":
            print(f"\n{VERDE}Resposta correta!{RESET}")
            print(f"Você conhece bem o brejo! Aqui está sua palavra: {AMARELO}{SENHA}{RESET}")
            print("Anote no diário e siga para a próxima estação, à sua direita.")
            break
        else:
            if tentativas < limite_tentativas:
                # Dica para a segunda tentativa
                print(f"\n{VERMELHO}Resposta incorreta.{RESET}")
                print(f"{AMARELO}DICA:{RESET} Uma das fraquezas é algo que queima.")
                print("A outra vem de um animal que relincha.\n")
            else:
                # Regra para não travar a fila da Expo
                print(f"\n{VERMELHO}Tentativas esgotadas!{RESET} Mas o Guardião reconhece seu esforço.")
                print(f"A palavra-chave é: {AMARELO}{SENHA}{RESET}")
                print("Anote no diário e siga para a próxima estação, à sua direita.")


# Loop contínuo para o estande na feira
if __name__ == "__main__":
    while True:
        os.system("cls")
        iniciar_estacao()
        print("\n" + "-" * 50)
        input("Pressione [ENTER] para o próximo visitante...")
