# 15-02-23
import pygame, sys

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
TILE_SIZE = 64

GRAVITY = 0.8

LEVEL_MAP = [
    "    P             ",
    "  XXXXXX      E   ",
    " XXXXXXXXX   XXXXX",
    "             XXXXX",
    "                  ",
    "  XXX  X E X      ",
    "        XXX    XX ",
    "                  ",
]

def get_input_vector():
    keys = pygame.key.get_pressed()
    input_vector = pygame.Vector2(0, 0)
    input_vector.y = (keys[pygame.K_s] or keys[pygame.K_DOWN] - keys[pygame.K_w])
    input_vector.x = (keys[pygame.K_d] - keys[pygame.K_a])
    return input_vector


class Entity(pygame.sprite.Sprite):
    def __init__(self, **kwargs):
        super().__init__()

        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(bottomleft=self.position)

        self.direction = pygame.Vector2()
        self.velocity = pygame.Vector2(0, 0)

        self.is_on_floor = False

    def apply_gravity(self):
        self.velocity.y += GRAVITY
        self.velocity.y = min(self.velocity.y, self.terminal_velocity)
        self.rect.y += self.velocity.y
    
    def apply_horizontal_movement(self):
        if self.direction.x != 0:
            self.velocity.x += self.acceleration * self.direction.x
            self.velocity.x = min(self.velocity.x, self.max_speed)
            self.velocity.x = max(self.velocity.x, -self.max_speed)
        else:
            self.velocity.x = 0

        self.rect.x += self.velocity.x
    
    def hit_wall(self):
        pass
    
    def check_vertical_tile_collisions(self):
        for tile in Tile.instances:
            if not self.rect.colliderect(tile.rect):
                continue
            if self.velocity.y > 0:
                self.rect.bottom = tile.rect.top
                self.is_on_floor = True
            elif self.velocity.y < 0:
                self.rect.top = tile.rect.bottom
            self.velocity.y = 0

    def check_horizontal_tile_collisions(self):
        for tile in Tile.instances:
            if not self.rect.colliderect(tile.rect):
                continue
            if self.velocity.x > 0:
                self.rect.right = tile.rect.left
            elif self.velocity.x < 0:
                self.rect.left = tile.rect.right
            
            self.hit_wall()
            self.velocity.x = 0
    
    def update(self):
        self.apply_gravity()
        self.is_on_floor = False
        self.check_vertical_tile_collisions()
        self.apply_horizontal_movement()
        self.check_horizontal_tile_collisions()


class Enemy(Entity):
    instances = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instances.append(self)


class WalkingEnemy(Enemy):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.direction.x = 1
    
    def hit_wall(self):
        self.direction.x *= -1


class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.jump_speed = 18
        self.can_jump = False

    def jump(self):
        self.velocity.y = -self.jump_speed
    
    def check_enemy_collisions(self):
        for enemy in Enemy.instances:
            if self.rect.colliderect(enemy.rect):
                self.kill()

    def update(self):
        super().update()
        self.direction = get_input_vector()

        if pygame.key.get_pressed()[pygame.K_SPACE] and self.is_on_floor:
            self.jump()

        self.check_enemy_collisions()


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
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                if cell == " ": continue
                x = cell_index * TILE_SIZE
                y = SCREEN_HEIGHT - row_index * TILE_SIZE
                if cell == "X":
                    self.tiles.add(Tile((x, y), TILE_SIZE))
                elif cell == "P":
                    self.player.add(Player(size=(32, 64), color='red', position=(x, y), terminal_velocity=12, acceleration=1, max_speed=8))
                elif cell == "E":
                    self.enemies.add(WalkingEnemy(size=(32, 32), color='blue', position=(x, y), terminal_velocity=12, acceleration=0.5, max_speed=3))

    def update(self):
        self.tiles.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.enemies.update()
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
