# Jogo da Velha em Python
def main():
    tabuleiro = [" " for _ in range(9)]  # Tabuleiro vazio
    jogador_atual = "X"

    while True:
        # Exibe o tabuleiro
        print("\n" + "-" * 13)
        for i in range(3):
            print(f"| {tabuleiro[i*3]} | {tabuleiro[i*3+1]} | {tabuleiro[i*3+2]} |")
            print("-" * 13)

        # Verifica vitória ou empate
        if verificar_vitoria(tabuleiro, "X"):
            print("\nJogador X venceu!")
            break
        elif verificar_vitoria(tabuleiro, "O"):
            print("\nJogador O venceu!")
            break
        elif " " not in tabuleiro:
            print("\nEmpate!")
            break

        # Recebe a jogada
        try:
            posicao = int(input(f"\nJogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if posicao < 0 or posicao > 8:
                print("\nPosição inválida! Escolha de 1 a 9.")
                continue
            if tabuleiro[posicao] != " ":
                print("\nPosição já ocupada!")
                continue
        except ValueError:
            print("\nEntrada inválida! Digite um número.")
            continue

        # Atualiza o tabuleiro
        tabuleiro[posicao] = jogador_atual
        jogador_atual = "O" if jogador_atual == "X" else "X"

def verificar_vitoria(tabuleiro, simbolo):
    # Verifica linhas, colunas e diagonais
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo:
            return True
    return False

if __name__ == "__main__":
    main()