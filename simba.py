import pygame
from time import sleep

pygame.init()

w, h = 1000, 600
f1 = pygame.font.Font(None, 36)
YELLOW = (247, 244, 47)
lose_image = pygame.transform.scale(pygame.image.load('lose_img.jpg'), (w, h))
win_image = pygame.transform.scale(pygame.image.load('win_img.jpg'), (w, h))

class Ball():
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_x = 3
        self.speed_y = 3
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        
    def draw_1(self):
        pygame.draw.circle(window, self.color, (self.rect.x+self.radius, self.rect.y+self.radius), self.radius)
        
    def go(self):
        global run, lose_image
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > h:
            window.blit(lose_image, (0, 0))
            pygame.display.update()
            lose_sound = pygame.mixer.Sound('lose.mp3')
            lose_sound.play()
            sleep(5)
            run = False
        elif self.rect.x > w:
            self.speed_x *= -1
        elif self.rect.x < 0:
            self.speed_x *= -1
        elif self.rect.y < 0:
            self.speed_y *= -1
class Brick():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw_2(self):
        pygame.draw.rect(window, self.color, self.rect)
         
def load_level_map (filename):
    global bricks
    bricks = list() 
    with open (filename, 'r') as file: 
        lines = [line for line in file.readlines ()] 
    for row_index, line in enumerate (lines): 
        for col_index, char in enumerate (line): 
            if char == '*': 
                x = (col_index + 0.3) * 65 
                y = (row_index + 0.3) * 65 
                brick = Brick(x, y, 50, 50, YELLOW) 
                bricks.append(brick)
    return bricks

window = pygame.display.set_mode((w, h))

ball = Ball(300, 300, (255, 0, 0), 20)
platforma = Brick(400, 500, 200, 30,YELLOW)

score = 0

lvl1 = load_level_map('sasha.txt')
right = False
left = False

clock = pygame.time.Clock()

run = True
while run:
    window.fill((0, 0 ,0))
    for brick in lvl1:
        brick.draw_2()
    pygame.draw.line(window, YELLOW, (0,0), (0, h), 5)
    pygame.draw.line(window, YELLOW, (0,h), (w, h), 5)
    pygame.draw.line(window, YELLOW, (w, h), (w, 0), 5)
    pygame.draw.line(window, YELLOW, (0,0), (w, 0), 5)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                # platforma.rect.x += 10
                right = True
            if e.key == pygame.K_LEFT:
                # platforma.rect.x -= 10
                left = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_LEFT:
                left = False

    if right:
        platforma.rect.x += 10
    if left:
        platforma.rect.x -= 10
    
    if platforma.rect.x == 0:
        left = False
    if platforma.rect.x == 800:
        right = False

    
    ball.draw_1()
    ball.go()
    platforma.draw_2()
    
    for brick in bricks:
        if brick.rect.colliderect(ball):
            bricks.remove(brick)
            ball.speed_y *= -1
            score += 1
            nado_sound = pygame.mixer.Sound('nado.mp3')
            nado_sound.play()
        else:
            brick.draw_2()

    if len(bricks) == 0:
        window.blit(win_image, (0, 0))
        pygame.display.update()
        lose_sound = pygame.mixer.Sound('win.mp3')
        lose_sound.play()
        sleep(5)
        run = False
        
    if platforma.rect.colliderect(ball):
        ball.speed_y *= -1
        
    text1 = f1.render(f'Score: {score}', True, (255, 255, 255))

    window.blit(text1, (20, 540))


    pygame.display.update()
    clock.tick(60)