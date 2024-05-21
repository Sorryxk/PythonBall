import pygame
import sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites_up = [
            pygame.transform.scale(pygame.image.load('personagens/barcelona_cima.png'), (50, 50)),
            pygame.transform.scale(pygame.image.load('personagens/barcelona_correndo_cima_direita.png'), (50, 50))
        ]
        self.sprites_down = [
            pygame.transform.scale(pygame.image.load('personagens/barcelona_baixo.png'), (50, 50)),
            pygame.transform.scale(pygame.image.load('personagens/barcelona_correndo_baixo_direita.png'), (50, 50))
        ]
        self.current_sprite = 0
        self.image = self.sprites_down[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.speed = 5
        self.last_key_pressed = None
        self.frame_count = 0
        self.running_frame_duration = 60  # Tempo em que o sprite de correndo é exibido

    def move_up(self):
        self.last_key_pressed = pygame.K_UP

    def move_down(self):
        self.last_key_pressed = pygame.K_DOWN

    def stop_move_up(self):
        if self.last_key_pressed == pygame.K_UP:
            self.image = self.sprites_up[0]
            self.last_key_pressed = None  # Limpa a última tecla pressionada

    def stop_move_down(self):
        if self.last_key_pressed == pygame.K_DOWN:
            self.image = self.sprites_down[0]
            self.last_key_pressed = None  # Limpa a última tecla pressionada

    def update(self):
        if self.last_key_pressed == pygame.K_UP:
            self.rect.y -= self.speed
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites_up)
            self.image = self.sprites_up[self.current_sprite]
        elif self.last_key_pressed == pygame.K_DOWN:
            self.rect.y += self.speed
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites_down)
            self.image = self.sprites_down[self.current_sprite]

# Inicialização do pygame
pygame.init()
clock = pygame.time.Clock()

# Configuração da tela do jogo
screen_width = 1600
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Criação dos sprites e grupos
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.stop_move_up()
            elif event.key == pygame.K_DOWN:
                player.stop_move_down()

    # Desenho
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(120)  # Velocidade de animação mais lenta para melhor visualização
