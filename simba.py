import pygame

pygame.init()

YELLOW = (247, 244, 47)

class Ball():
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.speed_x = 2
        self.speed_y = 2
        
    def draw_1(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
        
    def go(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > h:
            self.speed_y *= -1
        elif self.x > w:
            self.speed_x *= -1
        elif self.x < 0:
            self.speed_x *= -1
        elif self.y < 0:
            self.speed_y *= -1
class Brick():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        
    def draw_2(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
         
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

w, h = 1000, 600
window = pygame.display.set_mode((w, h))

ball = Ball(300, 300, (255, 0, 0), 20)

lvl1 = load_level_map('sasha.txt')

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
    
    ball.draw_1()
    ball.go()
    
    for b in bricks:
        if b.rect.coliderect(brick):
            bricks.remove(b)
            ball.speed_y *= -1
        else:
            b.reset()
        
    pygame.display.update()
    clock.tick(60)