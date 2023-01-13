# Arham & Herman - Zelda-Like Major Project

# January 12th, 2022
# This is a zelda-like gme where you have to use the arrow keys to move the player around, avoid the obstacles and the fireballs and reach the finish line to win


import pygame																																						#importing the pygame module
pygame.init()

width = 800
height = 800
window = pygame.display.set_mode((width,height))																													# setting the width and height of the canvas

pygame.display.set_caption("Major Project")																															# Captioning the display
vel = 0
game_condition = 0
tile_size = 50																																						# setting tile size to 50
bushimg = pygame.image.load('bush2.png')																															# loading the bush image
spikeimg = pygame.image.load('spikeimg1.png')																														# loading the spike image
backimg = pygame.image.load('backimg.jpg')																															# loading the background image
bg = pygame.transform.scale(backimg, (800,800))																														# transforming the background image to fit the entire canvas
endgame = pygame.image.load('neon_gameover_sign.png')																						# end screen
eg = pygame.transform.scale(endgame, (800,800))
wingame = pygame.image.load('congratulations-game-screen-golden-congrats-sign-vector-32216807.jpg')																	# This screen shows up when the player wins the game 
wg = pygame.transform.scale(wingame, (800,800))
startscreen = pygame.image.load('StartScreen1.webp')																												# start screen
startsc = pygame.transform.scale(startscreen, (800,800))
keys = pygame.key.get_pressed()
play = False
end = False


player_health = 200																																					# setting player health to 200hp
clock = pygame.time.Clock()																																			# to keep the count of seconds to spawn another enemy

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        img = pygame.image.load('hiiiiiiiiii-removebg-preview.png').convert_alpha()
        self.image = pygame.transform.scale(img, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
    def draw(self):
        window.blit(self.image, self.rect)
portal = Portal(700,200)

class Player(pygame.sprite.Sprite):																																	# creating the player class using sprites from pygame
    def __init__(self, x, y):
        """ Using this function to set up the character """
        img = pygame.image.load('testplayer-removebg-preview.png').convert_alpha()																					# loading the character image
        self.image = pygame.transform.scale(img,(50,50))																											# transforming the image by 50 by 50
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 30																																				# setting the width of the character
        self.height = 30																																			# setting the height of the character
        self.vel_y = 0																																				# velocity of the character about the y axis
        
    def draw(self):
        """ keeps drawing the image over and over again"""
        window.blit(self.image, self.rect)																															# copies the pixels of an image on the canvas
        
    def update(self, game_condition):
        """ Updating the location and player health of the character """
        global player_health
        global keys
        dx = 0																																						# speed of the character about the x axis (horizontal)
        dy = 0																																						# speed of the character about the y axis (vertical)
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.x > 0:																													# when the left arrow key is pressed
            dx -= 15																																				# decrease the speed of character about the x axis by 15
            
        if keys[pygame.K_RIGHT] and self.rect.x < 800 - 50:																											# when the right arrow key is pressed
             dx += 15																																				# increase the speed of character about the x axis by 15
                
        if keys[pygame.K_UP] and self.rect.y > 0:																													# when the up arrow key is pressed
            dy -= 15																																				# decrease the speed of character about the y axis by 15
            
        if keys[pygame.K_DOWN] and self.rect.y < 800 - 50:																											# when the down arrow key is pressed
            dy += 15																																				# increase the speed of character about the y axis by 15
            
            
        self.rect.x += dx																																			# moving the character horizontally according to dx
        self.rect.y += dy																																			# moving the character vertically according to dy
            
        if self.rect.bottom > height:
            self.rect.bottom = height
            dy = 0
        #Collisions
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y,self.width,self.height):
                player_health -= 40																																	# If the character collides with a bush or a spike his health decreases by 10
                if dx > 0:																																			# if the character collides while moving to the right
                    self.rect.right = self.rect.left																												# the characters right and left sides switch so it looks like it bounced off
                    self.vel_y = 0
                if dx < 0:																																			# if the character collides while moving to the left
                    self.rect.left = self.rect.right
                    self.vel_y = 0
                if dy > 0:
                    self.rect.bottom = self.rect.top																												# if the character collides while moving upwards
                    self.vel_y = 0
                if dy < 0:
                    self.rect.top = self.rect.bottom																												#if the character collides while moving downwards
                    self.vel_y = 0
        #In the process of making a health bar
        pygame.draw.rect(window, "red", (15, 50, 200, 10))
        pygame.draw.rect(window, "green",(15, 50, player_health,10))
    
        def checkCollision(self, player, monsterfire, monsterfire1, monsterfire2, monsterfire3, monsterfire4): 														# this method checks for collisions
            """ this function is used to check collisions between the fireball and the player   """
            global player_health
            col = pygame.sprite.collide_rect(player, monsterfire)																									# if player and monsterfire collide the variable col becomes true
            col1 = pygame.sprite.collide_rect(player, monsterfire1)
            col2 = pygame.sprite.collide_rect(player, monsterfire2)
            col3 = pygame.sprite.collide_rect(player, monsterfire3)
            col4 = pygame.sprite.collide_rect(player, monsterfire4)
            if col == True:																																			# if theres a collision between player and monsterfire
                player_health -= 30																																	# player health decreases by 10
            if col1 == True:
                player_health -= 30
            if col2 == True:
                player_health -= 30
            if col3 == True:
                player_health -= 30
            if col4 == True:
                player_health -= 30
        checkCollision(self, player, monsterfire, monsterfire1, monsterfire2, monsterfire3, monsterfire4)

    
        
