import pygame
import math
import random
from pygame import mixer
import csv
import pyttsx3
import os

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
#Title and Icon
pygame.display.set_caption("Marvel Invaders")
icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)

#background image and sound
bg= pygame.image.load("space.jpg")
start_bg = pygame.image.load("start_page.jpg")
shop_bg = pygame.image.load("shop_page.jpg")
help_bg = pygame.image.load("help_page.jpg")
pause_bg = pygame.image.load("paused_page.jpeg")
over_bg = pygame.image.load("game_over_page.jpeg")
mixer.music.load("start_song.mp3")
mixer.music.play(loops=-1,start=7.6)

#texts
over_text= pygame.font.Font('freesansbold.ttf', 70)
font = pygame.font.Font('freesansbold.ttf', 32)
font_small = pygame.font.Font('freesansbold.ttf', 25)

#PLAYER
playerimg = pygame.image.load("spaceship.png")
playerX= 370
playerY = 480
vel = 3
right_limit=735
left_limit=0
def player(x):
     screen.blit(playerimg , (x, playerY))

#start page
def start():
     global run
     start = True
     count = 1
     while start:
          for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()
                  elif event.type == pygame.MOUSEBUTTONUP:
                       pos = pygame.mouse.get_pos() 
                  elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                         run = True
                         start = False
                         mixer.music.fadeout(4000)
                    elif event.key == pygame.K_q:
                         pygame.quit()
                         quit()
                    elif event.key == pygame.K_s:
                         shop()
                    elif event.key == pygame.K_h:
                         help_page()
          screen.blit(start_bg, (0,0))
          if count % 2 == 0 or count % 3 == 0 or count % 5 == 0 or count % 7 == 0 or count % 11 == 0 or count % 13 == 0:
               game_text = font.render("Press A to Start the Game", True, (0,0,255))
          else:
               game_text = font.render("Press A to Start the Game", True, (255,0,0))
          screen.blit(game_text, (205,550))
          pygame.display.update()
          count +=0.5
     
#pause
def pause():
     paused = True
     count = 1
     while paused:
        for event in pygame.event.get():
             global run
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                    mixer.music.unpause()
                    paused = False
                    run = True
                    #speaker("Continue")
               elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.blit(pause_bg, (0,0))            
        pygame.display.update()
        if count ==2 :
             speaker("paused")
        count += 1

#help_page
def help_page():
     start = False
     help_status =True
     while help_status:
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                    help_status = False
                    start = True
               elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
          
          screen.blit(help_bg, (0,0))
          inst_text = font.render("Press C to Continue", True, (255,0,0))
          screen.blit(inst_text, (230,560))
          pygame.display.update()
     
#Shop_Page
def shop():
     global select_status,t
     buy = True
     pressed="0"
     start = False
     select_status=False
     while buy:
          screen.blit(shop_bg, (0,0))
          img1 = pygame.image.load("spaceship1 view.png")
          img2 = pygame.image.load("spaceship2 view.png")
          img3 = pygame.image.load("spaceship3 view.png")
          img4 = pygame.image.load("spaceship4 view.png")
          img5 = pygame.image.load("spaceship5 view.png")
          show_coins()
          screen.blit(img1 , ( 50 , 100))
          num1_text = font_small.render("Press 1", True, (255,255,255))
          screen.blit(num1_text, (70, 230))
          screen.blit(img2 , ( 350 , 100))
          num2_text = font_small.render("Press 2", True, (255,255,255))
          screen.blit(num2_text, (370, 230))
          screen.blit(img3 , ( 650 , 100))
          num3_text = font_small.render("Press 3", True, (255,255,255))
          screen.blit(num3_text, (670, 230))
          screen.blit(img4 , ( 50 , 350))
          num4_text = font_small.render("Press 4", True, (255,255,255))
          screen.blit(num4_text, (70, 480))
          screen.blit(img5 , ( 350 , 350))
          num5_text = font_small.render("Press 5", True, (255,255,255))
          screen.blit(num5_text, (370, 480))
          inst_text2 = font.render("Press C to Continue", True, (255,0,0))
          screen.blit(inst_text2, (220,545))
          for event in pygame.event.get():
             global run
             global playerimg
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.MOUSEBUTTONUP:
                  pos = pygame.mouse.get_pos()
                  t=pygame.key.get_pressed()
                  if img1.get_rect(topleft=(50,100)).collidepoint(pos):
                       pressed="1"
                  if img2.get_rect(topleft=(350,100)).collidepoint(pos):
                       pressed="2"
                  if img3.get_rect(topleft=(650,100)).collidepoint(pos):
                       pressed="3"
                  if img4.get_rect(topleft=(50,350)).collidepoint(pos):
                       pressed="4"
                  if img5.get_rect(topleft=(350,350)).collidepoint(pos):
                       pressed="5"
                  i=pressed
                  select(pressed)
                  screen.blit(inst_text,(210 ,50))
                  pygame.display.update()
             keys=pygame.key.get_pressed()        
             if keys[pygame.K_q]:
                  pygame.quit()
                  quit()
             elif keys[pygame.K_1]:
                 i="1"
                 select("1")
                 screen.blit(inst_text, (210, 50))
                 pygame.display.update()
             elif keys[pygame.K_2]:
                 i="2"
                 select("2")
                 screen.blit(inst_text, (210, 50))
                 pygame.display.update()
             elif keys[pygame.K_3]:
                 i="3"
                 select("3")
                 screen.blit(inst_text, (210, 50))
                 pygame.display.update()
             elif keys[pygame.K_4]:
                 i="4"
                 select(i)
                 screen.blit(inst_text, (210, 50))
                 pygame.display.update()
             elif keys[pygame.K_5]:
                 i="5"
                 select("5")
                 screen.blit(inst_text, (210, 50))
                 pygame.display.update()
             elif keys[pygame.K_c]:
                 buy = False
                 run = True
             elif select_status:
                 t=pygame.key.get_pressed()
                 select(i)       
          try:
               screen.blit(inst_text,(210,50))
               pygame.display.update()
          except NameError:
               None
          pygame.display.update()
          
