import pygame
import sys
import random
from color_palette import *
from player import MusicPlayer

pygame.init()

SIZE_BLOCK = 20
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1


size = [SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK +MARGIN*COUNT_BLOCKS,
        SIZE_BLOCK*COUNT_BLOCKS+2*SIZE_BLOCK +MARGIN*COUNT_BLOCKS+HEADER_MARGIN]


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer = pygame.time.Clock()

class SnakeBlock:
  def __init__(self, x, y):
    self.x=x
    self.y=y
    
  def is_inside(self):
    return 0<=self.x<COUNT_BLOCKS and 0<=self.y<COUNT_BLOCKS 
    

def draw_block(color, row, column):
  pygame.draw.rect(screen, color,[SIZE_BLOCK+column*SIZE_BLOCK + (column+1)*MARGIN, 
                                      HEADER_MARGIN+SIZE_BLOCK+row*SIZE_BLOCK + (row+1)*MARGIN,
                                      SIZE_BLOCK,
                                      SIZE_BLOCK])
  
def reset_game():
    global snake_blocks, food, d_row, d_col, game_over 
    
    global game_over_sound_played
    

    snake_blocks = [SnakeBlock(9,8), SnakeBlock(9,9), SnakeBlock(9,10)]

    food = SnakeBlock(
        random.randint(0, COUNT_BLOCKS - 1),
        random.randint(0, COUNT_BLOCKS - 1)
    )

    d_row = 0
    d_col = 1
    game_over = False
    
    


    music.current = 0
    music.play_loop()
    game_over_sound_played = False
  
snake_blocks = [SnakeBlock(9,8),SnakeBlock(9,9),SnakeBlock(9,10)]

food = SnakeBlock(
    random.randint(0, COUNT_BLOCKS - 1),
    random.randint(0, COUNT_BLOCKS - 1)
)

font = pygame.font.SysFont("Arial", 36)
font1 = pygame.font.SysFont("Times New Roman", 30)


d_row = 0
d_col = 1
  
speed = 10      # чем меньше — тем быстрее
counter = 0

fps=2
num =0
level=1
game_over = False
game_over_sound_played = False

music = MusicPlayer()
music.play_loop()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("Exit")
      pygame.quit()
      sys.exit()
    elif event.type ==pygame.KEYDOWN:
      if event.key == pygame.K_UP and d_col!=0:
        d_row = -1
        d_col = 0
      elif event.key == pygame.K_DOWN and d_col!=0:
        d_row = 1
        d_col = 0     
      elif event.key == pygame.K_LEFT and d_row!=0:
        d_row = 0
        d_col = -1
      elif event.key == pygame.K_RIGHT and d_row!=0:
        d_row = 0
        d_col = 1
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and game_over:
          reset_game()
          
     
      
      
  screen.fill(FRAME_COLOR)
  pygame.draw.rect(screen,HEADER_COLOR,[0,0,size[0],HEADER_MARGIN])
  
  text3=font1.render("Total:", True,(255,255,255))
  rect3 = text3.get_rect(center=(50,20))
  screen.blit(text3, rect3)
  
  text4=font1.render(str(num), True,(255,255,255))
  rect4 = text4.get_rect(center=(100,20))
  screen.blit(text4, rect4)
  
  text5=font1.render("Level:", True,(255,255,255))
  rect5 = text5.get_rect(center=(55,50))
  screen.blit(text5, rect5)
  
  text6=font1.render(str(level), True,(255,255,255))
  rect6 = text6.get_rect(center=(100,50))
  screen.blit(text6, rect6)
  
  for row in range(COUNT_BLOCKS):
    for column in range(COUNT_BLOCKS):
      if (row+column)%2==0:
        color = BLUE
      else:
        color = WHITE
      
      draw_block(color,row,column)
      
  draw_block(FOOD_COLOR, food.x, food.y)
      
      
      
      

  head = snake_blocks[-1]
  
  if not head.is_inside():
    game_over = True
    fps=2
    num=0
    level=1
      
  for block in snake_blocks:
    draw_block(SNAKE_COLOR,block.x,block.y)
    
  new_head = SnakeBlock(head.x + d_row,head.y + d_col)
  
  
  for block in snake_blocks[:-1]:
    if block.x == new_head.x and block.y == new_head.y:
        game_over=True
        fps=2
        num=0
        level=1
  
  if not game_over:
    snake_blocks.append(new_head)
    if new_head.x==food.x and new_head.y==food.y:
      fps+=0.1
      food = SnakeBlock(
          random.randint(0, COUNT_BLOCKS - 1),
          random.randint(0, COUNT_BLOCKS - 1)
      )
      num+=1
      if num%10==0:
        level+=1
        fps+=2
      
    else:
      snake_blocks.pop(0)
    

    
     
  if game_over:
    if not game_over_sound_played:
        music.game_over()
        game_over_sound_played = True
    
    text1 = font.render("GAME OVER", True, (0, 0, 0))
    text2 = font.render("Press ENTER to restart", True, (0, 0, 0))

    screen.blit(text1, (120, size[1] // 2 - 20))
    screen.blit(text2, (50, size[1] // 2 + 20)) 
  
  pygame.display.flip()
  timer.tick(fps)