player = Player(650,200)																																				# spawning the player


class MonsterFire(pygame.sprite.Sprite):																															# creating a class for the fireball the monster fires 
    def __init__(self, x, y):
        """ setting up the fireball """
        img = pygame.image.load('MonsterFire-removebg.png').convert_alpha()																							# loading up the image of the fireball
        self.image = pygame.transform.scale(img,(60,60))																											# transforming the image's size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()																															# setting the image's  width as its width
        self.height = self.image.get_height()																														# setting the image's  width as its width
           
    def draw(self):
        """ keeps on drawing the image over and over again """
        window.blit(self.image, self.rect) 

monsterfire = MonsterFire(75,100)																																	# calling monsterfire
monsterfire1 = MonsterFire(150, 100)
monsterfire2 = MonsterFire(400, 100)
monsterfire3 = MonsterFire(600, 100)
monsterfire4 = MonsterFire(475, 100)


class Monster(pygame.sprite.Sprite):																																# creating a class to create the enemy/monster
    def __init__(self, x, y):
        """setting up the monster """
        img = pygame.image.load('ZeldaEnemy1.webp').convert_alpha()																									#  loading up the image of the monster
        self.image = pygame.transform.scale(img,(50,50))																											# transforming the image's size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
           
    def draw(self):
        """ keeps on drawing the image over and over again """
        window.blit(self.image, self.rect)																															# copies the pixels of an image on the canvas

                   

        
monster = Monster(75,100)																																			# calling the monster at different locations
monster1 = Monster(150, 100)
monster2 = Monster(400, 100)
monster3 = Monster(600, 100)
monster4 = Monster(475, 100)

     
#Class created so that the window is broken up into individual tiles
class world():
    def __init__(self,data):
         #creates a list of all the tiles spaces avalibe on the screen
        self.tile_list = []
        #accociates values to specific tiles   
        rows = 0
        for row in data:
            col = 0
            for tile in row:
                if tile == 1:																																	# if the tile in the world data is 1
                    img = pygame.transform.scale(bushimg, (70, 70))																								# a bush image is put up in that tile
                    img_rect = img.get_rect()
                    img_rect.x = col * tile_size																												# setting the x coordinate of the bush
                    img_rect.y = rows * tile_size																												# setting the y coordinate of the bush
                    tile = (img,img_rect)
                    self.tile_list.append(tile)																													# appending the tile to the empty tile_list
                if tile == 2:																																	# if the tile in the world data is 2
                    img = pygame.transform.scale(spikeimg, (30,30))																								# a spike image is put up in that tile
                    img_rect = img.get_rect()
                    img_rect.x = col * tile_size																												# setting the x coordinate of the spike
                    img_rect.y = rows * tile_size																												# setting the y coordinate of the spike
                    tile = (img,img_rect)
                    self.tile_list.append(tile)																													# appending the tile to the empty tile_list

                col += 1
            rows += 1
    
    def draw(self):
        """Keeps drawing the bush or spike"""
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])


                    

