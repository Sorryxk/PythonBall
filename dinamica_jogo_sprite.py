import pygame
class Player(pygame.sprite.Sprite):
    def _init_(self, image_paths, pos_x, pos_y, screen_height):
        super()._init_()
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
#Mudando a dinâmica do jogo conforme o placar atualiza
    def update(self, score_difference): #diminui o personagen pela metade
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