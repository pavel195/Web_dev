import pygame
import random

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Определение игрового поля
WIDTH, HEIGHT = 300, 600
CELL_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Создание игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Определение фигур и их форм
tetrominoes = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]]
]


# Функция отрисовки фигур
def draw_shape(shape, x, y):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                pygame.draw.rect(screen, WHITE, (x + j * CELL_SIZE, y + i * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