#select spaceship and start
def select(i):
     global select_status
     global run,buy,coins
     global inst_text
     global t,playerimg
     select_status=True
     if i in ships["bought"]:
          inst_text = font.render("Press D to select spaceship "+str(i), True, (0,255,0))
          global run
          global buy
          try:
               if t[pygame.K_d]:
                    playerimg = pygame.image.load("spaceship"+str(i)+".png")
                    inst_text = font.render(str(i)+"th spaceship selected", True, (0,255,0))
                    screen.blit(inst_text,(210,50))
                    pygame.display.update()
                    ships["selected"]=i
                    buy = False
                    run= True
                    select_status=False
                    t=0
          except NameError or TypeError:
               None
     elif i not in ships["bought"]:
          cost=str((int(i))*100)
          inst_text=font.render("Press B to buy it  Price:"+cost, True,(0,255,0))
          screen.blit(inst_text, (210, 50))
          pygame.display.update()
          try:
               if t[pygame.K_b]:
                    if coins>=int(cost):
                         coins=coins-int(cost)
                         ships["bought"]=ships["bought"]+str(i)
                         ships["selected"]=str(i)
                         save_ships()
                         playerimg = pygame.image.load("spaceship"+str(i)+".png")
                         buy=False
                         run=True
                         select_status=False
                         t=0
                    else:
                         inst_text=font.render("Not Enough Coins", True,(0,255,0))
                         screen.blit(inst_text, (210, 50))
                         pygame.display.update()
                         select_status=False
                         t=0
          except NameError or TypeError:
               None

#speaker
def speaker(n):
     speaker = pyttsx3.init()
     rate = speaker.getProperty('rate')
     speaker.setProperty('rate', rate-50)
     speaker.say(n)
     speaker.runAndWait()
     
#loading last selected spaceship and bought spaceships
f=open("shops.csv")
ships={}
list_2=[]
r=csv.reader(f)
for row in r:
     list_2.append(row)
ships["selected"]=list_2[0][0]
ships["bought"]=list_2[0][1]
def save_ships():
     f=open("shops.csv","w")
     w=csv.DictWriter(f,{"selected","bought"})
     w.writerow({"selected":ships["selected"],"bought":ships["bought"]})
     
#Reward
rewardimg=[pygame.image.load("dynamite.png"),pygame.image.load("money.png"),pygame.image.load("shotgun.png"),pygame.image.load("machine gun.png")]
reward_state=["ready","ready","ready","ready"]
rewardX=[0,0,0,0]
rewardY=[40,40,40,40]
rewardY_change=[2,2,2,2]
def reward():
     global reward_state,rewardY_change,rewardX,rewardY
     i=random.randint(1,1000)
     if i<4 and reward_state[0]=="ready":
          reward_state[0]="fire"
          rewardY_change[0]=1
          rewardX[0]=random.randint(50,700)
          rewardY[0]=40
          screen.blit(rewardimg[0],(rewardX[0],rewardY[0]))
     elif  (i>100 and i<200) and reward_state[1]=="ready":
          reward_state[1]="fire"
          rewardY_change[1]=random.randint(1,3)
          rewardX[1]=random.randint(50,700)
          rewardY[1]=40
          screen.blit(rewardimg[1],(rewardX[1],rewardY[1]))
     elif i<10 and reward_state[2]=="ready":
          reward_state[2]="fire"
          rewardY_change[2]=2
          rewardX[2]=random.randint(50,700)
          rewardY[2]=40
          screen.blit(rewardimg[2],(rewardX[2],rewardY[2]))
     elif i<16 and reward_state[3]=="ready":
          reward_state[3]="fire"
          rewardY_change[3]=2
          rewardX[3]=random.randint(50,700)
          rewardY[3]=40
          screen.blit(rewardimg[3],(rewardX[3],rewardY[3]))
