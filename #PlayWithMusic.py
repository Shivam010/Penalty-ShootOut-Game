import random
import time
import math
import pygame

#Pygame intialized
pygame.init()

#Define colors
lgreen=(128,240,0)
dgreen=(0,100,0)
white=(255,255,255)
black=(0,0,0)
Ar = "MANIT : "
Po = "MNIT : "

#Constants
displayWidth = 1200
displayHeight = 700
centre_x = displayWidth/2
centre_y = displayHeight/2
FPS=15
Shots = 3

#Images
lm = pygame.image.load('images/lmanit.png')
point = pygame.image.load('images/point.png')

back = pygame.image.load('images/back.png')

frnt_1 = pygame.image.load('images/front-1.jpg')

img_instr = pygame.image.load('images/intro.png')

img_play1 = pygame.image.load('images/Play.png')
home_icn = pygame.image.load('images/home.png')
home_icn1 = pygame.image.load('images/home1.png')

icn = pygame.image.load('images/icon.jpg')
img_sky = pygame.image.load('images/sky2.png')

banner = pygame.image.load('images/BANNER.png')
img_goalpost = pygame.image.load('images/goalpost.png')
img_aud = pygame.image.load('images/audi.png')

line1 = pygame.image.load('images/line.png')
line2 = pygame.image.load('images/boundry.png')

img_g1 = pygame.image.load('images/g1.png')
img_g2 = pygame.image.load('images/g2.png')
img_football = pygame.image.load('images/football.png')

imgAt = pygame.image.load('images/a_turn.png')
imgPt = pygame.image.load('images/p_turn.png') 

imgAf = pygame.image.load('images/argentina.png')
imgPf = pygame.image.load('images/portugal.png')

imgDraw = pygame.image.load('images/draw.jpg')


#Screen and Top bar
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('BRAZUCA')

#Create a icon for the top bar
pygame.display.set_icon(icn)

#For using the frames per second
clock=pygame.time.Clock()

#Fonts
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)


#Font Formating Function
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


#To display message to screen
def message_to_screen(msg,color,y_displace=0,size="small"):
    textSurf,textRect = text_objects(msg, color, size)
    textRect.center = (centre_x, (centre_y + y_displace))
    gameDisplay.blit(textSurf,textRect)


#To display the score of the teams
def score_card(msg, x_place, y_place, color=black):
    screen_text = smallfont.render(msg, True, color)
    gameDisplay.blit(screen_text, (x_place, y_place))


