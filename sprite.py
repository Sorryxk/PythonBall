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