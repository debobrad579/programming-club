import pygame, sys

TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PLAYER_SPEED = 8
MAX_SPEED = 8
ACCELERATION = 1
FRICTION = 0.5
GRAVITY = 0.8
TERMINAL_VELOCITY = 40
JUMP_SPEED = -12

LEVEL_MAP = [
    "      P           ",
    "  XXXXXX          ",
    " XXXXXXXXX   XXXXX",
    "             XXXXX",
    "                  ",
    "  XXX             ",
    "        XXX    XX ",
    "                  ",
]

def get_input_vector():
    keys = pygame.key.get_pressed()
    input_vector = pygame.Vector2(0, 0)
    input_vector.x = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
    input_vector.y = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
    return input_vector

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(bottomleft=position)

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # Surface
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(bottomleft=position)

        # Movement
        self.input_vector = pygame.Vector2(0, 0)
        self.direction = pygame.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.acceleration = ACCELERATION
        self.max_speed = MAX_SPEED
        self.gravity = GRAVITY
        self.terminal_velocity = TERMINAL_VELOCITY
        self.jump_speed = JUMP_SPEED
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.direction.y = min(self.direction.y, self.terminal_velocity)
        self.rect.y += self.direction.y
    
    def update(self):
        self.input_vector = get_input_vector()
        self.apply_gravity()

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.initialize_level(level_data)
    
    def initialize_level(self, layout):
        layout.reverse()
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                if cell == " ": continue
                x = cell_index * TILE_SIZE
                y = SCREEN_HEIGHT - row_index  * TILE_SIZE
                if cell == "X":
                    self.tiles.add(Tile((x, y), TILE_SIZE))
                elif cell == "P":
                    self.player.add(Player((x, y)))
    
    def update(self):
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.update()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(LEVEL_MAP, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
    screen.fill('black')
    level.update()

    pygame.display.update()
    clock.tick(60)
