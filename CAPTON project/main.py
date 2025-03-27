import pygame
score = 0
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load('CAPTON project/images/Spacey backround.png')
background_scale = pygame.transform.scale(background,(WIDTH,HEIGHT))
directions = [0,0,0,0]
bullets = []
class Space_ship:
    def __init__(self):
        self.x = WIDTH/2 - 50
        self.y = HEIGHT/2 -50
        self.angle = 0
        self.hp = 3
        self.image = pygame.image.load('CAPTON project/images/kirby_star_ship.png')
        self.rect = self.image.get_rect()

    def draw(self):
        if directions[0] == 1 and directions[1] == 0 and directions[2] == 0 and directions[3] == 0:
            self.angle = 0
        if directions[0] == 0 and directions[1] == 1 and directions[2] == 0 and directions[3] == 0:
            self.angle = 180
        if directions[0] == 0 and directions[1] == 0 and directions[2] == 1 and directions[3] == 0:
            self.angle = 90
        if directions[0] == 0 and directions[1] == 0 and directions[2] == 0 and directions[3] == 1:
            self.angle = -90
        if directions[0] == 1 and directions[1] == 0 and directions[2] == 1 and directions[3] == 0:
            self.angle = 45
        if directions[0] == 1 and directions[1] == 0 and directions[2] == 0 and directions[3] == 1:
            self.angle = -45
        if directions[0] == 0 and directions[1] == 1 and directions[2] == 1 and directions[3] == 0:
            self.angle = 135
        if directions[0] == 0 and directions[1] == 1 and directions[2] == 0 and directions[3] == 1:
            self.angle = -135
        if directions[0] == 1 and directions[1] == 0 and directions[2] == 1 and directions[3] == 1:
            self.angle = 0
        if directions[0] == 1 and directions[1] == 1 and directions[2] == 0 and directions[3] == 1:
            self.angle = 90
        if directions[0] == 1 and directions[1] == 1 and directions[2] == 1 and directions[3] == 0:
            self.angle = -90
        if directions[0] == 0 and directions[1] == 1 and directions[2] == 1 and directions[3] == 1:
            self.angle = 180

        rotated_image = pygame.transform.rotate(self.image,self.angle)
        screen.blit(rotated_image,(self.x,self.y))
class Bullet:
    def __init__(self):
        self.x = spaceship.x + 50
        self.y = spaceship.y + 50
        self.angle = spaceship.angle

    def draw(self):
        pygame.draw.rect(screen,'white',(self.x,self.y,10,10))

def create_bullet():
    bullet = Bullet()
    bullets.append(bullet)


spaceship = Space_ship()

running = True
while running:
    screen.blit(background_scale,(0,0))
    spaceship.draw()
    
    for bullet in bullets:
        bullet.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                create_bullet()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                directions[0] = 1

            if event.key == pygame.K_DOWN:
                directions[1] = 1

            if event.key == pygame.K_LEFT:
                directions[2] = 1

            if event.key == pygame.K_RIGHT:
                directions[3] = 1

        if event.type == pygame.KEYUP:
            directions = [0,0,0,0]

    if directions[0] == 1:
        spaceship.y -= 1
    if directions[1] == 1:
        spaceship.y += 1
    if directions[2] == 1:
        spaceship.x -= 1
    if directions[3] == 1:
        spaceship.x += 1
        

    pygame.display.update()
pygame.quit()