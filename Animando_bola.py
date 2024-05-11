import pygame
import sys
import random

from pygame.time import Clock


def animacao_bola(): #Animando a bola e configurando
    global velocidade_bola_x, velocidade_bola_y, score_jogador, score_oponente, score_time, ball_speed, largura_tela, altura_tela, jogador, oponente, bola
    
    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y
    
    if bola.top <= 0 or bola.bottom >= altura_tela:
        velocidade_bola_y *= -1
    
    # Score do jogador
    if bola.left <= 0:
        score_time = pygame.time.get_ticks() # Só roda uma vez, 1 ponto por tempo
        score_jogador += 1
        #Checkando vitória
    
    # Score do oponente
    if bola.right >= largura_tela:
        score_time = pygame.time.get_ticks() 
        score_oponente += 1
        #Checkando vitória

    if bola.colliderect(jogador) and velocidade_bola_x > 0:
        if abs(bola.right - jogador.left) < 10:
            velocidade_bola_x *= -1
        elif abs(bola.bottom - jogador.top) < 10 and velocidade_bola_y > 0:
            velocidade_bola_y *= -1
        elif abs(bola.top - jogador.bottom) < 10 and velocidade_bola_y < 0:
            velocidade_bola_y *= -1        

    if bola.colliderect(oponente) and velocidade_bola_x < 0:
        if abs(bola.left - oponente.right) < 10:
            velocidade_bola_x *= -1
        elif abs(bola.bottom - oponente.top) < 10 and velocidade_bola_y > 0:
            velocidade_bola_y *= -1
        elif abs(bola.top - oponente.bottom) < 10 and velocidade_bola_y < 0:
            velocidade_bola_y *= -1 
# Configuração do Pygame
pygame.mixer.pre_init(44100, -16, 2 , 512) #Configurando o som
pygame.init() #Iniciar o pygame
clock = pygame.time.Clock() #FPS

# Configuração da tela do jogo
largura_tela = 1280
altura_tela = 960
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pyhtonball") #Nome

# Configurando tamanhos de bola, jogador1 e jogador2
bola = pygame.Rect(largura_tela/2 - 15 , altura_tela/2 - 15 , 30 , 30)
jogador = pygame.Rect(largura_tela - 20 , altura_tela/2 - 70 , 10 , 140)
oponente = pygame.Rect(10, altura_tela/2 - 70 , 10 , 140)

# Cores do jogo
cor_oponente = pygame.Color("red")
vermelho_claro = (139, 0, 0, 255)

cor_jogador = pygame.Color("blue")
azul_escuro = (0, 0, 255, 255)

cor_bola = pygame.Color("lawngreen")
verde_claro = (124, 252, 0, 255)

cor_tela = pygame.Color("black")

cor_linha = pygame.Color("white")
branco = (255, 255, 255, 255)
preto = (0, 0, 0)

# Variáveis do jogo
velocidade_bola_x = 3 * random.choice((1,-1))
velocidade_bola_y = 3 * random.choice((1,-1))
velocidade_jogador = 0
velocidade_oponente = 10.5
ball_speed = 5.5
game_over = False

# Variáveis de texto
score_jogador = 0
score_oponente = 0
fonte_jogo = pygame.font.Font("freesansbold.ttf", 32)

# Score Timer
score_time = True

exibir_tela_inicial = True

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                velocidade_jogador += 10.5
        if evento.key  == pygame.K_UP:
            velocidade_jogador -= 10.5
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_DOWN:
                velocidade_jogador -= 10.5
        if evento.key  == pygame.K_UP:
            velocidade_jogador += 10.5  

    # Cores visuais
    tela.fill(cor_tela)
    pygame.draw.rect(tela, azul_escuro ,jogador)
    pygame.draw.rect(tela, vermelho_claro , oponente)
    pygame.draw.ellipse(tela, verde_claro, bola)    
    pygame.draw.aaline(tela, branco , (largura_tela/2,0), (largura_tela/2, altura_tela))


    texto_jogador = fonte_jogo.render(f'{score_jogador}', False, branco)
    tela.blit(texto_jogador, (660,80))

    texto_oponente = fonte_jogo.render(f'{score_oponente}', False, branco)
    tela.blit(texto_oponente, (600,80))

    # Passando para a tela final
    pygame.display.flip() 
    clock.tick(120) # frames per second (fps)