def reward_collision():
     global coins,reward_state,rewardY_change,rewardX,rewardY
     if collision(playerX,playerY,rewardX[1],rewardY[1]):
          coins=coins+(rewardY_change[1])
          rewardY[1]=0
          rewardX[1]=0
          reward_state[1]="ready"
     elif collision(playerX,playerY,rewardX[0],rewardY[0]):
          power_state[0]+=1
          rewardY[0]=0
          rewardX[0]=0
          reward_state[0]="ready"
     elif collision(playerX,playerY,rewardX[2],rewardY[2]):
          power_state[1]+=1
          rewardY[2]=0
          rewardX[2]=0
          reward_state[2]="ready"
     elif collision(playerX,playerY,rewardX[3],rewardY[3]):
          power_state[2]+=1
          rewardY[3]=0
          rewardX[3]=0
          reward_state[3]="ready"
          
#Blast power
num_enemy=6
power_state=[1,1,1]
blast_state=0
blastimg=pygame.image.load("blast.png")
blastbutton1= pygame.image.load("blastbutton1.png")
blastbutton2= pygame.image.load("blastbutton2.png")
def blast():
     global power_state,score,blast_state,playerX,playerY,blastimg
     power_state[0]=power_state[0]-1
     blast_state=40
     for i in range(len(enemyX)):
          if enemyY[i]>350:
               score += 1
               enemyX[i]= random.randint(0, 735)
               enemyY[i] = random.randint(40, 150)
               enemy(enemyX[i],enemyY[i],i)

#smg power
smg_state=0
smgbutton1= pygame.image.load("smgbutton1.png")
smgbutton2= pygame.image.load("smgbutton2.png")
def smg():
     global power_state,bulletY_change,smg_state,bulletimg1,bulletimg2,bulletimg3,bulletimg
     smg_state=1000
     power_state[2]=power_state[2]-1
     bulletY_change=2*bulletY_change
     bulletimg1 = pygame.image.load("smg.png")
     bulletimg3 = pygame.image.load("smg.png")
     bulletimg2 = pygame.image.load("smg.png")
     bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
def not_smg():
     global power_state,bulletY_change,bulletimg1,bulletimg2,bulletimg3,bulletimg
     bulletY_change=10
     bulletimg1 = pygame.image.load("bullet.png")
     bulletimg2 = pygame.image.load("bullet.png")
     bulletimg3 = pygame.image.load("bullet.png")
     bulletimg=["",bulletimg1,bulletimg2,bulletimg3]

#shotgun
shotgun_state=0
shotgunbutton1= pygame.image.load("shotgunbutton1.png")
shotgunbutton2= pygame.image.load("shotgunbutton2.png")
bulletimg2 = pygame.image.load("bullet.png")
bulletimg3 = pygame.image.load("bullet.png")
def shotgun():
     global power_state,shotgun_state
     power_state[1]=power_state[1]-1
     shotgun_state=1000

#bot
AI_space=False
AI_right=False
AI_left=False
autopilot_state=0
autopilot_time=100000
button_press=0
def AI():
     global enemyY,enemyX,playerY,playerX,power_state,X_change,Y_change,vel,bulletY_change,AI_space,AI_left,AI_right
     for i in range(len(enemyX)):
          if enemyY[i]==max(enemyY):
               enemy_future_X=enemyX[i]+(X_change[i]*(playerY-enemyY[i]))/bulletY_change
               if collision(playerX,enemyY[i],enemy_future_X,enemyY[i]):
                    AI_space=True
               elif (enemyX[i]>playerX+bulletY_change) and playerX<600:
                    AI_right=True
               elif (enemyX[i]<playerX-bulletY_change) and playerX>100:
                    AI_left=True
                    
