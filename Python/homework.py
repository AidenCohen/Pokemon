import sys
import pygame
import time
import keyboard
import textwrap
pygame.mixer.init()
pygame.init()
size=width, height=450, 280
speed=[1,1]
color=244,244,244
screen=pygame.display.set_mode(size)
nindorino = pygame.image.load("n.jpg")
oak = pygame.image.load("oak.jpg")
red = pygame.image.load("red.jpg")
blue = pygame.image.load("blue.jpg")


pygame.mixer.music.load('Pokemon Red Blue.mp3')
pygame.mixer.music.play(0)

pygame.event.wait()
def text_box():
    pygame.draw.rect(screen,pygame.Color("black"), (10,200,430,100), 5)
def print_slow(str,int):
    x = 0
    y = int
    for letter in str:
            if(keyboard.is_pressed('space')):
                myfont = pygame.font.SysFont("monospace", 15)
                label = myfont.render(letter, 1, (1,1,1))
                screen.blit(label, (20 + x, 220 + y))
                x = x+10
                time.sleep(.005)
                pygame.display.update()
            else:
                myfont = pygame.font.SysFont("monospace", 15)
                label = myfont.render(letter, 1, (1,1,1))
                screen.blit(label, (20 + x, 220 + y))
                x = x+10
                time.sleep(.1)
                pygame.display.update()

def text1(word,x,y):
    font = pygame.font.SysFont(None, 25)
    text = font.render("{}".format(word), True, RED)
    return screen.blit(text,(x,y))

def inpt(text, number):
    word=""
    print_slow(text, 0)
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word+=str(chr(event.key))
                    text1
                if event.key == pygame.K_b:
                    word+=chr(event.key)
                if event.key == pygame.K_c:
                    word+=chr(event.key)
                if event.key == pygame.K_d:
                    word+=chr(event.key)
                if event.key == pygame.K_e:
                    word+=chr(event.key)
                if event.key == pygame.K_f:
                    word+=chr(event.key)
                if event.key == pygame.K_g:
                    word+=chr(event.key)
                if event.key == pygame.K_h:
                    word+=chr(event.key)
                if event.key == pygame.K_i:
                    word+=chr(event.key)
                if event.key == pygame.K_j:
                    word+=chr(event.key)
                if event.key == pygame.K_k:
                    word+=chr(event.key)
                if event.key == pygame.K_l:
                    word+=chr(event.key)
                if event.key == pygame.K_m:
                    word+=chr(event.key)
                if event.key == pygame.K_n:
                    word+=chr(event.key)
                if event.key == pygame.K_o:
                    word+=chr(event.key)
                if event.key == pygame.K_p:
                    word+=chr(event.key)
                if event.key == pygame.K_q:
                    word+=chr(event.key)
                if event.key == pygame.K_r:
                    word+=chr(event.key)
                if event.key == pygame.K_s:
                    word+=chr(event.key)
                if event.key == pygame.K_t:
                    word+=chr(event.key)
                if event.key == pygame.K_u:
                    word+=chr(event.key)
                if event.key == pygame.K_v:
                    word+=chr(event.key)
                if event.key == pygame.K_w:
                    word+=chr(event.key)
                if event.key == pygame.K_x:
                    word+=chr(event.key)
                if event.key == pygame.K_y:
                    word+=chr(event.key)
                if event.key == pygame.K_z:
                    word+=chr(event.key)
                if event.key == pygame.K_1:
                    word+=chr(event.key)
                if event.key == pygame.K_2:
                    word+=chr(event.key)
                if event.key == pygame.K_3:
                    word+=chr(event.key)
                if event.key == pygame.K_4:
                    word+=chr(event.key)
                if event.key == pygame.K_5:
                    word+=chr(event.key)
                if event.key == pygame.K_6:
                    word+=chr(event.key)
                if event.key == pygame.K_7:
                    word+=chr(event.key)
                if event.key == pygame.K_8:
                    word+=chr(event.key)
                if event.key == pygame.K_9:
                    word+=chr(event.key)
                if event.key == pygame.K_RETURN:
                    done=False
                if event.key == pygame.K_RETURN and word == "" and number == True:
                    word = "Red"
                    done = False
                if event.key == pygame.K_RETURN and word == "" and number == False:
                    word = "Blue"
                    done = False
    aiden = word
    return aiden
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    screen.fill(pygame.Color("white"))
    screen.blit(oak,(140,50))
    text_box()
    print_slow("Hello there! Welcome to the world of" , 0)
    print_slow("POKEMON!" , 30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(oak,(140,50))
    print_slow("My name is OAK!" + " People call me the", 0)
    print_slow("POKEMON PROF!", 30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    screen.blit(nindorino,(140,50))
    text_box()
    print_slow("This world is inhabited by creatures", 0 )
    print_slow("called POKEMON!", 30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    screen.blit(nindorino,(140,50))
    text_box()
    print_slow( " For some people, POKEMON are pets." , 0)
    print_slow("Others use them for fights.", 30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    screen.blit(nindorino,(140,50))
    text_box()
    print_slow("Myself... I study POKEMON as a profession." , 0)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(red,(140,50))
    c = 3
    if (c==3):
        aiden = inpt("What's your name?", True)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(red,(140,50))
    print_slow("Right! So your name is " + aiden , 0)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(blue,(140,50))
    print_slow("This is my grandson. He's been your", 0)
    print_slow("rival since you were a baby.",30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(blue,(140,50))
    c = 4
    if(c == 4):
        cohen = inpt("...Erm, what is his name again?" , False)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(blue,(140,50))
    print_slow("That's right! I remember now!", 0)
    print_slow( "His name is " + cohen , 30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(red,(140,50))
    print_slow(aiden + " " + "Your very own POKEMON legend is about" , 0 )
    print_slow("to unfold!" + " A world of dreams and " , 30)
    while not keyboard.is_pressed("."):
        time.sleep(1)
    pygame.display.update()
    screen.fill(pygame.Color("white"))
    text_box()
    screen.blit(red,(140,50))
    print_slow("adventures with POKEMON awaits! Let's go!",0)

    break
pygame.quit()
