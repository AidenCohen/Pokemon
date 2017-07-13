import time
import sys
import subprocess
from PIL import Image
from msvcrt import getch
import keyboard
from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open("n.jpg").convert('RGBA')
image1 = Image.open("Pokemon_Red_Sprite.jpg")
image2 = Image.open("images.png")
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('Pokemon GB.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity


'''
p = subprocess.Popen(["display", "n.png"])
a = subprocess.Popen(["display", "Pokemon_Red_Sprite.jpg"])
i = subprocess.Popen(["display", "images.png"])
'''
scrolling_text = []


def print_slow(str):
    for letter in str:
            if(keyboard.is_pressed('space')):
                print(letter, sep=' ', end='', flush=True)
                time.sleep(.005)
            else:
                print(letter, sep=' ', end='', flush=True)
                time.sleep(.1)


print_slow("Hello there! Welcome to the world of POKEMON! " +
" My name is OAK!" +  " People call me the POKEMON PROF!")

print_slow("This world is inhabited by creatures called POKEMON!" +
 " For some people, POKEMON are pets. Others use them for fights." +
" Myself... I study POKEMON as a profession.")

image1.show()
name = input("First, what is your name?")
#a.kill()
image2.show()
print_slow( "Right! So your name is " + name)
print_slow("This is my grandson. He's been your rival since you were a baby.")
enemyName = input( "...Erm, what is his name again?")
print_slow("That's right! I remember now! His name is " + name)
#i.kill()
image1.show()
print_slow(name + " " + "Your very own POKEMON legend is about to unfold!" +
"A world of dreams and adventures with POKEMON awaits! Let's go!")
#a.kill()