#thanos
stones_img={"soul":pygame.image.load("soul stone dead.png"),"black":pygame.image.load("black_stone.png"),"power":pygame.image.load("power stone dead.png"),"space":pygame.image.load("space stone dead.png"),"time":pygame.image.load("time stone dead.png"),"reality":pygame.image.load("reality stone dead.png"),"mind":pygame.image.load("mind stone dead.png")}
stones_status={"soul":-1,"power":-1,"space":-1,"time":-1,"reality":-1,"mind":-1,"black":-2}
stones_life={"soul":300,"power":100,"space":100,"time":100,"reality":100,"mind":200,"black":0}
stones_X={"soul":400,"power":575,"space":225,"time":750,"reality":50,"mind":400,"black":-50}
stones_X2={"soul":400,"power":575,"space":225,"time":750,"reality":50,"mind":400,"black":400}
stones_Y={"soul":50,"power":150,"space":150,"time":150,"reality":150,"mind":150,"black":-50}
stones_Y2={"soul":50,"power":150,"space":150,"time":150,"reality":150,"mind":150,"black":250}
laserimg=pygame.image.load("laser.png")
laserimg=pygame.transform.scale(laserimg,(10,470))
for i in stones_img.keys():
     stones_img[i]=pygame.transform.scale(stones_img[i],(40,40))
def stones_display():
     if stones_status["soul"]!=-2:
          screen.blit(stones_img["soul"], (stones_X["soul"],stones_Y["soul"]))
     if stones_status["mind"]!=-2:
          screen.blit(stones_img["mind"], (stones_X["mind"],stones_Y["mind"]))
     if stones_status["power"]!=-2:
          screen.blit(stones_img["power"], (stones_X["power"],stones_Y["power"]))
     if stones_status["time"]!=-2:
          screen.blit(stones_img["time"], (stones_X["time"],stones_Y["time"]))
     if stones_status["space"]!=-2:
          screen.blit(stones_img["space"], (stones_X["space"],stones_Y["space"]))
     if stones_status["black"]!=-2:
          screen.blit(stones_img["black"], (stones_X["black"],stones_Y["black"]))
     if stones_status["reality"]!=-2:
          screen.blit(stones_img["reality"], (stones_X["reality"],stones_Y["reality"]))
stone_trigger_state=2500
def stone_trigger():
     global stones_status,stones_life,stone_trigger_state,stones_X,stones_Y
     a=True
     c=["soul","power","time","reality","mind","space"]
     for i in stones_img.keys():
          if i=="black":
               continue
          if stones_status[i]==-2:
               c.remove(i)
          elif stones_status[i]!=-1:
               a=False
     if c==[]:
          stone_trigger_state=4000
          stones_status={"soul":-1,"power":-1,"space":-1,"time":-1,"reality":-1,"mind":-1,"black":-2}
          stones_life={"soul":300,"power":100,"space":100,"time":100,"reality":100,"mind":200,"black":0}
          stones_X={"soul":400,"power":575,"space":225,"time":750,"reality":50,"mind":400,"black":-50}
          stones_Y={"soul":50,"power":150,"space":150,"time":150,"reality":150,"mind":150,"black":-50}
     elif a and score>10:
          d=random.choice(c)
          if d=="soul":
               soulstone()
          elif d=="power":
               powerstone()
          elif d=="space":
               spacestone()
          elif d=="time":
               timestone()
          elif d=="reality":
               realitystone()
          elif d=="mind":
               mindstone()
     
                    
def timestone():
     global stones_img,stones_status,bulletY_change,vel,stone_trigger_state
     stones_img["time"]=pygame.image.load("time stone.png")
     stones_img["time"]=pygame.transform.scale(stones_img["time"],(40,40))
     stones_status["time"]=2500
     stone_trigger_state=3500
     mixer.music.load("time_song.mp3")
     mixer.music.play(loops=1)
     vel=vel/2
     bulletY_change=bulletY_change/2
     
def realitystone():
     global stones_img,stones_status,bulletY_change,bulletimg1,bulletimg,stone_trigger_state,bullet_limit
     stones_img["reality"]=pygame.image.load("reality stone.png")
     stones_img["reality"]=pygame.transform.scale(stones_img["reality"],(40,40))
     stones_status["reality"]=2400
     stone_trigger_state=3400
     bulletimg1=pygame.image.load("bubbles.png")
     bulletimg2=pygame.image.load("bubbles.png")
     bulletimg3=pygame.image.load("bubbles.png")
     mixer.music.load("reality_song.mp3")
     mixer.music.play(loops=1)
     bulletimg1=pygame.transform.scale(bulletimg1,(40,40))
     bulletimg2=pygame.transform.scale(bulletimg2,(40,40))
     bulletimg3=pygame.transform.scale(bulletimg3,(40,40))
     bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
     bulletY_change=1
     bullet_limit=360
