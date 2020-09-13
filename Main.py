import pygame
import math
import random
from pygame import mixer
import time
import csv

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

#background image and sound
bg= pygame.image.load("space.jpg")
mixer.music.load("background.mp3")
mixer.music.play(-1)

#texts
over_text= pygame.font.Font('freesansbold.ttf', 70)
font = pygame.font.Font('freesansbold.ttf', 32)
font_small = pygame.font.Font('freesansbold.ttf', 25)

#PLAYER
playerimg = pygame.image.load("spaceship.png")
playerX= 370
playerY = 480
vel = 3
def player(x):
     screen.blit(playerimg , (x, playerY))

#start page
def start():
     global run
     start = True
     while start:
          for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()
                  elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                         run = True
                         start = False
                    elif event.key == pygame.K_q:
                         pygame.quit()
                         quit()
                    elif event.key == pygame.K_s:
                         shop()
          screen.fill((255,255,255))
          start_text = over_text.render("SPACE INVADERS", True, (0,0,0))
          screen.blit(start_text, (100, 50))
          obj_text_1 = font_small.render('The objective of Space Invaders, is to pan across a screen and', True, (0,0,0))
          obj_text_2 = font_small.render("shoot descending swarms of aliens, preventing them from", True, (0,0,0))
          obj_text_3 = font_small.render("reaching the bottom of the screen.", True, (0,0,0))
          screen.blit(obj_text_1, (20,200))
          screen.blit(obj_text_2, (20,230))
          screen.blit(obj_text_3, (20,260))
          instruction_text_1 = font_small.render("Instructions: ",True, (0,0,255))
          instruction_text_2 = font_small.render("1. Use Side Keys to Move Spaceship. ",True, (0,0,255))
          instruction_text_3 = font_small.render("2. Use Spacebar Key to fire Bullet. ",True, (0,0,255))
          instruction_text_4 = font_small.render("3. Press P Key to Pause the Game. ",True, (0,0,255))
          screen.blit(instruction_text_1, (20,320))
          screen.blit(instruction_text_2, (80,350))
          screen.blit(instruction_text_3, (80,380))
          screen.blit(instruction_text_4, (80,410))
          shop_text = font.render("Press S to Shop", True, (155, 105, 50))
          screen.blit(shop_text, (20, 470))
          shopcart = pygame.image.load("shop.png")
          screen.blit(shopcart , ( 273 , 477))
          game_text = font.render("Press A to Start the Game", True, (255,0,0))
          screen.blit(game_text, (180,550))
          pygame.display.update()
     
#pause
def pause():
     paused = True
     while paused:
        for event in pygame.event.get():
             global run
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                    paused = False
                    run = True
               elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
     
        screen.fill((255,255,255))
        pause_text = over_text.render("PAUSED", True, (0,0,0))
        screen.blit(pause_text, (250, 200))
        inst_text = font.render("Press C to Continue and Press Q to Quit", True, (0,0,0))
        screen.blit(inst_text, (90,300))
        pygame.display.update()

