import pygame
import sys

def inicio():
    # Inicialize o Pygame
    pygame.init()

    # Defina as dimensões da tela
    largura_tela = 1280
    altura_tela = 920
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Exibição de Imagens")

    # Função para carregar e redimensionar imagens
    def carregar_imagem(nome_arquivo):
        imagem = pygame.image.load(nome_arquivo).convert()
        return pygame.transform.scale(imagem, (largura_tela, altura_tela))

    # Carregue as imagens que você deseja exibir
    imagens = ["personagens/Ini.jpg", "personagens/Time.jpg"]
    num_imagens = len(imagens)
    indice_imagem_atual = 0
    imagem_atual = carregar_imagem(imagens[indice_imagem_atual])

    # Função para desenhar a imagem atual na tela
    def desenhar_imagem():
        tela.fill((255, 255, 255))
        tela.blit(imagem_atual, (0, 0))
        pygame.display.flip()

    # Função para verificar se um ponto está dentro de uma área clicável
    def ponto_na_area(ponto, area):
        return area.collidepoint(ponto)

    # Função para criar as áreas clicáveis na imagem "time.jpg"
    def criar_areas_clicaveis():
        # Define a área clicável no lado esquerdo da tela
        area_clicavel_esquerda = pygame.Rect(0, 0, largura_tela // 4, altura_tela)
        # Define a área clicável no lado direito da tela
        area_clicavel_direita = pygame.Rect(largura_tela // 2 + largura_tela // 5, 0, largura_tela // 5, altura_tela)

        return area_clicavel_esquerda, area_clicavel_direita

    # Variável para controlar se já passou da primeira imagem
    passou_da_primeira_imagem = False

    # Carregue o áudio de fundo
    pygame.mixer.music.load("sons/Hino da UEFA Champions League - (Letra e Tradução PT-BR).mp3")
    pygame.mixer.music.play(-1)  # -1 para reprodução em loop

    # Loop principal do jogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and not passou_da_primeira_imagem:
                    # Avance para a próxima imagem
                    indice_imagem_atual = (indice_imagem_atual + 1) % num_imagens
                    # Carregue a próxima imagem
                    imagem_atual = carregar_imagem(imagens[indice_imagem_atual])
                    # Indique que já passou da primeira imagem
                    passou_da_primeira_imagem = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique ocorreu dentro das áreas clicáveis
                area_esquerda, area_direita = criar_areas_clicaveis()
                if ponto_na_area(evento.pos, area_esquerda):
                    import jogobayernxborussia
                    jogobayernxborussia.bayernxboru()
                elif ponto_na_area(evento.pos, area_direita):
                    import jogorealmadridxbarcelona
                    jogorealmadridxbarcelona.realxbarca()

        # Desenha a imagem atual na tela
        desenhar_imagem()
