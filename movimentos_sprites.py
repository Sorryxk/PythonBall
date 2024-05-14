import pygame


class Player(pygame.sprite.Sprite): #Começando as animações
    def __init__(self, image_paths, pos_x, pos_y, screen_height): # Essa função define o começo da animação, velocidade e tamanho 
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


#Definindo em quais momentos irá ter a troca de animação

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
