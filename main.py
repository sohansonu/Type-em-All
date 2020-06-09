import pygame
import time
import threading
import random
from playsound import playsound
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
    TD=10
    SCORE=0
    def sound1():
        playsound("sounds\gamesound.mp3")
    def sound2():
        playsound("sounds\gamesound2.mp3")
    def TIME():
        global wordlist
        global wordpos
        global timer
        global timelevel
        global Ylist
        global TD
        global speed 
        TD=10
        timelevel=5
        timer=0
        wordlist={}
        Ylist=[50,100,150,200,250,300,350,400,450,500,550,600]
        while(1):
            time.sleep(timelevel)
            timer+=timelevel
            if timer>200:
                speed=15
            elif timer>190:
                speed=14
            elif timer>180:
                speed=12
            elif timer>170:
                speed=10
            elif timer>160:
                speed=8
            elif timer>150:
                timelevel=1
                TD=1
                speed=6
            elif timer>80:
                timelevel=2
                TD=2
                speed=4
            elif timer>40:
                timelevel=3
                TD=5
                speed=3
            elif timer>20:
                timelevel=4
                TD=7
                speed=2
            
            try:
                
                file=open('words.txt','r')
                rand=random.randrange(1000)
                x=0
                try:
                    Ylist.remove(y)
                except:
                    Ylist=[50,100,150,200,250,300,350,400,450,500,550,600]
                y=random.choice(Ylist)
                Ylist=[50,100,150,200,250,300,350,400,450,500,550,600]
                for i, line in enumerate(file):
                    if i==rand:
                        wordlist[line[:-1]]=[x,y]
                file.close()        
            except:
                continue

                    
    Tthread=threading.Thread(target=TIME)
    Sthread2=threading.Thread(target=sound2)
    Tthread.start()
    Sthread2.start()
    ##
    
    win.fill((0,0,0))
    speed=1
    Etext=''
    running=True
    while running:
        pygame.time.delay(TD)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                
        
                if event.key == pygame.K_q:
                    Etext=Etext+'q'
                    
                                
                elif event.key == pygame.K_w:
                    Etext=Etext+'w'
                    
                                
                elif event.key == pygame.K_e:
                    Etext=Etext+'e'
                    
                                
                elif event.key == pygame.K_r:
                    Etext=Etext+'r'
                    
                                
                elif event.key == pygame.K_t:
                    Etext=Etext+'t'
                    
                                
                elif event.key == pygame.K_y:
                    Etext=Etext+'y'
                    
                                
                elif event.key == pygame.K_u:
                    Etext=Etext+'u'
                    
                                
                elif event.key == pygame.K_i:
                    Etext=Etext+'i'
                    
                                
                elif event.key == pygame.K_o:
                    Etext=Etext+'o'
                    
                                
                elif event.key == pygame.K_p:
                    Etext=Etext+'p'
                    
                                
                elif event.key == pygame.K_a:
                    Etext=Etext+'a'
                    
                                
                elif event.key == pygame.K_s:
                    Etext=Etext+'s'
                    
                                
                elif event.key == pygame.K_d:
                    Etext=Etext+'d'
                    
                                
                elif event.key == pygame.K_f:
                    Etext=Etext+'f'
                    
                               
                elif event.key == pygame.K_g:
                    Etext=Etext+'g'
                    
                                
                elif event.key == pygame.K_h:
                    Etext=Etext+'h'
                    
                                
                elif event.key == pygame.K_j:
                    Etext=Etext+'j'
                    
                                
                elif event.key == pygame.K_k:
                    Etext=Etext+'k'
                    
                                
                elif event.key == pygame.K_l:
                    Etext=Etext+'l'
                    
                               
                elif event.key == pygame.K_z:
                    Etext=Etext+'z'
                    
                                
                elif event.key == pygame.K_x:
                    Etext=Etext+'x'
                    
                                
                elif event.key == pygame.K_c:
                    Etext=Etext+'c'
                    
                                
                elif event.key == pygame.K_v:
                    Etext=Etext+'v'
                    
                                
                elif event.key == pygame.K_b:
                    Etext=Etext+'b'
                    
                                
                elif event.key == pygame.K_n:
                    Etext=Etext+'n'
                    
                                
                elif event.key == pygame.K_m:
                    Etext=Etext+'m'
                    

                elif event.key == pygame.K_BACKSPACE:
                    Etext=Etext[:-1]
                    

                elif event.key == pygame.K_RETURN:
                    if Etext!="":
                        try:
                            del wordlist[Etext]
                            SCORE+=5
                            Etext=''
                            Sthread=threading.Thread(target=sound1)
                            Sthread.start()
                            
                        except:
                            continue
                     

        win.fill((0,0,0))
        try:  
            for i in wordlist:
                x,y=wordlist[i]
                if x>1200:
                    return SCORE
                gameText(i,x,y)
                wordlist[i][0]+=speed
                
        except:
            continue

       
            
                   
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
