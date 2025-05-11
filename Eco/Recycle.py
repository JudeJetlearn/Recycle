import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 700
TITLE = "Recylce Marathon"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

bg = pygame.image.load("ecobg.png")
bg = pygame.transform.scale(bg, (WIDTH,HEIGHT))
screen.blit(bg,(0,0))

items = ["Crate.png","paperbag.png","pencil.png"]
score = 0
font = pygame.font.SysFont("Arial", 25)
start_time = time.time()

add_score = font.render("score =" + str(score), True, "white")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.y = (self.rect.y - 5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.y = (self.rect.y + 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
             
        
Sprites = pygame.sprite.Group()

class Plastic_bag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("plasticbag.png")
        self.image = pygame.transform.scale(self.image, (35,35))
        self.rect = self.image.get_rect()

plastic_group = pygame.sprite.Group()

for i in range(20):
    
    PB = Plastic_bag()
    
    PB.rect.x = random.randint(0,WIDTH)  
    PB.rect.y = random.randint(0,HEIGHT)
    
    Sprites.add(PB)
    plastic_group.add(PB)  




bin = Bin() 
Sprites.add(bin)

class Recycleable_Items(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(35,35))
        self.rect = self.image.get_rect()

recycle_group = pygame.sprite.Group()

for i in range(20):
    
    item = Recycleable_Items(random.choice(items))
    
    item.rect.x = random.randint(0,WIDTH)  
    item.rect.y = random.randint(0,HEIGHT)
    
    Sprites.add(item)
    recycle_group.add(item) 


run = True

while run:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    time_played = time.time() - start_time
    if time_played >= 60:
        if score >= 15:
            add_score = font.render("You Win!", True, "Gold")
        else:
            add_score = font.render("Better luck next time", True, "white")
    
    screen.blit(bg,(0,0))            
    Sprites.draw(screen)        
    pressed_keys = pygame.key.get_pressed()
    bin.update(pressed_keys)
    
    Hit_recycle = pygame.sprite.spritecollide(bin,recycle_group,True)
    Hit_plastic = pygame.sprite.spritecollide(bin,plastic_group,True)
    
    for i in Hit_recycle:
        score = score + 1
        add_score = font.render( "score =" + str(score), True, "white") 
    for i in Hit_plastic:
        score = score - 1
        add_score = font.render( "score =" + str(score), True, "white")
    
    screen.blit(add_score,(0,0))
    
pygame.quit()
