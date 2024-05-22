def barcelona():
    import pygame
    import sys
    import telainicio
    # Inicialize o Pygame
    pygame.init()


    def tela_final_barcelona1():
        # Código para exibir a tela final do Barcelona

        # Loop para verificar eventos
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    # Verifica se o clique ocorreu na área esquerda da tela
                    if evento.pos[0] < largura_tela / 2:
                        telainicio.inicio()  # Volta para a tela inicial

    # Defina as dimensões da tela
    largura_tela = 1250
    altura_tela = 760
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Exibição de Imagens")

    # Função para carregar e redimensionar imagens
    def carregar_imagem(nome_arquivo):
        imagem = pygame.image.load(nome_arquivo).convert()
        return pygame.transform.scale(imagem, (largura_tela, altura_tela))

    # Carregue as imagens que você deseja exibir
    imagens = ["personagens/barcelonatelafinal.png"]
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

    # Função para reiniciar o jogo
    def reiniciar_jogo():
        global passou_da_primeira_imagem
        passou_da_primeira_imagem = False
        # Aqui você pode redefinir outras variáveis ou estado do jogo conforme necessário

    # Variável para controlar se já passou da primeira imagem
    passou_da_primeira_imagem = False

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
                    # Reiniciar o jogo
                    telainicio.inicio()

                elif ponto_na_area(evento.pos, area_direita):
                    # sair do jogo
                    sys.exit()

        # Desenha a imagem atual
        desenhar_imagem()