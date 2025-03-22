import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Определяем размеры экрана и цвета
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Тир")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Настройки игры
target_radius = 30
score = 0
font = pygame.font.SysFont("arial", 30)
game_over = False

# Класс мишени
class Target:
    def __init__(self):
        self.x = random.randint(target_radius, screen_width - target_radius)
        self.y = random.randint(target_radius, screen_height - target_radius)
        self.color = RED

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), target_radius)

    def check_hit(self, pos):
        dist = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        return dist < target_radius

# Создание начальной мишени
target = Target()

# Главный игровой цикл
while not game_over:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if target.check_hit(pygame.mouse.get_pos()):
                score += 1
                target = Target()  # Создаём новую мишень

    # Отображение мишени
    target.draw()

    # Отображение счёта
    score_text = font.render(f"Очки: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()

    # Ожидание перед новой итерацией
    pygame.time.delay(100)

# Закрытие Pygame
pygame.quit()