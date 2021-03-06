import pygame
import time
import random

pygame.init()

gray = (119,118,110)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
display_width = 800
display_height = 600
car_width = 56
pause = False

gameDisplay = pygame.display.set_mode((display_width, display_height))      #Game Resolution
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()
playerCar = pygame.image.load("Player car.jpg")                             #player car image
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("background.jpg")
instruction_background = pygame.image.load("background2.jpg")

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect = text_objects("CAR GAME",largetext)
        TextRect.center = (400,100)
        gameDisplay.blit(TextSurf, TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,red,bright_red,"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if(x+w > mouse[0] > x and y+h > mouse[1] > y):
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if(click[0]==1 and action!=None):
            if(action == "play"):
                countdown()
            elif(action == "quit"):
                pygame.quit()
                quit()
                sys.exit()
            elif(action == "intro"):
                introduction()
            elif(action == "menu"):
                intro_loop()
            elif(action == "pause"):
                paused()
            elif(action=="unpause"):
                unpaused()


    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textsurf,textrect)
    
def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("Dodge the cars",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTIONS",largetext)
        TextRect.center=((400),(100))
        gameDisplay.blit(TextSurf,TextRect)
        gameDisplay.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("A : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("D : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_objects("W : ACCELERATOR",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("S : BRAKE ",smalltext)
        rtextRect.center=((150),(550))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gameDisplay.blit(sTextSurf,sTextRect)
        gameDisplay.blit(stextSurf,stextRect)
        gameDisplay.blit(hTextSurf,hTextRect)
        gameDisplay.blit(atextSurf,atextRect)
        gameDisplay.blit(rtextSurf,rtextRect)
        gameDisplay.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("PAUSED",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
        button("RESTART",350,450,150,50,blue,bright_blue,"play")
        button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)

def unpaused():
    global pause
    pause = False

def car(x, y):
    gameDisplay.blit(playerCar, (x, y))

def background():
    gameDisplay.blit(backgroundpic,(0,0))
    gameDisplay.blit(backgroundpic,(0,200))
    gameDisplay.blit(backgroundpic,(0,400))
    gameDisplay.blit(backgroundpic,(700,0))
    gameDisplay.blit(backgroundpic,(700,200))
    gameDisplay.blit(backgroundpic,(700,400))
    
    gameDisplay.blit(yellow_strip,(400,0))
    gameDisplay.blit(yellow_strip,(400,100))
    gameDisplay.blit(yellow_strip,(400,200))
    gameDisplay.blit(yellow_strip,(400,300))
    gameDisplay.blit(yellow_strip,(400,400))
    gameDisplay.blit(yellow_strip,(400,500))
    
    gameDisplay.blit(strip,(120,0))
    gameDisplay.blit(strip,(120,100))
    gameDisplay.blit(strip,(120,200))
    gameDisplay.blit(strip,(680,0))
    gameDisplay.blit(strip,(680,100))
    gameDisplay.blit(strip,(680,200))

def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("passed" + str(passed), True, black)
    score = font.render("score" + str(score), True, red)
    gameDisplay.blit(text,(0,50))
    gameDisplay.blit(score,(0,30))

def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def display_message(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf,textrect = text_objects(text, largetext)
    textrect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def countdown():
    countdown=True

    while countdown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gameDisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("3",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("2",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("1",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gameDisplay.fill(gray)
        countdown_background()
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("GO!!!",largetext)
        TextRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()

def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gameDisplay.blit(backgroundpic,(0,0))
    gameDisplay.blit(backgroundpic,(0,200))
    gameDisplay.blit(backgroundpic,(0,400))
    gameDisplay.blit(backgroundpic,(700,0))
    gameDisplay.blit(backgroundpic,(700,200))
    gameDisplay.blit(backgroundpic,(700,400))
    gameDisplay.blit(yellow_strip,(400,100))
    gameDisplay.blit(yellow_strip,(400,200))
    gameDisplay.blit(yellow_strip,(400,300))
    gameDisplay.blit(yellow_strip,(400,400))
    gameDisplay.blit(yellow_strip,(400,100))
    gameDisplay.blit(yellow_strip,(400,500))
    gameDisplay.blit(yellow_strip,(400,0))
    gameDisplay.blit(yellow_strip,(400,600))
    gameDisplay.blit(strip,(120,200))
    gameDisplay.blit(strip,(120,0))
    gameDisplay.blit(strip,(120,100))
    gameDisplay.blit(strip,(680,100))
    gameDisplay.blit(strip,(680,0))
    gameDisplay.blit(strip,(680,200))
    gameDisplay.blit(playerCar,(x,y))
    text=font.render("DODGED: 0",True, black)
    score=font.render("SCORE: 0",True,red)
    gameDisplay.blit(text,(0,50))
    gameDisplay.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("Player car.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("car7.jpg")
    gameDisplay.blit(obs_pic,(obs_startx,obs_starty))

def crash():
    display_message("Gamer Over!")

def game_loop():
    bumped = False
    
    x = display_width * 0.45
    y = display_height * 0.77
    x_change = 0                                                        #to move the car using keys
    obs = 0                                                             #obstacles(cars)
    obs_speed = 10
    y_change = 0
    obs_startx = random.randrange(200, display_width-200)               #setting the limit for obstacles
    obs_starty = -750                                                   #obstacles come from the top of the window
    obs_width = 56
    obs_height = 125
    score = 0
    passed = 0
    level = 0
    fps = 120
    y2 = 7
    while not bumped:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()                                           #Ends the loop to close the game
                quit()
        if(event.type == pygame.KEYDOWN):                               #on key press
            if(event.key == pygame.K_a):
                x_change = -5
            if(event.key == pygame.K_d):
                x_change = 5
            if event.key==pygame.K_w:
                obs_speed += 2
            if event.key==pygame.K_s:
                obs_speed -= 2
        if(event.type == pygame.KEYUP):                                 #on releasing the key
            if(event.key == pygame.K_a or event.key == pygame.K_d):
                x_change = 0
        
        x += x_change                                                   #making the car move by x_change valaue when the player will press 
                                                                        #left/right key
        gameDisplay.fill(gray)

        rel_y = y2%backgroundpic.get_rect().width
        gameDisplay.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gameDisplay.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gameDisplay.blit(backgroundpic,(0,rel_y))
            gameDisplay.blit(backgroundpic,(700,rel_y))
            gameDisplay.blit(yellow_strip,(400,rel_y))
            gameDisplay.blit(yellow_strip,(400,rel_y+100))
            gameDisplay.blit(yellow_strip,(400,rel_y+200))
            gameDisplay.blit(yellow_strip,(400,rel_y+300))
            gameDisplay.blit(yellow_strip,(400,rel_y+400))
            gameDisplay.blit(yellow_strip,(400,rel_y+500))
            gameDisplay.blit(yellow_strip,(400,rel_y-100))
            gameDisplay.blit(strip,(120,rel_y-200))
            gameDisplay.blit(strip,(120,rel_y+20))
            gameDisplay.blit(strip,(120,rel_y+30))
            gameDisplay.blit(strip,(680,rel_y-100))
            gameDisplay.blit(strip,(680,rel_y+20))
            gameDisplay.blit(strip,(680,rel_y+30))

        y2+=obs_speed

        obs_starty -= (obs_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obs_speed
        car(x, y)
        score_system(passed, score)
        if(x > 700 - car_width or x < 110):                             #Defining the limit for car moving area
            crash()
        #if car makes contact with any obstacle
        if(x > display_width-(car_width+110) or x < 110):
            crash()
        if(obs_starty > display_height):
            obs_starty = 0-obs_height
            obs_startx = random.randrange(170,(display_width-170))
            obs = random.randrange(0,7)
            passed = passed+1
            score = passed*10
            if(int(passed)%10 == 0):
                level = level+1
                obs_speed+=2
                largetext = pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect = text_objects("LEVEL" + str(level), largetext)
                textrect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if(y < obs_starty + obs_height):
            if(x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width):
                crash()
        #end of obstacle
        pygame.display.update()
        clock.tick(60)
        

intro_loop()
game_loop()
pygame.quit()
quit()
