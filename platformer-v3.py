# 08-02-23
import pygame, sys

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
TILE_SIZE = 64

ACCELERATION = 1
PLAYER_SPEED = 8
MAX_SPEED = 8
GRAVITY = 0.8
JUMP_SPEED = 18
TERMINAL_VELOCITY = 12

LEVEL_MAP = [
    "    P             ",
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
    input_vector.y = (keys[pygame.K_s] or keys[pygame.K_DOWN] - keys[pygame.K_w])
    input_vector.x = (keys[pygame.K_d] - keys[pygame.K_a])
    return input_vector


class Player(pygame.sprite.Sprite):
    def __init__(self, size, position):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill('red')
        self.rect = self.image.get_rect(bottomleft=position)

        self.input_vector = pygame.Vector2(0, 0)
        self.direction = pygame.Vector2(0, 0)
        self.acceleration = ACCELERATION
        self.gravity = GRAVITY
        self.terminal_velocity = TERMINAL_VELOCITY
        self.max_speed = MAX_SPEED
        self.player_speed = PLAYER_SPEED
        self.jump_speed = JUMP_SPEED

        self.can_jump = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.direction.y = min(self.direction.y, self.terminal_velocity)
        self.rect.y += self.direction.y
        self.can_jump = False

    def jump(self):
        self.direction.y = -self.jump_speed

    def apply_horizontal_movement(self):
        if self.input_vector.x != 0:
            self.direction.x += ACCELERATION * self.input_vector.x
            self.direction.x = min(self.direction.x, self.max_speed)
            self.direction.x = max(self.direction.x, -self.max_speed)
        else:
            self.direction.x = 0

        self.rect.x += self.direction.x

    def check_vertical_collisions(self):
        for tile in Tile.instances:
            if not self.rect.colliderect(tile.rect):
                continue
            if self.direction.y > 0:
                self.rect.bottom = tile.rect.top
                self.can_jump = True
            elif self.direction.y < 0:
                self.rect.top = tile.rect.bottom
            self.direction.y = 0

    def check_horizontal_collisions(self):
        for tile in Tile.instances:
            if not self.rect.colliderect(tile.rect):
                continue
            if self.direction.x > 0:
                self.rect.right = tile.rect.left
            elif self.direction.x < 0:
                self.rect.left = tile.rect.right

            self.direction.x = 0

    def update(self):
        self.input_vector = get_input_vector()
        self.apply_gravity()
        self.check_vertical_collisions()
        if pygame.key.get_pressed()[pygame.K_SPACE] and self.can_jump:
            self.jump()
        self.apply_horizontal_movement()
        self.check_horizontal_collisions()


class Tile(pygame.sprite.Sprite):
    instances = []

    def __init__(self, position, size):
        super().__init__()
        self.instances.append(self)
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(bottomleft=position)


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
                y = SCREEN_HEIGHT - row_index * TILE_SIZE
                if cell == "X":
                    self.tiles.add(Tile((x, y), TILE_SIZE))
                elif cell == "P":
                    self.player.add(Player((32, 64), (x, y)))

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
    
