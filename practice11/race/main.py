import pygame
import random
import os

pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Пути
car_path = os.path.join(BASE_DIR, "resources", "player.png")
road_path = os.path.join(BASE_DIR, "resources", "road.png")
coin_path = os.path.join(BASE_DIR, "resources", "coin.png")
coin2_path = os.path.join(BASE_DIR, "resources", "coin2.png")
enemy_path = os.path.join(BASE_DIR, "resources", "enemy.png")

bg_music_path = os.path.join(BASE_DIR, "resources", "background.wav")
crash_sound_path = os.path.join(BASE_DIR, "resources", "crash.wav")

# Загрузка изображений
car_img = pygame.image.load(car_path)
road_img = pygame.image.load(road_path)
coin_img = pygame.image.load(coin_path)
coin2_img = pygame.image.load(coin2_path)
enemy_img = pygame.image.load(enemy_path)

# Загрузка звуков
pygame.mixer.music.load(bg_music_path)
crash_sound = pygame.mixer.Sound(crash_sound_path)

# Размер окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гонщик")

# Масштаб
car_img = pygame.transform.scale(car_img, (50, 120))
coin_img = pygame.transform.scale(coin_img, (50, 50))
coin2_img = pygame.transform.scale(coin2_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (50, 120))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Игрок
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 120
car_speed = 5

# Монеты
coins = []
coin_speed = 5

# Враг
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -120
enemy_speed = 6

# Счёт
score = 0
font = pygame.font.SysFont(None, 36)

# Флаги
bonus_ready = False
speed_increased = False

clock = pygame.time.Clock()
running = True

# ▶️ запускаем музыку
pygame.mixer.music.play(-1)

while running:
    screen.blit(road_img, (0, 0))

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed

    # Спавн монет
    if random.randint(1, 50) == 1:
        coin_x = random.randint(0, WIDTH - 50)
        coin_y = -50

        if bonus_ready:
            coins.append([coin_x, coin_y, "bonus"])
            bonus_ready = False
        else:
            coins.append([coin_x, coin_y, "normal"])

    # Движение монет
    for coin in coins:
        coin[1] += coin_speed

    # Движение врага
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -120
        enemy_x = random.randint(0, WIDTH - 50)

    # Коллизии
    car_rect = pygame.Rect(car_x, car_y, 50, 120)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 120)

    if car_rect.colliderect(enemy_rect):
        crash_sound.play()
        pygame.time.delay(1000)  # даём звуку проиграться
        print("GAME OVER")
        running = False

    # Проверка монет
    new_coins = []
    for coin in coins:
        coin_rect = pygame.Rect(coin[0], coin[1], 50, 50)

        if car_rect.colliderect(coin_rect):
            if coin[2] == "bonus":
                score += 2
            else:
                score += 1

            # каждые 10 очков — бонус
            if score % 10 == 0:
                bonus_ready = True

            # ускорение врага при 20 очках
            if score >= 20 and not speed_increased:
                enemy_speed += 3
                speed_increased = True
        else:
            if coin[1] < HEIGHT:
                new_coins.append(coin)

    coins = new_coins

    # Рисуем монеты
    for coin in coins:
        if coin[2] == "bonus":
            screen.blit(coin2_img, (coin[0], coin[1]))
        else:
            screen.blit(coin_img, (coin[0], coin[1]))

    # Рисуем врага
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Рисуем игрока
    screen.blit(car_img, (car_x, car_y))

    # Счёт
    text = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(text, (WIDTH - 150, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()