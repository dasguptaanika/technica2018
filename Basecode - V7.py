#Hae Rin Kim (edit)
#11/10/18
#Technica 2018

"""
Categories:
1. Deep
    a. What are your future goals?
    b. "What do you want to be when you grow up, and why?"
    c. "What's your favorite meme? Give a brief description of it for us."
    d. "What is your meaning of life?"
2. Math
    a. "What is 6 ÷2(1 + 2)?"
    b. "What is 2+0? "
    c. "If 9(x^2)+6x + 1 = (x-h)^2, find h."
    d. What is 0/0?
3. Recite a nursery rhyme
    a. Twinkle twinkle
    b. Roses are red, Violets are blue
    c. baa baa black sheep
    d. the itsy bitsy spider
4.Riddles
    a. What is often returned but is never borrowed? Thanks
    b. What do you call a famous lobster? a lobstar
    c. I have cities but no houses, moutains but no trees,
    and water but no fish. What am I? a map
    d. What month do all soldiers hate?
"""
#import
import pygame
from datetime import datetime
import random
import time
#import enchant

pygame.init()
#input
wakeUpString = input("When do you want to wake up? (Ex: YYYY-DD-MM hh:mm): ")
currentTime = datetime.now()
wakeUpTime = datetime.strptime(wakeUpString, "%Y-%m-%d %H:%M")
currentTime = currentTime.replace(second=0, microsecond=0)

#loop until time
b=0
while(b==0):
    
    #check for proper wake up time input
    if(wakeUpString[-5] == " "):
        wakeUpString = input("Enter the time so that the hour has a zero in front: ")
        wakeUpTime = datetime.strptime(wakeUpString, "%Y-%m-%d %H:%M")
    elif(wakeUpTime < currentTime):
        wakeUpString = input("That date has already passed: ")
        wakeUpTime = datetime.strptime(wakeUpString, "%Y-%m-%d %H:%M")
    else:
        currentTime = datetime.now()
        currentTime = currentTime.replace(second=0, microsecond=0)
        
        if(currentTime == wakeUpTime):
            b=1
            #anika: put your code here