def gExit():
    pygame.mixer.music.load("music/#Start.MP3")
    pygame.mixer.music.play(-1,0.0)
    team = pygame.image.load("images/Team.jpg")
    gameDisplay.blit(team, (0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.time.delay(10000)
    pygame.mixer.music.stop()


def instr(flag = 1):
    #Background
    gameDisplay.fill(lgreen)
    gameDisplay.blit(img_sky,(0,0))
    #Audiences
    gameDisplay.blit(img_aud,(0,50))
    gameDisplay.blit(img_aud, (550, 50))
    gameDisplay.blit(img_aud, (1100, 50))
    #Banner
    gameDisplay.blit(banner,(0,280))

    gameDisplay.blit(line1,(0,360))
    
    #GoalPost
    imgRect = img_goalpost.get_rect()
    imgRect.center = (centre_x,193)
    gameDisplay.blit(img_goalpost,imgRect)

    imgRect = line2.get_rect()
    imgRect.center = (centre_x,465)
    gameDisplay.blit(line2,imgRect)

    gameDisplay.blit(point,(585,660))
    
    if flag:
        #Welcome To Inter NIT
        img_wc = pygame.image.load("images/welcome.png")
        ir = img_wc.get_rect()
        ir.center = (centre_x+22,540)
        gameDisplay.blit(img_wc,ir)
        
        pygame.display.update()
        cnt=0
        while cnt<100:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gExit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gExit()
                        quit()
                    elif event.key==pygame.K_SPACE:
                        cnt  = 100
            pygame.time.delay(10)
            cnt+=1

    #Background
    gameDisplay.fill(lgreen)
    gameDisplay.blit(img_sky,(0,0))
    #Audiences
    gameDisplay.blit(img_aud,(0,50))
    gameDisplay.blit(img_aud, (550, 50))
    gameDisplay.blit(img_aud, (1100, 50))
    #Banner
    gameDisplay.blit(banner,(0,280))

    gameDisplay.blit(line1,(0,360))
    
    #GoalPost
    imgRect = img_goalpost.get_rect()
    imgRect.center = (centre_x,193)
    gameDisplay.blit(img_goalpost,imgRect)

    imgRect = line2.get_rect()
    imgRect.center = (centre_x,465)
    gameDisplay.blit(line2,imgRect)

    gameDisplay.blit(point,(585,660))
    
    #Keeper
    imgRect = img_g2.get_rect()
    imgRect.center = (centre_x,307)
    gameDisplay.blit(img_g2,imgRect)
    
    #home play icon
    gameDisplay.blit(home_icn,(-21,displayHeight-80))
    
    gameDisplay.blit(img_play1,(centre_x-97,450))
    
    imgRect = img_instr.get_rect()
    imgRect.center = (centre_x,610)
    gameDisplay.blit(img_instr, imgRect)
    
    pygame.display.update()

    instruction = 0 
    while not instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gExit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    gExit()
                    quit()
                    
            elif event.type == pygame.MOUSEMOTION:                    
                if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        gameDisplay.blit(home_icn1,(-21,displayHeight-80))
                        pygame.display.update()
                else:
                    gameDisplay.blit(home_icn,(-21,displayHeight-80))
                    pygame.display.update()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= centre_x-97 and event.pos[0] <= centre_x+97 and event.pos[1] >= 450 and event.pos[1] <= 89+450:
                    gameLoop()
                elif event.pos[0] >= centre_x-438 and event.pos[0] <= centre_x+438 and event.pos[1] >= 484 and event.pos[1] <= 736:
                    instruction = 1
                elif event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                    intro()

    #Background
    gameDisplay.fill(lgreen)
    gameDisplay.blit(img_sky,(0,0))
    #Audiences
    gameDisplay.blit(img_aud,(0,50))
    gameDisplay.blit(img_aud, (550, 50))
    gameDisplay.blit(img_aud, (1100, 50))
    #Banner
    gameDisplay.blit(banner,(0,280))
    
    gameDisplay.blit(line1,(0,360))

    #GoalPost
    imgRect = img_goalpost.get_rect()
    imgRect.center = (centre_x,193)
    gameDisplay.blit(img_goalpost,imgRect)

    imgRect = line2.get_rect()
    imgRect.center = (centre_x,465)
    gameDisplay.blit(line2,imgRect)

    #gameDisplay.blit(point,(585,660))
    
    #Keeper
    imgRect = img_g2.get_rect()
    imgRect.center = (centre_x,307)
    gameDisplay.blit(img_g2,imgRect)
    
    #home play icon
    gameDisplay.blit(home_icn,(-21,displayHeight-80))
    gameDisplay.blit(back, (5,0))
    
    pygame.display.update()

    while 1:
        q = "Upper Left Shoot"
        w = "Upper Middle Shoot"
        e = "Upper Right Shoot"
        a = "Lower Left Shoot"
        s = "Lower Middle Shoot"
        d = "Lower Right Shoot"
        click = "Or Click in the respective region to Shoot"

        img_q = pygame.image.load('images/q.jpg')
        img_w = pygame.image.load('images/w.jpg')
        img_e = pygame.image.load('images/e.jpg')
        img_a = pygame.image.load('images/a.jpg')
        img_s = pygame.image.load('images/s.jpg')
        img_d = pygame.image.load('images/d.jpg')

        gameDisplay.blit(img_q,(180+40, 440-25))
        gameDisplay.blit(img_w,(550+40, 440-25))
        gameDisplay.blit(img_e,(890+40, 440-25))
        gameDisplay.blit(img_a,(180+40, 550-25))
        gameDisplay.blit(img_s,(550+40, 550-25))
        gameDisplay.blit(img_d,(890+40, 550-25))

        score_card(q, 100+40, 490-25, white)
        score_card(w, 450+40, 490-25, white)
        score_card(e, 800+40, 490-25, white)
        score_card(a, 100+40, 600-25, white)
        score_card(s, 450+40, 600-25, white)
        score_card(d, 800+40, 600-25, white)

        message_to_screen(click,white,300,size="small")

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gExit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    gExit()
                    quit()
                    
            elif event.type == pygame.MOUSEMOTION:                    
                if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        gameDisplay.blit(home_icn1,(-21,displayHeight-80))
                        pygame.display.update()
                else:
                    gameDisplay.blit(home_icn,(-21,displayHeight-80))
                    pygame.display.update()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= 5 and event.pos[0] <= 45 and event.pos[1] >= 0 and event.pos[1] <= 44:
                    instr(0)
                elif event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                    intro()



#front Screen
def intro():
    pygame.mixer.music.load("music/#Start.MP3")
    pygame.mixer.music.play(-1,0.0)
    name = "BRAZUCA"
    gameDisplay.blit(frnt_1,(0,0))

    x = 200
    i = 0
    check = [0,0,0,0,0,0,0]

    while i < 7:
        N = str("images/")+str(name[i])+str(".png")
        img = pygame.image.load(N)
        
        ang = -10
        if i%2 == 0:
            ang = 10
        img = pygame.transform.rotate(img,ang)
        
        y = -50
        while y <= centre_y-100:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    gExit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        gExit()
                        quit()
                    elif event.key==pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        instr()
            gameDisplay.blit(frnt_1,(0,0))
            j=0
            while check[j]!=0:
                N = str("images/")+str(name[j])+str(".png")
                img1 = pygame.image.load(N)
                ang = 10
                if j%2 == 0:
                    ang = -10
                img1 = pygame.transform.rotate(img1,ang)
                imgRect = img1.get_rect()
                imgRect.center = (x+80*j,centre_y-100)
                gameDisplay.blit(img1,imgRect.center)
                j+=1
            imgRect = img.get_rect()
            imgRect.center = (x+80*i,y)
            gameDisplay.blit(img,imgRect.center)
            pygame.display.update()
            pygame.time.delay(50)
            y += 50
        check[i] = 1
        i += 1
    
    cnt = 0
    while cnt<100:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                gExit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    gExit()
                    quit()
                elif event.key==pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    instr()
        pygame.time.delay(10)
        cnt+=1
    pygame.mixer.music.stop()
    instr()



#Movement after the kick
def kick(img_football, g_posi, rand_var, i, P_goals, A_goals, goal):

    by_var = int(g_posi/4)
    bx_var = (g_posi%3)

    ky_var = int(rand_var/4)
    kx_var = (rand_var%3)

    bx, by = 568, 600
    kx, ky = centre_x, 307
    
    #Upper Shot
    bychange = 25
    bylimit = 50
    #Lower Shot
    if by_var == 1:
        bychange = 15
        bylimit = 270

    #Upper estimate
    kychange = 12
    kylimit = 50
    #Lower Shot
    if ky_var == 1:
        kychange = 0.5
        kylimit = 270

    #print("For Ball = var: ",bx_var," ",by_var," limit ",bylimit," change ",bychange)
    #print("For Keeper = var: ",kx_var," ",ky_var," limit ",kylimit," change ",kychange)
    gameDisplay.blit(home_icn,(-21,displayHeight-80))
    pygame.display.update()
    
    cntr = 0
    while by > bylimit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gExit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gExit()
                        quit()
                    elif event.key==pygame.K_SPACE:
                        gameLoop()
                elif event.type == pygame.MOUSEMOTION:
                    if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        gameDisplay.blit(home_icn1,(-21,displayHeight-80))
                        pygame.display.update()
                    else:
                        gameDisplay.blit(home_icn,(-21,displayHeight-80))
                        pygame.display.update()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        intro()
        by -= bychange
        if bx_var == 1:
            bx -= 11
        elif bx_var == 0:
            bx += 11
            
        ky -= kychange
        if kx_var == 1:
            kx -= 12
        elif kx_var == 0:
            kx += 10
            
        #Background
        gameDisplay.fill(lgreen)
        gameDisplay.blit(img_sky,(0,0))
        gameDisplay.blit(lm, (centre_x-140, 450))
        #Audiences
        gameDisplay.blit(img_aud,(0,50))
        gameDisplay.blit(img_aud, (550, 50))
        gameDisplay.blit(img_aud, (1100, 50))
        #Banner
        gameDisplay.blit(banner,(0,280))

        gameDisplay.blit(line1,(0,360))
        
        #GoalPost
        imgRect = img_goalpost.get_rect()
        imgRect.center = (centre_x,193)
        gameDisplay.blit(img_goalpost,imgRect)

        imgRect = line2.get_rect()
        imgRect.center = (centre_x,465)
        gameDisplay.blit(line2,imgRect)
        gameDisplay.blit(lm, (centre_x-140, 450))
        gameDisplay.blit(point,(585,660))
        
        gameDisplay.blit(home_icn,(-21,displayHeight-80))
        #Goalkeeper of the opposite team
        if i%2 is 0:
            imgRect = img_g2.get_rect()
            imgRect.center = (kx,round(ky))
            gameDisplay.blit(img_g2,imgRect)
        else:
            imgRect = img_g1.get_rect()
            imgRect.center = (kx,round(ky))
            gameDisplay.blit(img_g1,imgRect)

        #FootBall
        gameDisplay.blit(img_football, (bx, by))
        
        #Score String
        s1 = Po + str(P_goals)
        s2 = Ar + str(A_goals)
        #Score Blit
        score_card(s2, 20, 10, black)
        score_card(s1, 1030, 10, black)
        pygame.time.delay(40)
        pygame.display.update()
        cntr += 1

    if goal:
        pygame.mixer.music.load("music/#win.MP3")
        pygame.mixer.music.play(1,0.0)
    else:
        pygame.mixer.music.load("music/#Aww.MP3")
        pygame.mixer.music.play(1,0.0)
    
    #Return to position
    while cntr > 0:
        ky += kychange
        if goal == 0:
            by += kychange
        elif cntr > 2:
            if bychange == 15:
                by += 2
            else:
                by += 12
        #Background
        gameDisplay.fill(lgreen)
        gameDisplay.blit(lm, (centre_x-140, 450))
        gameDisplay.blit(img_sky,(0,0))
        #Audiences
        gameDisplay.blit(img_aud,(0,50))
        gameDisplay.blit(img_aud, (550, 50))
        gameDisplay.blit(img_aud, (1100, 50))
        #Banner
        gameDisplay.blit(banner,(0,280))

        gameDisplay.blit(line1,(0,360))
        
        #GoalPost
        imgRect = img_goalpost.get_rect()
        imgRect.center = (centre_x,193)
        gameDisplay.blit(img_goalpost,imgRect)

        imgRect = line2.get_rect()
        imgRect.center = (centre_x,465)
        gameDisplay.blit(line2,imgRect)
        gameDisplay.blit(lm, (centre_x-140, 450))
        gameDisplay.blit(point,(585,660))
        
        gameDisplay.blit(home_icn,(-21,displayHeight-80))
        if goal == 0:
            #Goalkeeper of the opposite team
            if i%2 is 0:
                imgRect = img_g2.get_rect()
                imgRect.center = (kx,round(ky))
                gameDisplay.blit(img_g2,imgRect)
            else:
                imgRect = img_g1.get_rect()
                imgRect.center = (kx,round(ky))
                gameDisplay.blit(img_g1,imgRect)
            #FootBall
            gameDisplay.blit(img_football, (bx, by))

        else:
            #FootBall
            gameDisplay.blit(img_football, (bx, by))
            #Goalkeeper of the opposite team
            if i%2 is 0:
                imgRect = img_g2.get_rect()
                imgRect.center = (kx,round(ky))
                gameDisplay.blit(img_g2,imgRect)
            else:
                imgRect = img_g1.get_rect()
                imgRect.center = (kx,round(ky))
                gameDisplay.blit(img_g1,imgRect)

        
        #Score String
        s1 = Po + str(P_goals)
        s2 = Ar + str(A_goals)
        #Score Blit
        score_card(s2, 20, 10, black)
        score_card(s1, 1030, 10, black)
        
        cntr -= 1
        pygame.time.delay(40)
        pygame.display.update()
    pygame.mixer.music.stop()


#Actual Game Loop
def gameLoop():
    i = 0
    pi = -1
    g_posi = 0
    
    gameExit=False
    gameOver=False

    A_goals=0
    P_goals=0


    while not gameExit:
        if i == 2*Shots:
            gameOver = True
            
        Ar = "MANIT : "
        Po = "MNIT : "

        #Exit Screen
        while gameOver == True:
            gameDisplay.fill(lgreen)
            #Score String
            s1 = Po + str(P_goals)
            s2 = Ar + str(A_goals)
            #Score Blit
            score_card(s2, 20, 10, black)
            score_card(s1, 1030, 10, black)
            a = A_goals
            b = P_goals
            gameDisplay.blit(home_icn,(-21,displayHeight-80))
            if(A_goals > P_goals):
                imgRect = imgAf.get_rect()
                imgRect.center = (centre_x,centre_y - 180)
                gameDisplay.blit(imgAf,imgRect)
                message_to_screen("Wins!!", black,-50,"large")
            elif(A_goals == P_goals):
                imgRect = imgDraw.get_rect()
                imgRect.center = (centre_x,130)
                gameDisplay.blit(imgDraw,imgRect)
                message_to_screen(" It is a draw!!", black,-50,"large")
            else:
                imgRect = imgPf.get_rect()
                imgRect.center = (centre_x,centre_y - 180)
                gameDisplay.blit(imgPf,imgRect)
                a = P_goals
                b = A_goals
                message_to_screen("Wins!!", black,-50,"large")
                
            ratio = "By ("+str(a)+"-"+str(b)+")"
            message_to_screen(ratio, black,50,"medium")
            message_to_screen("Press R to restart and Esc to quit the game.", black,150,"medium")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gExit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gExit()
                        quit()
                    elif event.key==pygame.K_r:
                        gameLoop()
                elif event.type == pygame.MOUSEMOTION:
                    if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        gameDisplay.blit(home_icn1,(-21,displayHeight-80))
                        pygame.display.update()
                    else:
                        gameDisplay.blit(home_icn,(-21,displayHeight-80))
                        pygame.display.update()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        intro()
                        
            gameDisplay.blit(home_icn,(-21,displayHeight-80))
            pygame.display.update()
            

        #Background
        gameDisplay.fill(lgreen)
        gameDisplay.blit(img_sky,(0,0))

        #Audiences
        gameDisplay.blit(img_aud,(0,50))
        gameDisplay.blit(img_aud, (550, 50))
        gameDisplay.blit(img_aud, (1100, 50))

        #Banner
        gameDisplay.blit(banner,(0,280))

        gameDisplay.blit(line1,(0,360))

        #GoalPost
        imgRect = img_goalpost.get_rect()
        imgRect.center = (centre_x,193)
        gameDisplay.blit(img_goalpost,imgRect)

        imgRect = line2.get_rect()
        imgRect.center = (centre_x,465)
        gameDisplay.blit(line2,imgRect)
        
        gameDisplay.blit(lm, (centre_x-140, 450))
        gameDisplay.blit(point,(585,660))

        #FootBall
        imgRect = img_football.get_rect()
        imgRect.center = (centre_x,637)
        gameDisplay.blit(img_football,imgRect)

        gameDisplay.blit(home_icn,(-21,displayHeight-80))

        #Goalkeeper of the opposite team
        if i%2 is 0:
            imgRect = img_g2.get_rect()
            imgRect.center = (centre_x,307)
            gameDisplay.blit(img_g2,imgRect)
        else:
            imgRect = img_g1.get_rect()
            imgRect.center = (centre_x,307)
            gameDisplay.blit(img_g1,imgRect)

        #Score String
        s1 = Po + str(P_goals)
        s2 = Ar + str(A_goals)
        #Score Blit
        score_card(s2, 20, 10, black)
        score_card(s1, 1030, 10, black)

        if i is not pi:
            if i%2==0:
                #Argentina's Turn
                imgRect = imgAt.get_rect()
                imgRect.center = (centre_x,centre_y + 170)
                gameDisplay.blit(imgAt,imgRect)
                pygame.time.delay(20)
            else:
                #Portugal's Turn
                imgRect = imgPt.get_rect()
                imgRect.center = (centre_x,centre_y + 170)
                gameDisplay.blit(imgPt,imgRect)
                pygame.time.delay(20)
        else:
            #Background
            gameDisplay.fill(lgreen)
            gameDisplay.blit(lm, (centre_x-140, 450))
            gameDisplay.blit(img_sky,(0,0))

            #Audiences
            gameDisplay.blit(img_aud,(0,50))
            gameDisplay.blit(img_aud, (550, 50))
            gameDisplay.blit(img_aud, (1100, 50))

            #Banner
            gameDisplay.blit(banner,(0,280))

            gameDisplay.blit(line1,(0,360))

            #GoalPost
            imgRect = img_goalpost.get_rect()
            imgRect.center = (centre_x,193)
            gameDisplay.blit(img_goalpost,imgRect)

            imgRect = line2.get_rect()
            imgRect.center = (centre_x,465)
            gameDisplay.blit(line2,imgRect)
            
            gameDisplay.blit(lm, (centre_x-140, 450))
            gameDisplay.blit(point,(585,660))

            #FootBall
            imgRect = img_football.get_rect()
            imgRect.center = (centre_x,637)
            gameDisplay.blit(img_football,imgRect)

            #Goalkeeper of the opposite team
            if i%2 is 0:
                imgRect = img_g2.get_rect()
                imgRect.center = (centre_x,307)
                gameDisplay.blit(img_g2,imgRect)
            else:
                imgRect = img_g1.get_rect()
                imgRect.center = (centre_x,307)
                gameDisplay.blit(img_g1,imgRect)

            gameDisplay.blit(home_icn,(-21,displayHeight-80))
            #Score String
            s1 = Po + str(P_goals)
            s2 = Ar + str(A_goals)
            #Score Blit
            score_card(s2, 20, 10, black)
            score_card(s1, 1030, 10, black)

        pygame.display.update()


        #Main loop and logic

        rand_var = 0
        
        if i<2*Shots:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        gExit()
                        quit()

                    dict = {'q':1,'w':2,'e':3,'a':4,'s':5,'d':6}
                    
                    Pg = Ag = 0
                    if (event.key==pygame.K_q or event.key==pygame.K_w or event.key==pygame.K_e or event.key==pygame.K_a or event.key==pygame.K_s or event.key==pygame.K_d):
                        g_posi = dict[chr(event.key)]
                        pi = i
                        i += 1
                        goal = 1
                        rand_var = random.randrange(1, 7)
                        if rand_var != g_posi and i % 2 == 0:
                            Pg = 1
                        elif rand_var != g_posi and i % 2 == 1:
                            Ag = 1
                        else:
                            goal = 0
                        kick(img_football, g_posi, rand_var, i-1, P_goals, A_goals, goal)
                        
                        P_goals += Pg
                        A_goals += Ag
                    #print("Not in function ", g_posi," ",rand_var)
                    
                elif event.type == pygame.MOUSEMOTION:
                    if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        gameDisplay.blit(home_icn1,(-21,displayHeight-80))
                        pygame.display.update()
                    else:
                        gameDisplay.blit(home_icn,(-21,displayHeight-80))
                        pygame.display.update()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] <= 79 and event.pos[1] >= displayHeight-80:
                        intro()
                    f = 0
                    Pg = Ag = 0
                    if event.pos[0] >= 285 and event.pos[1] >= 21 and event.pos[0] <= 365 and event.pos[1] <= 101:
                        f = 1
                        g_posi = 1
                    elif event.pos[0] <= 640 and event.pos[1] >= 21 and event.pos[0] >= 560 and event.pos[1] <= 101:
                        f = 1
                        g_posi = 2
                    elif event.pos[0] <= 918 and event.pos[1] >= 21 and event.pos[0] >= 838 and event.pos[1] <= 101:
                        f = 1
                        g_posi = 3
                    elif event.pos[0] >= 285 and event.pos[1] <= 364 and event.pos[0] <= 365 and event.pos[1] >= 284:
                        g_posi = 4
                        f = 1
                    elif event.pos[0] >= 560 and event.pos[1] <= 364 and event.pos[0] <= 640 and event.pos[1] >= 284:
                        f = 1
                        g_posi = 5
                    elif event.pos[0] <= 918 and event.pos[1] <= 364 and event.pos[0] >= 838 and event.pos[1] >= 284:
                        f = 1
                        g_posi = 6
                    if f is 1:
                        pi = 1
                        goal = 1
                        i+=1
                        rand_var = random.randrange(1,7)
                        if rand_var != g_posi and i % 2 == 0:
                            Pg = 1
                        elif rand_var != g_posi and i % 2 == 1:
                            Ag = 1
                        else:
                            goal = 0
                        kick(img_football, g_posi, rand_var, i-1, P_goals, A_goals, goal)
                        P_goals += Pg
                        A_goals += Ag
                    

            pygame.display.update()
            
        pygame.event.get()
        pygame.display.update()
        clock.tick(FPS)
        pygame.time.delay(300)
        
    gExit()
    quit()

#Actual function calls
intro()
