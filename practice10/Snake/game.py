import pygame
import random
from config import *
from db import save_score

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_block(screen, color, x, y):
    pygame.draw.rect(
        screen,
        color,
        [
            SIZE_BLOCK + y * SIZE_BLOCK,
            HEADER_MARGIN + SIZE_BLOCK + x * SIZE_BLOCK,
            SIZE_BLOCK - MARGIN,
            SIZE_BLOCK - MARGIN
        ]
    )

def run_game(screen, username):

    snake = [Block(9, 8), Block(9, 9), Block(9, 10)]
    dx, dy = 0, 1

    food = Block(random.randint(0, 19), random.randint(0, 19))
    bonus = None

    score = 0
    level = 1
    fps = 5
    game_over = False
    saved = False

    clock = pygame.time.Clock()

    while True:

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, (0, 0, screen.get_width(), HEADER_MARGIN))

        font = pygame.font.SysFont("Arial", 24)

        screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (20,20))
        screen.blit(font.render(f"Level: {level}", True, (255,255,255)), (20,45))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: dx,dy=-1,0
                if event.key == pygame.K_DOWN: dx,dy=1,0
                if event.key == pygame.K_LEFT: dx,dy=0,-1
                if event.key == pygame.K_RIGHT: dx,dy=0,1

        head = snake[-1]
        new_head = Block(head.x + dx, head.y + dy)

        if new_head.x < 0 or new_head.x >= COUNT_BLOCKS or new_head.y < 0 or new_head.y >= COUNT_BLOCKS:
            game_over = True

        for b in snake:
            if b.x == new_head.x and b.y == new_head.y:
                game_over = True

        snake.append(new_head)

        # FOOD
        if new_head.x == food.x and new_head.y == food.y:
            score += 1
            food = Block(random.randint(0,19), random.randint(0,19))

            if score % 5 == 0:
                level += 1
                fps += 1

                bonus = Block(random.randint(0,19), random.randint(0,19))
        elif bonus and new_head.x == bonus.x and new_head.y == bonus.y:
            score += 2
            bonus = None
        else:
            snake.pop(0)

        # GRID
        for r in range(COUNT_BLOCKS):
            for c in range(COUNT_BLOCKS):
                color = BLUE if (r+c)%2==0 else WHITE
                pygame.draw.rect(screen,color,(SIZE_BLOCK+c*SIZE_BLOCK,HEADER_MARGIN+SIZE_BLOCK+r*SIZE_BLOCK,SIZE_BLOCK,SIZE_BLOCK))

        # SNAKE
        for i,b in enumerate(snake):
            draw_block(screen, (0,255,120) if i==len(snake)-1 else SNAKE_COLOR, b.x, b.y)

        draw_block(screen, FOOD_COLOR, food.x, food.y)

        if bonus:
            draw_block(screen, BONUS_COLOR, bonus.x, bonus.y)

        # GAME OVER
        if game_over:
            if not saved:
                save_score(username, score, level)
                saved = True

            font2 = pygame.font.SysFont("Arial", 50)
            screen.blit(font2.render("GAME OVER", True, (255,0,0)), (120,300))

        pygame.display.flip()
        clock.tick(fps)