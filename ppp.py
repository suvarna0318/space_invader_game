import pygame
import random
import math	

pygame.init()
screen=pygame.display.set_mode((800,600))
runnig=True

background_img=pygame.image.load('background.png')

player_img=pygame.image.load('space-invaders.png')
playerX=368
playerY=480
player_change=0

enemy_img=pygame.image.load('enemy.png')
enemyX=random.randint(0,736)
enemyY=random.randint(0,100)
enemyX_change=5
enemyY_change=60

bullet_img=pygame.image.load('bullet.png')
bulletX=382
bulletY=480
bulletX_change=0
bulletY_change=0

bullet_state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf', 32)
testX=10
testY=10
def show_score(x,y):
	score=font.render("Score"+str(score_value),True,(255,255,255))
	screen.blit(score,(x,y))

def bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bullet_img,(x+16,y+10))

def player(x,y):
	screen.blit(player_img,(x,y))

def enemy(x,y):
	screen.blit(enemy_img,(x,y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
		distance=math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
		if distance<27:
			return True
		else:
			return False


while runnig:
	screen.fill((0,0,0))
	screen.blit(background_img,(0,0))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			runnig=False

		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				player_change=-5

			if event.key==pygame.K_RIGHT:
				player_change=5

			if event.key==pygame.K_SPACE:
				if bullet_state=="ready":
					bulletX=playerX
					bullet(bulletX,bulletY)

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				player_change=0
	collision=isCollision(enemyX, enemyY, bulletX, bulletY)
	if collision:
		# print("collision")
		score_value+=1
		screen.blit(pygame.image.load("space-icon.png"),(enemyX,enemyY))
		bullet_state="ready"
		bulletY=480
		enemyX=random.randint(0,736)
		enemyY=random.randint(0,100)

	if bullet_state=="fire":
		bulletY_change=-8
		bullet(bulletX,bulletY)
	else:
		bullet_state="ready"

	if bulletY<=0:
		bulletY=playerY
		bullet_state="ready"

			
	bulletY+=bulletY_change

	if enemyX>=736:
		enemyX_change=-5
		enemyY+=enemyY_change
		
	elif enemyX<=0:
		enemyX_change=5
		enemyY+=enemyY_change
		


	if playerX<=0:
		playerX=0
	if playerX>=736:
		playerX=736

	

	playerX+=player_change
	enemyX+=enemyX_change

	enemy(enemyX,enemyY)
	player(playerX,playerY)
	show_score(testX,testY)
	pygame.display.update()