list_soul=[]   
def soulstone():
     global stones_img,stones_status,stone_trigger_state,stones_life,stones_X,stones_Y,stones_X2,stones_Y2,list_soul
     list_soul=[]
     for i in stones_img.keys():
          if stones_status[i]==-2 and i!="soul" and i!="black":
               list_soul.append(i)
     if len(list_soul)>0:
          stones_img["soul"]=pygame.image.load("soul stone.png")
          stones_img["soul"]=pygame.transform.scale(stones_img["soul"],(40,40))
          stones_status["soul"]=2600
          mixer.music.load("soul_song.mp3")
          mixer.music.play(loops=1)
          stones_life["soul"]=300
          stone_trigger_state=3600
          
def mindstone():
     global stones_img,stones_status,stone_trigger_state,left_limit,right_limit
     stones_img["mind"]=pygame.image.load("mind stone.png")
     stones_img["mind"]=pygame.transform.scale(stones_img["mind"],(40,40))
     stones_status["mind"]=4000
     mixer.music.load("mind_song.mp3")
     mixer.music.play(loops=1,start=10.0)
     stone_trigger_state=5000
     screen.blit(laserimg,(400,150))
     if playerX>=400:
          left_limit=424
     elif playerX<400:
          right_limit=350

def spacestone():
      global stones_img,stones_status,stone_trigger_state
      stones_img["space"]=pygame.image.load("space stone.png")
      stones_img["space"]=pygame.transform.scale(stones_img["space"],(40,40))
      stones_status["space"]=2500
      mixer.music.load("space_song.mp3")
      mixer.music.play(loops=1)
      stone_trigger_state=3500
      for i in range(num_enemy):
          enemyimg[i]=pygame.image.load("ufo.png")
          if X_change[i]==3:
               X_change[i]=4
          elif X_change[i]==-3:
               X_change[i]=-4
          
def teleport():
     global enemyX,enemyY
     a=random.randint(1,200)
     for i in range(num_enemy):
          if a==i:
               if enemyY[i]<=350:
                    enemyX[i]=735-enemyX[i]
                    enemyY[i]=enemyY[i]+40
                    
def powerstone():
      global stones_img,stones_status,stone_trigger_state
      stones_img["power"]=pygame.image.load("power stone.png")
      stones_img["power"]=pygame.transform.scale(stones_img["power"],(40,40))
      stones_status["power"]=3500
      mixer.music.load("power_song.mp3")
      mixer.music.play(loops=1,start=65.0)
      stone_trigger_state=4500
      for i in range(num_enemy):
          enemyimg[i]=pygame.image.load("power_ufo.png")
          if X_change[i]==3:
               X_change[i]=4
          elif X_change[i]==-3:
               X_change[i]=-4
power_blast_state=[0,0,0,0,0,0]

def power_shield():
     for i in range(num_enemy):
          for j in range(1,4):
                distance = math.sqrt(((enemyX[i] - bulletX[j])**2) + ((enemyY[i] - bulletY[j])**2))
                if distance < 50:
                     a=random.randint(1,100)
                     if a<20:
                          bulletY[j] = 480
                          bullet_state[j] = "ready"
                          power_blast_state[i] = 80
                          
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
     if power_blast_state[i]>0:
          power_shield_img=pygame.image.load("power_blast.png")
          screen.blit(power_shield_img, (x-30,y-30))
          power_blast_state[i]-=1
          
#bullet (Ready = can't see bulet and Fire = bullet current moving)
bulletimg1 = pygame.image.load("bullet.png")
bulletX=[-200,-200,-200,-200]
bulletY =[-200,-200,-200,-200]
bulletY_change = 10
bullet_limit=0
bullet_state =["ready","ready","ready","ready"]
bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
def fire (x, y,p,i):
     global bullet_state
     bullet_state[i] = "fire"
     screen.blit(p, (x+16, y+10))

#Collision
def collision (enemyX, enemyY, bulletX , bulletY):
     distance = math.sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY)**2))
     if distance < 27:
          return True
     else:
          return False
def smg_collision (enemyX, enemyY, bulletX , bulletY):
     distance = math.sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY)**2))
     if distance < 54:
          return True
     else:
          return False

#Score
score = 0
def show_score():
     score_v = font.render("Score: " + str(score), True, (255,255,255))
     screen.blit(score_v, (10, 10))

def power_score():
     blast_score = font.render(str(power_state[0]), True, (255,0,0))
     shotgun_score = font.render(str(power_state[1]), True, (255,0,0))
     smg_score = font.render(str(power_state[2]), True, (255,0,0))
     screen.blit(blast_score, (314, 558))
     screen.blit(shotgun_score, (64, 558))
     screen.blit(smg_score, (564, 558))

#Highscore
list_1=[]
highscore= {}
f=open("highscore.csv", "r")
r=csv.reader(f)
for row in r:                 #Loading the saved data of highscore
     list_1.append(row)