#Shop
def shop():
     buy = True
     start = False
     while buy:
          screen.fill((255,255,255))
          img1 = pygame.image.load("spaceship1 view.png")
          img2 = pygame.image.load("spaceship2 view.png")
          img3 = pygame.image.load("spaceship3 view.png")
          img4 = pygame.image.load("spaceship4 view.png")
          img5 = pygame.image.load("spaceship5 view.png")
          shop_text = font.render("Shop ", True, (255,0,0))
          screen.blit(shop_text, (10, 10))
          shopcart = pygame.image.load("shop.png")
          screen.blit(shopcart , ( 95 , 16))
          screen.blit(img1 , ( 50 , 100))
          num1_text = font_small.render("Press 1", True, (0,0,0))
          screen.blit(num1_text, (70, 230))
          screen.blit(img2 , ( 350 , 100))
          num2_text = font_small.render("Press 2", True, (0,0,0))
          screen.blit(num2_text, (370, 230))
          screen.blit(img3 , ( 650 , 100))
          num3_text = font_small.render("Press 3", True, (0,0,0))
          screen.blit(num3_text, (670, 230))
          screen.blit(img4 , ( 50 , 350))
          num4_text = font_small.render("Press 4", True, (0,0,0))
          screen.blit(num4_text, (70, 480))
          screen.blit(img5 , ( 350 , 350))
          num5_text = font_small.render("Press 5", True, (0,0,0))
          screen.blit(num5_text, (370, 480))
          inst_text = font.render("Press C to Continue", True, (255,0,0))
          screen.blit(inst_text, (250,550))
          for event in pygame.event.get():
             global run
             global playerimg
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                    buy = False
                    run = True
               elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
               elif event.key == pygame.K_1:
                    playerimg = pygame.image.load("spaceship1.png")
                    select()
                    inst_text = font.render("1st Spaceship is Selected", True, (0,0,255))
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
                    time.sleep(2)
               elif event.key == pygame.K_2:
                    playerimg = pygame.image.load("spaceship2.png")
                    select()
                    inst_text = font.render("2nd Spaceship is Selected", True, (0,0,255))
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
                    time.sleep(2)
               elif event.key == pygame.K_3:
                    playerimg = pygame.image.load("spaceship3.png")
                    select()
                    inst_text = font.render("3rd Spaceship is Selected", True, (0,0,255))
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
                    time.sleep(2)
               elif event.key == pygame.K_4:
                    playerimg = pygame.image.load("spaceship4.png")
                    select()
                    inst_text = font.render("4th Spaceship is Selected", True, (0,0,255))
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
                    time.sleep(2)
               elif event.key == pygame.K_5:
                    playerimg = pygame.image.load("spaceship5.png")
                    select()
                    inst_text = font.render("5th Spaceship is Selected", True, (0,0,255))
                    screen.blit(inst_text, (210, 50))
                    pygame.display.update()
                    time.sleep(2)
          pygame.display.update()

#select spaceship and start
def select():
     for event in pygame.event.get():
          global run
          global buy
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                    buy = False
                    run = True

#Reward
rewardimg=pygame.image.load("money.png")
reward_state="ready"
rewardX=0
rewardY=40
rewardY_change=2
def reward():
     global reward_state,rewardY_change,rewardX,rewardY
     i=random.randint(1,10)
     if i==4 :
          reward_state="fire"
          rewardY_change=random.randint(1,3)
          rewardX=random.randint(50,700)
          rewardY=40
          screen.blit(rewardimg,(rewardX,rewardY))
def reward_collision():
     global coins,reward_state,rewardY_change,rewardX,rewardY
     if collision(playerX,playerY,rewardX,rewardY):
          coins=coins+(rewardY_change)
          rewardY=0
          rewardX=0
          reward_state="ready"
          
#Enemy
enemyimg = [ ]
enemyX = [ ]
enemyY = [ ]
X_change = [ ]
Y_change = [ ]
num_enemy = 6

for i in range(num_enemy):
     enemyimg.append(pygame.image.load("enemy.png"))
     enemyX.append(random.randint(0, 735))
     enemyY.append(random.randint(40, 150))
     X_change.append(3)
     Y_change.append(40)
     
def enemy(x , y, i):
     screen.blit(enemyimg[i] , (x, y))

#bullet (Ready = can't see bulet and Fire = bullet current moving)
bulletimg = pygame.image.load("bullet.png")
bulletX= 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"
def fire (x, y):
     global bullet_state
     bullet_state = "fire"
     screen.blit(bulletimg, (x+16, y+10))

#Collision
def collision (enemyX, enemyY, bulletX , bulletY):
     distance = math.sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY)**2))
     if distance < 27:
          return True
     else:
          return False

