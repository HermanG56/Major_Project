import pygame
import random2
pygame.init()

width = 800
height = 800
window = pygame.display.set_mode((width,height))

pygame.display.set_caption("Major Project")

x = 400
y = 400
vel = 0
game_condition = 0
tile_size = 50
bushimg = pygame.image.load('bush2.png')
spikeimg = pygame.image.load('spikeimg1.png')
backimg = pygame.image.load('backimg.jpg')
bg = pygame.transform.scale(backimg, (800,800))
player_health = 200
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        img = pygame.image.load('testplayer-removebg-preview.png').convert_alpha()
        self.image = pygame.transform.scale(img,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 30
        self.height = 30
        self.vel_y = 0
        self.space = False
        clock.tick(30)
        
    def draw(self): 
        window.blit(self.image, self.rect)
        
    def update(self, game_condition):
        global player_health
        global keys
        dx = 0
        dy = 0
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            dx -= 15
            
        if keys[pygame.K_RIGHT] and self.rect.x < 800 - 50:
             dx += 15
                
        if keys[pygame.K_UP] and self.rect.y > 0:
            dy -= 15
            
        if keys[pygame.K_DOWN] and self.rect.y < 800 - 50:
            dy += 15
            
            
        self.rect.x += dx
        self.rect.y += dy
            
        if self.rect.bottom > height:
            self.rect.bottom = height
            dy = 0
        #Collisions
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x, self.rect.y,self.width,self.height):
                player_health -= 10
                if dx > 0:
                    self.rect.right = self.rect.left
                    self.vel_y = 0
                if dx < 0:
                    self.rect.left = self.rect.right
                    self.vel_y = 0
                if dy > 0:
                    self.rect.bottom = self.rect.top
                    self.vel_y = 0
                if dy < 0:
                    self.rect.top = self.rect.bottom
                    self.vel_y = 0
        #In the process of making a health bar
        pygame.draw.rect(window, "red", (15, 50, 200, 10))
        pygame.draw.rect(window, "green",(15, 50, player_health,10))
    
        if player_health == 0:
            
            quit()

    
        
player = Player(0,800)


class MonsterFire(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        img = pygame.image.load('MonsterFire-removebg.png').convert_alpha()
        self.image = pygame.transform.scale(img,(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        
           
    def draw(self): 
        window.blit(self.image, self.rect)

monsterfire = MonsterFire(75,100)
monsterfire1 = MonsterFire(150, 100)
monsterfire2 = MonsterFire(400, 100)
monsterfire3 = MonsterFire(600, 100)
monsterfire4 = MonsterFire(475, 100)
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        img = pygame.image.load('ZeldaEnemy1.webp').convert_alpha()
        self.image = pygame.transform.scale(img,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.NEW = pygame.USEREVENT + 1
           
    def draw(self): 
        window.blit(self.image, self.rect)

                   

        
monster = Monster(75,100)
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
                if tile == 1:
                    img = pygame.transform.scale(bushimg, (70, 70))
                    img_rect = img.get_rect()
                    img_rect.x = col * tile_size
                    img_rect.y = rows * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(spikeimg, (30,30))
                    img_rect = img.get_rect()
                    img_rect.x = col * tile_size
                    img_rect.y = rows * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)

                col += 1
            rows += 1
    
    def draw(self):
        for tile in self.tile_list:
            window.blit(tile[0], tile[1])


                    
#Each tile is 50 
world_data =  [
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
start_ticks = pygame.time.get_ticks()
time_elapsed = 0
keys = pygame.key.get_pressed()

while True:
    dt = clock.tick()
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    window.blit(bg, (0,0))
    world.draw()
    player.draw()
    player.update(0)
    monster.draw()
    monster.update(0)
    for i in range(10):
        y = y + 5
        if seconds > 0:
            monsterfire = MonsterFire(75,y)
            monsterfire.draw()
            monsterfire.update(0)
        if seconds > 5:
            monsterfire1 = MonsterFire(150,y)
            monsterfire1.draw()
            monsterfire1.update(0)
        if seconds > 10:
            monsterfire2 = MonsterFire(400,y)
            monsterfire2.draw()
            monsterfire2.update(0)
        if seconds > 15:
            monsterfire3 = MonsterFire(600,y)
            monsterfire3.draw()
            monsterfire3.update(0)
        if seconds > 20:
            monsterfire4 = MonsterFire(475,y)
            monsterfire4.draw()
            monsterfire4.update(0)
        if y == 850:
            y = 200
            
    if seconds > 5:
        monster1.draw()
        monster1.update(0)
    if seconds > 10:
        monster2.draw()
        monster2.update(0)
    if seconds > 15:
        monster3.draw()
        monster3.update(0)
    if seconds > 20:
        monster4.draw()
        monster4.update(0)
 

    
    print(seconds)
    

        
    pygame.display.flip()
    pygame.display.update()



    