highscore["score"]=list_1[0][0]
f.close()
f=open("coins.csv","r")
r=csv.reader(f)
list_1=[]
for row in r:
     list_1.append(row)
highscore["coins"]=list_1[0][0]
f.close()
def show_highscore():
     highscore_v=font.render("Highscore: "+ str(highscore["score"]),True,(255,255,255))
     screen.blit(highscore_v,(280,10))
def save_highscore():         #Saves new highscore
     if int(score)>=int(highscore["score"]):
          over_text= pygame.font.Font('freesansbold.ttf', 50)
          new_highscore=over_text.render("!! NEW HIGHSCORE !!",True,(255,255,255))
          screen.blit(new_highscore,(20,460))
          speaker("Congratulations! New High Score")
          f=open("highscore.csv","w",newline='')
          w=csv.DictWriter(f,{"score"})
          w.writerow({"score":score})
          f.close()
          save_coins()
          show_highscore()
     else:
          save_coins()
          
#coins
coins=int(highscore["coins"])
def show_coins():
     coins_v = font.render("Coins: " + str(coins), True, (255,255,255))
     screen.blit(coins_v, (610, 10))
def save_coins():
     f=open("coins.csv","w",newline='')
     w=csv.DictWriter(f,{"coins"})
     w.writerow({"coins":coins})
     f.close()

#Game Over
animate_over=-1
def game_over_animation():
     global animate_over,enemyY,Y_change
     animate_over=500-min(enemyY)
     for i in range(num_enemy):
          Y_change[i]=1
     
def game_over():
     global run
     mixer.music.load("end_song.mp3")
     mixer.music.play(-1)
     run = False
     over = True
     while over:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_y:
                    pygame.quit()
                    os.system("#Main.py")
               elif event.key == pygame.K_n:
                    pygame.quit()
                    quit()
     
        screen.blit(over_bg, (0,0))
        pygame.display.update()
     