#Score
score = 0
def show_score():
     score_v = font.render("Score: " + str(score), True, (255,255,255))
     screen.blit(score_v, (10, 10))

#Highscore
list_1=[]
highscore= {}
f=open("highscore.csv", "r")
r=csv.reader(f)
for row in r:                 #Loading the saved data of highscore
     list_1.append(row)
highscore["coins"]=list_1[0][0]
highscore["score"]=list_1[0][1]
f.close()
def show_highscore():
     highscore_v=font.render("Highscore: "+ str(highscore["score"]),True,(255,255,255))
     screen.blit(highscore_v,(280,10))
def save_highscore():         #Saves new highscore
     if int(score)>=int(highscore["score"]):
          over_text= pygame.font.Font('freesansbold.ttf', 50)
          new_highscore=over_text.render("!!! NEW HIGHSCORE !!!",True,(255,255,255))
          screen.blit(new_highscore,(150,350))
          f=open("highscore.csv","w",newline='')
          w=csv.DictWriter(f,{"coins","score"})
          w.writerow({"coins":coins,"score":score})
          f.close()
          show_highscore()
     else:
          save_coins()
          
#coins
coins=int(highscore["coins"])
def show_coins():
     coins_v = font.render("Coins: " + str(coins), True, (255,255,255))
     screen.blit(coins_v, (620, 10))
def save_coins():
     f=open("highscore.csv","w",newline='')
     w=csv.DictWriter(f,{"coins","score"})
     w.writerow({"coins":coins,"score":highscore["score"]})
     f.close()

#Game Over
def game_over_text():
     game_over = over_text.render("GAME OVER", True, (255,255,255))
     screen.blit(game_over, (200, 250))
     
#Main Loop
start()
while run:
     #RGB - Red, Green, Blue
     screen.fill((0,0,0))
     screen.blit(bg, (0,0))

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
          elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_p:
                          run = False
                          pause()
                  elif event.key == pygame.K_q:
                          pygame.quit()
                          quit()
                   
     #alternate mechanic and continous method
     keys = pygame.key.get_pressed()
     if keys[pygame.K_LEFT] and playerX>0 :
          playerX -= vel
     if keys[pygame.K_RIGHT] and playerX<736 :
          playerX += vel
     if keys[pygame.K_SPACE]:
          if bullet_state is "ready" :
               # current coordinate of spaceship
               bulletX = playerX
               fire(bulletX, bulletY)
          
     # enemy movement
     for i in range(num_enemy):
          if enemyY[i] >= 440:
               for j in range (num_enemy):
                    enemyY[j] = 2000
                    game_over_text()
                    save_highscore()
                    rewardY_change=0
               break
     
          enemyX[i] = enemyX[i] + X_change[i]
          if enemyX[i] <= 0:
               X_change[i] = 3
               enemyY[i] = enemyY[i] + Y_change[i]
          elif enemyX[i] >= 736:
               X_change[i] = -3
               enemyY[i] = enemyY[i] + Y_change[i]
          #collision check
          collisions = collision (enemyX[i] , enemyY[i] , bulletX , bulletY)
          if collisions:
               bulletY = 480
               bullet_state = "ready"
               score += 1
               reward()
               enemyX[i]= random.randint(0, 735)
               enemyY[i] = random.randint(40, 150)

          enemy(enemyX[i], enemyY[i], i)
     reward_collision()
     
     # Bullet movement
     if bullet_state is "fire":
          fire(bulletX, bulletY)
          bulletY -= bulletY_change
     if bulletY <= 0:
          bulletY = 480
          bullet_state = "ready"

     # Reward movement
     if reward_state is "fire":
          rewardY+=rewardY_change
          screen.blit(rewardimg,(rewardX,rewardY))
     if rewardY>=480:
          rewardY=0
          reward_state="ready"

     player(playerX)
     show_score()
     show_highscore()
     show_coins()
     pygame.display.update()

pygame.quit()


