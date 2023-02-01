import pygame, sys

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
TILE_SIZE = 64

LEVEL_MAP = [
    "  XXXXXX          ",
    " XXXXXXXXX   XXXXX",
    "             XXXXX",
    "                  ",
    "  XXX             ",
    "        XXX    XX ",
    "                  ",
]

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
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
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                if cell == " ": continue
                x = cell_index * TILE_SIZE
                y = SCREEN_HEIGHT - row_index  * TILE_SIZE
                if cell == "X":
                    self.tiles.add(Tile((x, y), TILE_SIZE))
    
    def update(self):
        self.tiles.draw(self.display_surface)

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