#Main Loop
start()
while run:
     #RGB - Red, Green, Blue
     screen.fill((0,0,0))
     screen.blit(bg, (0,0))
     screen.blit(shotgunbutton1, (50, 555))
     screen.blit(blastbutton1, (300, 555))
     screen.blit(smgbutton1, (550, 555))
     pygame.draw.line(screen,(240,0,0),(0,500),(1000,500),3)
     power_score()
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               run = False
               save_coins()
               quit()
          elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_p:
                          run = False
                          mixer.music.pause()
                          pause()
                  elif event.key == pygame.K_q:
                          save_coins()
                          pygame.quit()
                          quit()
                 
     #alternate mechanic and continous method
     keys = pygame.key.get_pressed()
     if (keys[pygame.K_LEFT] or AI_left ) and playerX>left_limit :
          playerX -= vel
          AI_left=False
     if (keys[pygame.K_RIGHT] or AI_right) and playerX<right_limit  :
          playerX += vel
          AI_right=False
     if keys[pygame.K_SPACE] or AI_space:
          AI_space=False
          if shotgun_state>0:
               if bullet_state==["ready","ready","ready","ready"]:
                    for p in range(1,4):                         
                         if smg_state==0 and (stones_status["reality"]==-1 or stones_status["reality"]==-2):
                              bulletX[p] = playerX
                              bulletY[p]= 480
                         elif stones_status["reality"]>0:
                              bulletX[p]=playerX
                              bulletY[p]= 480
                         elif smg_state>0:
                              bulletX[p]=playerX-47
                              bulletY[p]=playerY-30
                         fire(bulletX[p],bulletY[p],bulletimg[p],p)
          else:
               if bullet_state[1] is "ready" :
                    # current coordinate of spaceship
                    if smg_state==0:
                         bulletX[1] = playerX
                         bulletY[1] = 480
                    elif smg_state>0:
                         bulletX[1]=playerX-47
                         bulletY[1]=playerY-30
                    fire(bulletX[1], bulletY[1],bulletimg1,1)
     if keys[pygame.K_b] :
          if power_state[0]>=1 and blast_state==0:
               blast()
     if keys[pygame.K_n] and smg_state==0 and (stones_status["reality"]==-1 or stones_status["reality"]==-2):
          if power_state[2]>=1:
               smg()
     if keys[pygame.K_v] and shotgun_state==0:
          if power_state[1]>=1:
               shotgun()
     if keys[pygame.K_m] and button_press==0:
          button_press=40
          if not autopilot_state:
               autopilot_state=True
               autopilot_time=autopilot_time//1
          else:
               autopilot_state=False
               autopilot_time=autopilot_time//1
     if button_press>0: # to prevent multiple button press for autopilot
          button_press-=1
     if keys[pygame.K_x]:
          mindstone()
          
     #stone trigger
     if stone_trigger_state==0:
          stone_trigger()
     elif stone_trigger_state>0:
          stone_trigger_state-=1
          
     #blast animation
     if blast_state<=0:
          None
     elif blast_state>0:
          screen.blit(blastimg,(playerX-30,playerY-30))
          screen.blit(blastbutton2, (0, 555))
          blast_state=blast_state-1
          
     #smg timer
     if smg_state>0 :
          smg_state=smg_state-1
          screen.blit(smgbutton2, (0, 555))
     elif smg_state==0 and stones_status["time"]<=0:
          not_smg()
     elif smg_state==0 and stones_status["time"]>0:
          not_smg()
          bulletY_change=5
          
     stones_display()
     #shotgun timer
     if shotgun_state>0:
          shotgun_state=shotgun_state-1
          screen.blit(shotgunbutton2, (0, 555))
     elif shotgun_state==0:
          bullet_state[2]="ready"
          bullet_state[3]="ready"
          bulletY[2]=0
          bulletY[3]=0

     #autopilot
     if autopilot_state and autopilot_time>1:
          autopilot_time-=1
          AI()
     elif autopilot_time==1 and autopilot_state:
          autopilot_state=False
          autopilot_time=0
     elif not autopilot_state:
          autopilot_time+=0.2
          
     #life of stones
     for t in stones_X.keys():
          for j in range(1,4):
               if smg_state>0:
                    collisions = smg_collision (stones_X[t] , stones_Y[t] , bulletX[j] , bulletY[j])
               else:
                     collisions = collision (stones_X[t] , stones_Y[t] , bulletX[j] , bulletY[j])
               if collisions and score>25 :
                    bulletY[j] = -200
                    bullet_state[j] = "ready"
                    if stones_status[t]==-1 and (stones_status["soul"]==-1 or stones_status["soul"]==-2):
                         stones_life[t]-=5
                    if stones_life[t]==0:
                         stones_X[t]=-50
                         stones_Y[t]=-50
                         stones_status[t]=-2

     #timestone
     if stones_status["time"]>0:
          stones_status["time"]=stones_status["time"]-1
     elif stones_status["time"]==0:
          stones_img["time"]=pygame.image.load("time stone dead.png")
          stones_img["time"]=pygame.transform.scale(stones_img["time"],(40,40))
          stones_status["time"]=-1
          vel=3
          mixer.music.fadeout(4000)
          bulletY_change=10

     #realitystone
     if stones_status["reality"]>0:
          stones_status["reality"]=stones_status["reality"]-1
          bulletimg1=pygame.image.load("bubbles.png")
          bulletimg2=pygame.image.load("bubbles.png")
          bulletimg3=pygame.image.load("bubbles.png")
          bulletimg1=pygame.transform.scale(bulletimg1,(40,40))
          bulletimg2=pygame.transform.scale(bulletimg2,(40,40))
          bulletimg3=pygame.transform.scale(bulletimg3,(40,40))
          bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
          bulletY_change=1
          bullet_limit=360
     elif stones_status["reality"]==0:
          stones_img["reality"]=pygame.image.load("reality stone dead.png")
          stones_img["reality"]=pygame.transform.scale(stones_img["reality"],(40,40))
          stones_status["reality"]=-1
          bulletY_change=10
          mixer.music.fadeout(4000)
          bulletimg1=pygame.image.load("bullet.png")
          bulletimg2=pygame.image.load("bullet.png")
          bulletimg3=pygame.image.load("bullet.png")
          bulletimg=["",bulletimg1,bulletimg2,bulletimg3]
          bullet_limit=0

     #soul stone
     if stones_status["soul"]==1450:
          d=random.choice(list_soul)
          stones_status[d]=-1
          stones_status["soul"]-=1
          stones_X[d]=stones_X2[d]
          stones_Y[d]=stones_Y2[d]
          stones_life[d]=100
     elif stones_status["soul"]>0:
          stones_status["soul"]-=1
     elif stones_status["soul"]==0:
          stones_status["soul"]=-1
          mixer.music.fadeout(4000)
          stones_img["soul"]=pygame.image.load("soul stone dead.png")
          stones_img["soul"]=pygame.transform.scale(stones_img["soul"],(40,40))
          
     #mind stone
     if stones_status["mind"]==940:
          stones_status["black"]=-1
          stones_X["black"]=stones_X2["black"]
          stones_Y["black"]=stones_Y2["black"]
          stones_life["black"]=100
          screen.blit(laserimg,(415,128))
          stones_status["mind"]=stones_status["mind"]-1
          
     elif stones_status["mind"]>0 :
          screen.blit(laserimg,(415,128))
          stones_status["mind"]=stones_status["mind"]-1
     
     elif stones_status["mind"]==0:
          stones_status["mind"]=-1
          mixer.music.fadeout(4000)
          stones_img["mind"]=pygame.image.load("mind stone dead.png")
          stones_img["mind"]=pygame.transform.scale(stones_img["mind"],(40,40))
          if playerX>=400:
               left_limit=0
          elif playerX<400:
               right_limit=735

     #space stone
     if stones_status["space"]>0:
          teleport()
          stones_status["space"]-=1
     elif stones_status["space"]==0:
          stones_status["space"]=-1
          mixer.music.fadeout(4000)
          stones_img["space"]=pygame.image.load("space stone dead.png")
          stones_img["space"]=pygame.transform.scale(stones_img["space"],(40,40))
          for i in range(num_enemy):
               enemyimg[i]=pygame.image.load("enemy.png")
               if X_change[i]>0:
                    X_change[i]=3
               elif X_change[i]<0:
                    X_change[i]=-3
                    
     #power stone
     if stones_status["power"]>0:
          power_shield()
          stones_status["power"]-=1
     elif stones_status["power"]==0:
          stones_status["power"]=-1
          mixer.music.fadeout(4000)
          stones_img["power"]=pygame.image.load("power stone dead.png")
          stones_img["power"]=pygame.transform.scale(stones_img["power"],(40,40))
          for i in range(num_enemy):
               enemyimg[i]=pygame.image.load("enemy.png")
               if X_change[i]>0:
                    X_change[i]=3
               elif X_change[i]<0:
                    X_change[i]=-3
                    
     # enemy movement
     if animate_over==-1:
          for i in range(len(enemyX)):
               if enemyY[i] >= 440:
                    for j in range (len(enemyX)):
                         mixer.music.stop()
                         save_highscore()
                         rewardY_change=0   
                         game_over_animation()
                    
               enemyX[i] = enemyX[i] + X_change[i]
               if enemyX[i] <= 0:
                    X_change[i] = 3
                    enemyY[i] = enemyY[i] + Y_change[i]
               elif enemyX[i] >= 736:
                    X_change[i] = -3
                    enemyY[i] = enemyY[i] + Y_change[i]     
     
               #collision check
               for j in range(1,4):
                    if smg_state<=0:
                         collisions = collision (enemyX[i] , enemyY[i] , bulletX[j] , bulletY[j])
                    else:
                         collisions = smg_collision (enemyX[i],enemyY[i] ,bulletX[j] , bulletY[j])
                    if collisions:
                         bulletY[j] =-200
                         bullet_state[j] = "ready"
                         score += 1
                         reward()
                         enemyX[i]= random.randint(0, 735)
                         enemyY[i] = random.randint(40, 150)
               if stones_status["black"]==-2:
                    enemy(enemyX[i], enemyY[i], i)

     elif animate_over==0:
          game_over()

     elif animate_over>0:
          animate_over-=1
          for i in range(len(enemyX)):
               enemyY[i]=enemyY[i]+Y_change[i]
               enemy(enemyX[i], enemyY[i], i)
     reward_collision()
     
     # Bullet movement
     for q in range(1,4):
          if q==1:
               if bullet_state[1] is "fire":
                    fire(bulletX[1], bulletY[1],bulletimg[1],1)
                    bulletY[1] -= bulletY_change
               if bulletY[1] <= bullet_limit:
                    bulletY[1] = -200
                    bullet_state[1] = "ready"
          if q==2 and shotgun_state>0:
               if bullet_state[2] is "fire":
                    bulletY[2] -= bulletY_change
                    bulletX[2] -=bulletY_change/2
                    fire(bulletX[2], bulletY[2],bulletimg[2],2)
               if bulletY[2] <= bullet_limit or bulletX[2]<=left_limit:
                    bulletY[2] = -200
                    bullet_state[2] = "ready"
          if q==3 and shotgun_state>0:
               if bullet_state[3] is "fire":
                    bulletY[3] -= bulletY_change
                    bulletX[3] +=bulletY_change/2
                    fire(bulletX[3], bulletY[3],bulletimg[3],3)
               if bulletY[3] <= bullet_limit or bulletX[3]>=right_limit:
                    bulletY[3] = -200
                    bullet_state[3] = "ready"
                    
     # Reward movement
     try:
          for p in range(4):
               if reward_state[p] is "fire":
                    rewardY[p]+=rewardY_change[p]
                    screen.blit(rewardimg[p],(rewardX[p],rewardY[p]))
               if rewardY[p]>=480:
                    rewardY[p]=0
                    reward_state[p]="ready"
     except TypeError:
          pass
                    
     player(playerX)
     show_score()
     show_highscore()
     show_coins()
     pygame.display.update()
pygame.quit()


