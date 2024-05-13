import pygame
import sys
import random




# Configurando do condições iniciais com os personagens corretos
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

largura_tela = 1250
altura_tela = 760
tela = pygame.display.set_mode((largura_tela, altura_tela))
fundo = pygame.image.load('personagens/campocerto.jpg').convert()
pygame.display.set_caption("Pyhtonbol")


bola = pygame.image.load("personagens/bolaparada.png").convert_alpha()
bola = pygame.transform.scale(bola, (40, 40))
bola_rect = bola.get_rect(center=(largura_tela/2, altura_tela/2))

jogador_real_madrid = Player(['personagens/realmadrid_cima.png', 'personagens/realmadrid_correndo_cima_esquerda.png', 'personagens/realmadrid_baixo.png', 'personagens/realmadrid_correndo_baixo_direita.png', 'personagens/realmadrid_chutando_esquerda.png'], largura_tela - 120, altura_tela/2 - 70, altura_tela)
jogador_barcelona = Player(['personagens/barcelona_cima.png', 'personagens/barcelona_correndo_cima_direita.png', 'personagens/barcelona_baixo.png', 'personagens/barcelona_correndo_baixo_direita.png', 'personagens/barcelona_chutando_direita.png'], 20, altura_tela/2 - 70, altura_tela)

cor_bola = pygame.Color("lawngreen")
verde_claro = (124, 252, 0, 255)

cor_tela = pygame.Color("black")
branco = (255, 255, 255, 255)

preto = (0,0,0,0)

velocidade_bola_x = 3 * random.choice((1, -1))
velocidade_bola_y = 3 * random.choice((1, -1))
velocidade_oponente = 10

score_jogador_real_madrid = 0
score_jogador_barcelona = 0
fonte_jogo = pygame.font.Font("fontes/retro_gaming/Retro Gaming.ttf", 48)
fonte_jogo_restart = pygame.font.Font("fontes/retro_gaming/Retro Gaming.ttf", 30)

score_time = True