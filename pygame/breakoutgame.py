import pygame
pygame.init()

WIDTH =700 #constant values nala capital kuduthurukom
HEIGHT=700
FPS=60

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (80,175,90)
BLUE = (60,160,200)



COLS = 10
ROWS = 6

win = pygame.display.set_mode((WIDTH,HEIGHT)) #etha la google pannale kedaikum,how do display a pygame dispaly apdinu
pygame.display.set_caption("Break Out Game")#this is for title
clock = pygame.time.Clock()

#paddle class
class Paddle():
    def __init__(self):
        self.width = int(WIDTH/COLS) #antha bricks oda size laye intha paddle iruntha nalla irukum so,we to that
        self.height = 20 #antha paddle oda height
        self.x = int(WIDTH/2)-int(self.width/2)
        self.y = HEIGHT - 40
        self.speed =  10
        self.box = pygame.Rect(self.x,self.y,self.width,self.height)

    def draw_paddle(self):
        pygame.draw.rect(win,WHITE,self.box)#draw indrathu oru inbuild method,1.entha display la varaya porom
        #2.enna color 3.entha object ah! varaya porom
        #this rect is a inbuild method name
    #paddle movements
    def paddle_move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.box.left > 0:
            self.box.x -=self.speed
        if key[pygame.K_RIGHT] and self.box.right < WIDTH:
            self.box.x +=self.speed

#ball movements ku oru class define panrom
class Ball():
    def __init__(self,x,y):
        self.radius = 10
        self.x = x  #center la ball varathukandi 10px - panron,pygame eppovume top left tha allocate pannum
        self.y = y
        self.box = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2) #ball first rectangle ah than cosider  pannikanum#ball size with height
        self.dx = 3 #dx positive na ball right side move agum,negative na lefft side
        self.dy = -3 #dy negative na ball upside
        self.game_status =0
    def draw_ball(self):
        pygame.draw.circle(win,BLUE,(self.box.x,self.box.y),self.radius)
    def move_ball(self):
        #wall   collision
        if self.box.right>WIDTH or self.box.left<0:
            self.dx *=-1
        if self.box.top<0:
            self.dy *= -1
        if self.box.bottom>HEIGHT:
            self.game_status =  -1#game over
        # paddle colliision
        if self.box.colliderect(bat) and self.dy >0:
            self.dy*=-1


        self.box.x += self.dx
        self.box.y += self.dy
        return self.game_status








bat = Paddle()# class ku oru object create panrom
ball = Ball(bat.x+int(bat.width/2),bat.y-10)


run =True
while run:
    clock.tick(FPS)
    win.fill(BLACK)
    bat.draw_paddle()  # thenn antha object vechu method call panrom
    bat.paddle_move()
    ball.draw_ball()
    game_status=ball.move_ball()
    if game_status ==-1:
        win.fill(BLACK)
        font=pygame.font.SysFont(None,50)
        text= font.render('GAME OVER',True,BLUE)
        text_box=text.get_rect(center=(WIDTH/2,HEIGHT/2))
        win.blit(text,text_box)

    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
    pygame.display.update()
pygame.quit()



