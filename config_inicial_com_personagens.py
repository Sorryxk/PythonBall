import pygame
import random
import sys

def realxbarca():
    class Player(pygame.sprite.Sprite):
        def __init__(self, image_paths, pos_x, pos_y, screen_height):
            super().__init__()
            self.sprites_up = [
                pygame.transform.scale(pygame.image.load(image_paths[0]), (120, 120)),
                pygame.transform.scale(pygame.image.load(image_paths[1]), (120, 120))
            ]
            self.sprites_down = [
                pygame.transform.scale(pygame.image.load(image_paths[2]), (120, 120)),
                pygame.transform.scale(pygame.image.load(image_paths[3]), (120, 120))
            ]
            self.sprites_kick = pygame.transform.scale(pygame.image.load(image_paths[4]), (120, 120))
            self.current_sprite = 0
            self.image = self.sprites_down[self.current_sprite]
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
            self.speed = 10
            self.last_key_pressed = None
            self.screen_height = screen_height
            self.kicking = False
            self.kick_timer = 0
            self.original_size = (120, 120)
            self.current_size = self.original_size

        def move_up(self):
            if self.rect.top > 0:
                self.last_key_pressed = pygame.K_w

        def move_down(self):
            if self.rect.bottom < self.screen_height:
                self.last_key_pressed = pygame.K_s

        def kick(self):
            self.kicking = True
            self.kick_timer = pygame.time.get_ticks()

        def stop_move_up(self):
            if self.last_key_pressed == pygame.K_w:
                self.image = self.sprites_up[0]
                self.last_key_pressed = None

        def stop_move_down(self):
            if self.last_key_pressed == pygame.K_s:
                self.image = self.sprites_down[0]
                self.last_key_pressed = None

        def update(self, score_difference):
            if score_difference >= 4:
                self.current_size = (self.original_size[0] * 0.5, self.original_size[1] * 0.5)
            else:
                self.current_size = self.original_size

            self.sprites_up = [pygame.transform.scale(sprite, self.current_size) for sprite in self.sprites_up]
            self.sprites_down = [pygame.transform.scale(sprite, self.current_size) for sprite in self.sprites_down]
            self.sprites_kick = pygame.transform.scale(self.sprites_kick, self.current_size)

            if self.last_key_pressed == pygame.K_w and self.rect.top > 0:
                self.rect.y -= self.speed
                self.current_sprite = (self.current_sprite + 1) % len(self.sprites_up)
                self.image = self.sprites_up[self.current_sprite]
            elif self.last_key_pressed == pygame.K_s and self.rect.bottom < self.screen_height:
                self.rect.y += self.speed
                self.current_sprite = (self.current_sprite + 1) % len(self.sprites_down)
                self.image = self.sprites_down[self.current_sprite]

            if self.kicking:
                self.image = self.sprites_kick
                if pygame.time.get_ticks() - self.kick_timer > 500:
                    self.kicking = False
                    if self.last_key_pressed == pygame.K_w:
                        self.image = self.sprites_up[self.current_sprite]
                    elif self.last_key_pressed == pygame.K_s:
                        self.image = self.sprites_down[self.current_sprite]

    # SETUP
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    clock = pygame.time.Clock()
    score_sound = "sons/olha-o-gol.mp3"
    background_music = "sons/Hino da UEFA Champions League - (Letra e Tradução PT-BR).mp3"
    
    largura_tela = 1250
    altura_tela = 760
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    fundo = pygame.image.load('personagens/campocerto.jpg').convert()
    pygame.display.set_caption("Pyhtonbol")

    bola_normal = pygame.image.load("personagens/bolaparada.png").convert_alpha()
    bola_normal = pygame.transform.scale(bola_normal, (40, 40))
    bola_fogo_baixo = pygame.image.load("personagens/bolafogo_baixo.png").convert_alpha()
    bola_fogo_baixo = pygame.transform.scale(bola_fogo_baixo, (40, 40))
    bola_rect = bola_normal.get_rect(center=(largura_tela/2, altura_tela/2))

    jogador_real_madrid = Player(['personagens/realmadrid_cima.png', 'personagens/realmadrid_correndo_cima_esquerda.png', 'personagens/realmadrid_baixo.png', 'personagens/realmadrid_correndo_baixo_esquerda.png', 'personagens/realmadrid_chutando_esquerda.png'], largura_tela - 120, altura_tela/2 - 70, altura_tela)
    jogador_barcelona = Player(['personagens/barcelona_cima.png', 'personagens/barcelona_correndo_cima_direita.png', 'personagens/barcelona_baixo.png', 'personagens/barcelona_correndo_baixo_direita.png', 'personagens/barcelona_chutando_direita.png'], 20, altura_tela/2 - 70, altura_tela)
    cor_bola = pygame.Color("lawngreen")
    verde_claro = (124, 252, 0, 255)

    cor_tela = pygame.Color("black")
    branco = (255, 255, 255, 255)

    preto = (0,0,0,0)

    velocidade_bola_x = 3 * random.choice((1, -1))
    velocidade_bola_y = 3 * random.choice((1, -1))
    velocidade_oponente = 10

    score_jogador_barcelona = 0
    score_jogador_real = 0
    fonte_jogo = pygame.font.Font("fontes/retro_gaming/Retro Gaming.ttf", 48)
    fonte_jogo_restart = pygame.font.Font("fontes/retro_gaming/Retro Gaming.ttf", 30)

    score_time = True
