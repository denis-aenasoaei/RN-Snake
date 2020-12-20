import GLOBALS as g
import pygame
from Snake import Snake
from Food import Food

def init_grid():
    grid = []
    for i in range(g.grid_size):
        grid.append([])
        for j in range(g.grid_size):
            grid[i].append(-1)
    return grid


def drawGrid(surface):
    for y in range(0, int(g.grid_size)):
        for x in range(0, int(g.grid_size)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*g.block_width, y*g.block_height), (g.block_width, g.block_height))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x * g.block_width, y * g.block_height), (g.block_width, g.block_height))
                pygame.draw.rect(surface, (84, 194, 205), rr)


def main():
    grid = init_grid()
    snake = Snake(grid)
    food = Food()

    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((g.screen_width, g.screen_height), flags=pygame.SCALED, depth=32, vsync=True)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)


    food.randomize_position(grid)
    myfont = pygame.font.SysFont("monospace",16)
    snake.draw(surface)
    while True:
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        if not snake.move(grid):
            grid = init_grid()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position(grid)
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

main()