import pygame
import time
import threading
import random
pygame.init()

win=pygame.display.set_mode((1200,700))

pygame.display.set_caption("Type em All")


def Text(st,x,y,bg=(0,0,0),size=64,color=(255,255,255)):
    font = pygame.font.Font('SEASRN__.ttf', size) 
      
    text = font.render(st, True, color, bg) 
      
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
      
    # set the center of the rectangular object. 
    textRect.center = (x,y)
    win.blit(text,textRect)

def gameText(st,x,y,bg=(0,0,0)):
    font = pygame.font.Font('freesansbold.ttf', 18) 
      
    text = font.render(st, True, (255,255,255), bg) 
      
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
      
    # set the center of the rectangular object. 
    textRect.center = (x,y)
    win.blit(text,textRect)

def Play():
    ##TIMER
    global SCORE
    SCORE=0
    def TIME():
        global wordlist
        global wordpos
        global timer
        global timelevel
        global Ylist
        global TD
        TD=10
        timelevel=5
        timer=0
        wordlist={}
        Ylist=[50,100,150,200,250,300,350,400,450,500,550,600]
        while(1):
            time.sleep(timelevel)
            timer+=timelevel
            if timer>20:
                timelevel=4
            elif timer>40:
                timelevel=3
                TD=8
            elif timer>80:
                timelevel=2
                TD=5
            elif timer>150:
                timelevel=2
                TD=3
            try:
                file=open('words.txt','r')
                rand=random.randrange(1000)
                x=0
                y=random.choice(Ylist)
                for i, line in enumerate(file):
                    if i==rand:
                        wordlist[line[:-1]]=[x,y]
                file.close()        
            except:
                continue

                    
    Tthread=threading.Thread(target=TIME)
    Tthread.start()
    ##
    win.fill((0,0,0))
    Etext=''
    running=True
    while running:
        pygame.time.delay(TD)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

        win.fill((0,0,0))
        try:  
            for i in wordlist:
                x,y=wordlist[i]
                if x>1200:
                    return SCORE
                gameText(i,x,y)
                wordlist[i][0]+=1
                
        except:
            continue

       
            
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_q]:
            Etext=Etext+'q'
            time.sleep(0.13)
                        
        elif keys[pygame.K_w]:
            Etext=Etext+'w'
            time.sleep(0.13)
                        
        elif keys[pygame.K_e]:
            Etext=Etext+'e'
            time.sleep(0.13)
                        
        elif keys[pygame.K_r]:
            Etext=Etext+'r'
            time.sleep(0.13)
                        
        elif keys[pygame.K_t]:
            Etext=Etext+'t'
            time.sleep(0.13)
                        
        elif keys[pygame.K_y]:
            Etext=Etext+'y'
            time.sleep(0.13)
                        
        elif keys[pygame.K_u]:
            Etext=Etext+'u'
            time.sleep(0.13)
                        
        elif keys[pygame.K_i]:
            Etext=Etext+'i'
            time.sleep(0.13)
                        
        elif keys[pygame.K_o]:
            Etext=Etext+'o'
            time.sleep(0.13)
                        
        elif keys[pygame.K_p]:
            Etext=Etext+'p'
            time.sleep(0.13)
                        
        elif keys[pygame.K_a]:
            Etext=Etext+'a'
            time.sleep(0.13)
                        
        elif keys[pygame.K_s]:
            Etext=Etext+'s'
            time.sleep(0.13)
                        
        elif keys[pygame.K_d]:
            Etext=Etext+'d'
            time.sleep(0.13)
                        
        elif keys[pygame.K_f]:
            Etext=Etext+'f'
            time.sleep(0.13)
                       
        elif keys[pygame.K_g]:
            Etext=Etext+'g'
            time.sleep(0.13)
                        
        elif keys[pygame.K_h]:
            Etext=Etext+'h'
            time.sleep(0.13)
                        
        elif keys[pygame.K_j]:
            Etext=Etext+'j'
            time.sleep(0.13)
                        
        elif keys[pygame.K_k]:
            Etext=Etext+'k'
            time.sleep(0.13)
                        
        elif keys[pygame.K_l]:
            Etext=Etext+'l'
            time.sleep(0.13)
                       
        elif keys[pygame.K_z]:
            Etext=Etext+'z'
            time.sleep(0.13)
                        
        elif keys[pygame.K_x]:
            Etext=Etext+'x'
            time.sleep(0.13)
                        
        elif keys[pygame.K_c]:
            Etext=Etext+'c'
            time.sleep(0.13)
                        
        elif keys[pygame.K_v]:
            Etext=Etext+'v'
            time.sleep(0.13)
                        
        elif keys[pygame.K_b]:
            Etext=Etext+'b'
            time.sleep(0.13)
                        
        elif keys[pygame.K_n]:
            Etext=Etext+'n'
            time.sleep(0.13)
                        
        elif keys[pygame.K_m]:
            Etext=Etext+'m'
            time.sleep(0.13)

        elif keys[pygame.K_BACKSPACE]:
            Etext=Etext[:-1]
            time.sleep(0.13)

        elif keys[pygame.K_RETURN]:
            if Etext!="":
                try:
                    del wordlist[Etext]
                    SCORE+=5
                    Etext=''
                except:
                    continue
            time.sleep(0.13)            
        Text(Etext,600,650,size=18,color=(255,255,0))
        Text(str(SCORE),1100,30,size=18)
        pygame.display.update()
                    
                        

            
            
            

global SCORE
SCORE=0
def MENU():
    global SCORE
    SCORE=0
    HIGHSCORE=0
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

                
        ms=pygame.mouse.get_pressed()
        
        mx,my=pygame.mouse.get_pos()
        
        

        if mx>450 and mx<750 and my>200 and my<400:
            win.fill((0,0,0))
            Text("EXIT",600,500)
            pygame.draw.rect(win,(100,100,100),(450,200,300,200))
            Text("PLAY",600,300,(100,100,100))
            Text("High score:"+str(HIGHSCORE),1100,30,size=18)
            pygame.display.update()
            if ms==(1,0,0):
                SCORE=Play()
                try:
                    if HIGHSCORE<SCORE:
                        HIGHSCORE=SCORE
                except:
                    continue
        elif mx>450 and mx<750 and my>400 and my<600:
            win.fill((0,0,0))
            Text("PLAY",600,300)
            pygame.draw.rect(win,(100,100,100),(450,400,300,200))
            Text("EXIT",600,500,(100,100,100))
            Text("High score:"+str(HIGHSCORE),1100,30,size=18)
            pygame.display.update()
            if ms==(1,0,0):
                run=False
        else:
            win.fill((0,0,0))
            Text("PLAY",600,300)
            Text("EXIT",600,500)
            Text("High score:"+str(HIGHSCORE),1100,30,size=18)
            pygame.display.update()
    pygame.quit()            
            
MENU()    
    











            
