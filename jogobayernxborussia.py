import pygame
import sys
import random

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

jogador_borussia = Player(['personagens/borussia_cima.png', 'personagens/borussia_correndo_cima_esquerda.png', 'personagens/borussia_baixo.png', 'personagens/borussia_correndo_baixo_direita.png', 'personagens/borussia_chutando_esquerda.png'], largura_tela - 120, altura_tela/2 - 70, altura_tela)
jogador_bayern = Player(['personagens/bayern_cima.png', 'personagens/bayern_correndo_cima_direita.png', 'personagens/bayern_baixo.png', 'personagens/bayern_correndo_baixo_direita.png', 'personagens/bayern_chutando_direita.png'], 20, altura_tela/2 - 70, altura_tela)

cor_bola = pygame.Color("lawngreen")
verde_claro = (124, 252, 0, 255)

cor_tela = pygame.Color("black")
branco = (255, 255, 255, 255)

preto = (0,0,0,0)

velocidade_bola_x = 3 * random.choice((1, -1))
velocidade_bola_y = 3 * random.choice((1, -1))
velocidade_oponente = 10

score_jogador_borussia = 0
score_jogador_bayern = 0
fonte_jogo = pygame.font.Font("fontes/retro_gaming/Retro Gaming.ttf", 48)
fonte_jogo_restart = pygame.font.Font("fontes/retro_gaming/Retro Gaming.ttf", 30)

score_time = True
# Adicione uma variável global para contar as colisões
colisoes = 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                jogador_borussia.move_down()
            if evento.key == pygame.K_UP:
                jogador_borussia.move_up()
            if evento.key == pygame.K_s:
                jogador_bayern.move_down()
            if evento.key == pygame.K_w:
                jogador_bayern.move_up()
            if evento.key == pygame.K_SPACE:
                if jogador_borussia.rect.colliderect(bola_rect):
                    jogador_borussia.kick()
                if jogador_bayern.rect.colliderect(bola_rect):
                    jogador_bayern.kick()
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_DOWN:
                jogador_borussia.stop_move_down()
            if evento.key == pygame.K_UP:
                jogador_borussia.stop_move_up()
            if evento.key == pygame.K_s:
                jogador_bayern.stop_move_down()
            if evento.key == pygame.K_w:
                jogador_bayern.stop_move_up()

    bola_rect.x += velocidade_bola_x
    bola_rect.y += velocidade_bola_y
    
    if bola_rect.top <= 0 or bola_rect.bottom >= altura_tela:
        velocidade_bola_y *= -1
    
    if bola_rect.left <= 0:
        score_time = pygame.time.get_ticks()
        score_jogador_borussia += 1
        # Reiniciar o contador de colisões após um gol
        colisoes = 0
    
    if bola_rect.right >= largura_tela:
        score_time = pygame.time.get_ticks() 
        score_jogador_bayern += 1
        # Reiniciar o contador de colisões após um gol
        colisoes = 0

    if bola_rect.colliderect(jogador_borussia.rect):
        colisoes += 1
        if velocidade_bola_x > 0:  
            if abs(bola_rect.right - jogador_borussia.rect.left) < 10:
                velocidade_bola_x *= -1
        else:  
            if abs(bola_rect.left - jogador_borussia.rect.right) < 10:
                velocidade_bola_x *= -1

        if abs(bola_rect.bottom - jogador_borussia.rect.top) < 10 and velocidade_bola_y > 0:
            velocidade_bola_y *= -1
        elif abs(bola_rect.top - jogador_borussia.rect.bottom) < 10 and velocidade_bola_y < 0:
            velocidade_bola_y *= -1
        jogador_borussia.kick()

    if bola_rect.colliderect(jogador_bayern.rect):
        colisoes += 1
        if velocidade_bola_x < 0:  
            if abs(bola_rect.left - jogador_bayern.rect.right) < 10:
                velocidade_bola_x *= -1
        else:  
            if abs(bola_rect.right - jogador_bayern.rect.left) < 10:
                velocidade_bola_x *= -1

        if abs(bola_rect.bottom - jogador_bayern.rect.top) < 10 and velocidade_bola_y > 0:
            velocidade_bola_y *= -1
        elif abs(bola_rect.top - jogador_bayern.rect.bottom) < 10 and velocidade_bola_y < 0:
            velocidade_bola_y *= -1
        jogador_bayern.kick()

    jogador_borussia.update(score_jogador_borussia - score_jogador_bayern)
    jogador_bayern.update(score_jogador_bayern - score_jogador_borussia)
    
    if colisoes >= 5:
        bola_rect = bola_fogo_baixo.get_rect(center=bola_rect.center)
        velocidade_bola_x *= 1.0005
        velocidade_bola_y *= 1.0005
        
        
    else:
        bola_rect = bola_normal.get_rect(center=bola_rect.center)

    tela.blit(fundo, (0, 0))
    tela.blit(jogador_borussia.image, jogador_borussia.rect)
    tela.blit(jogador_bayern.image, jogador_bayern.rect)
    if colisoes >= 5:
        tela.blit(bola_fogo_baixo, bola_rect)
    else:
        tela.blit(bola_normal, bola_rect)
    pygame.draw.aaline(tela, branco, (largura_tela/2,0), (largura_tela/2, altura_tela))
    
    if score_jogador_borussia >= 10:
        import tela_final_borussia
        tela_final_borussia.borussia()
    elif score_jogador_bayern >= 10:
        import tela_final_bayern
        tela_final_bayern.bayern()
    if score_time:
        tempo_atual = pygame.time.get_ticks()
        bola_rect.center = (largura_tela / 2, altura_tela / 2)
        
        if tempo_atual - score_time < 700:
            numero_tres = fonte_jogo_restart.render("3", False, preto)
            tela.blit(numero_tres, (largura_tela / 2 - 10, altura_tela/2 + 20))
        if 700 < tempo_atual - score_time < 1400:
            numero_dois = fonte_jogo_restart.render("2", False, preto)
            tela.blit(numero_dois, (largura_tela / 2 - 10, altura_tela/2 + 20))
        if 1400 < tempo_atual - score_time < 2100:
            numero_um = fonte_jogo_restart.render("1", False, preto)
            tela.blit(numero_um, (largura_tela / 2 - 10, altura_tela/2 + 20))
        
        if tempo_atual - score_time < 2100:
            velocidade_bola_x, velocidade_bola_y = 0,0
        else:
            velocidade_bola_y = 7 * random.choice((1,-1))
            velocidade_bola_x = 7 *  random.choice((1,-1))
            score_time = None
        
    texto_jogador_borussia = fonte_jogo.render(f'{score_jogador_borussia}', False, preto)
    tela.blit(texto_jogador_borussia, (largura_tela // 2 +40 , 20))  # Centralizando o placar
    texto_jogador_bayern = fonte_jogo.render(f'{score_jogador_bayern}', False, preto)
    tela.blit(texto_jogador_bayern, (largura_tela // 2 - 75, 20))  # Centralizando o placar
    
    pygame.display.flip()
    clock.tick(120)