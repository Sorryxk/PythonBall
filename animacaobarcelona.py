import pygame
import sys

class Position:
    def _init_(self, x, y, speed):
        self.__x = x          # Encapsula detalhe de implementação
        self.__y = y          # Coordenada não é acessível diretamente
        self.__speed = speed  # Velocidade é configuração interna
        self.__direction = None  # Estado interno: up/down

    def move(self, direction):
        """Interface pública para movimento (alto nível)"""
        self.__direction = direction

    def stop(self, direction):
        """Interface pública para parar movimento"""
        if self.__direction == direction:
            self.__direction = None

    def update(self):
        """Atualização interna baseada em estado (detectada pelo tempo)"""
        if self.__direction == 'up':
            self._y -= self._speed
        elif self.__direction == 'down':
            self._y += self._speed

    def coordinates(self):
        """Interface de consulta (não expõe referência interna)"""
        return (self._x, self._y)

class Player(pygame.sprite.Sprite):
    def _init_(self, pos_x, pos_y):
        super()._init_()
        self.__position = Position(pos_x, pos_y, 5)  # Composição > Herança
        
        # Configuração de animação (detectada apenas internamente)
        self.__sprites = {
            'up': self.__load_sprites(['barcelona_cima.png', 'barcelona_correndo_cima_direita.png']),
            'down': self.__load_sprites(['barcelona_baixo.png', 'barcelona_correndo_baixo_direita.png'])
        }
        self.__current_animation = 'down'
        self.__current_frame = 0
        self.image = self.__sprites['down'][0]  # Frame inicial
        
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.__last_animation_update = pygame.time.get_ticks()

    def __load_sprites(self, filenames):
        """Detalhe interno de carregamento de arquivos"""
        return [pygame.transform.scale(pygame.image.load(f'personagens/{f}'), (50, 50)) for f in filenames]

    def handle_input(self, event):
        """Interface pública para controle (alto nível)"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.__position.move('up')
            elif event.key == pygame.K_DOWN:
                self.__position.move('down')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.__position.stop('up')
            elif event.key == pygame.K_DOWN:
                self.__position.stop('down')

    def update(self):
        """Atualização controlada por tempo (detectada internamente)"""
        now = pygame.time.get_ticks()
        
        # Atualização de posição (delegada para a classe Position)
        self.__position.update()
        self.rect.topleft = self.__position.coordinates()
        
        # Atualização de animação (detectada internamente)
        if now - self.__last_animation_update > 200:  # 200ms por frame
            self.__last_animation_update = now
            if self._position._Position_direction:  # Acesso controlado
                self._current_frame = (self._current_frame + 1) % 2
                self.image = self._sprites[self.position._Positiondirection][self._current_frame]
            else:
                self.__current_frame = 0
                self.image = self._sprites[self._current_animation][0]

# Configuração do Pygame (detectada externamente)
pygame.init()
screen = pygame.display.set_mode((1600, 960))
clock = pygame.time.Clock()

# Uso da abstração (nível alto)
player = Player(100, 100)
group = pygame.sprite.GroupSingle(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        player.handle_input(event)  # Interface simplificada
    
    screen.fill((0, 0, 0))
    group.update()     # Atualização encapsulada
    group.draw(screen) # Renderização padrão
    pygame.display.flip()
    clock.tick(120)