world_data =  [																																					# each tile is 50
[0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0],
[0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0],
[0,0,0,0,1,1,1,0,0,1,0,0,0,0,2,0],
[0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,0],
[0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,2,0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,2,2,2,2,2,0,0,0,1,0,0,0],
]

world = world(world_data)   
y = 150
keys = pygame.key.get_pressed()


while play == False:
    window.blit(startsc, (0,0))
    for event in pygame.event.get():           
        if event.type == pygame.KEYDOWN:
            play = True
            start_ticks = pygame.time.get_ticks()																															# starting the seconds to spawn another enemy after a few seconds

        
    pygame.display.flip()
    pygame.display.update()

    

    
while play == True:
    dt = clock.tick()
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.blit(bg, (0,0))
    world.draw()
    player.draw()																																				# keeps on drawing the player
    player.update(0)
    monster.draw()																																				# keeps on drawing the monster
    monster.update(0)
    portal.draw()
    portal.update(0)
    for i in range(10):																																			# this loop helps in moving the fireball
        y = y + 5
        if seconds > 0:																																			# only one fireball is spawned in the first 5 seconds
            monsterfire = MonsterFire(75,y)																														# as y increments the fireball moves down the canvas
            monsterfire.draw()
            monsterfire.update(0)
        if seconds > 5:																																			# The second fireball spawns after 5 seconds
            monsterfire1 = MonsterFire(150,y)
            monsterfire1.draw()
            monsterfire1.update(0)
        if seconds > 10:																																		# The third fireball spawns after 10 seconds
            monsterfire2 = MonsterFire(400,y)
            monsterfire2.draw()
            monsterfire2.update(0)
        if seconds > 15:																																		# The fourth fireball spawns after 15 seconds
            monsterfire3 = MonsterFire(600,y)
            monsterfire3.draw()
            monsterfire3.update(0)
        if seconds > 20:																																		# The fifth fireball spawns after 20 seconds
            monsterfire4 = MonsterFire(475,y)
            monsterfire4.draw()
            monsterfire4.update(0)
        if y == 850:																																			# if the fireball goes out the canvas
            y = 200																																				# the y coordinate of the firball is resetted to back where it started
            
    if seconds > 5:																																				# the second monster spawns after 5 seconds
        monster1.draw()
        monster1.update(0)
    if seconds > 10:																																			# the third monster spawns after 10 seconds
        monster2.draw()
        monster2.update(0)
    if seconds > 15:																																			# the fourth monster spawns after 15 seconds
        monster3.draw()
        monster3.update(0)
    if seconds > 20:																																			# the fifth monster spawns after 20 seconds
        monster4.draw()
        monster4.update(0)
     
    win_collision = pygame.sprite.collide_rect(player, portal)																									# win collision is true when the player reaches the portal
    if win_collision == True:																																	# when win collision is true, show win screen
        window.blit(wg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                quit()
    if player_health == 0:																																		# when the player's health equals 0
        end = True
        while end == True:
            window.blit(eg, (0,0))																																	# show end game over screen
            pygame.display.flip()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    quit()    
        

        
    pygame.display.flip()
    pygame.display.update()

