#Hae Rin Kim
#11/10/18
#Technica 2018


#import
import pygame
from datetime import datetime

pygame.init()

#input
wakeUpTime = input("When do you want to wake up? (Ex: 2018-05-03 17:45): ")
audio = input("Enter the name of an audio file (mp3): ")

currentTime = datetime.now()

question = "What do you want to do with your life? "

#loop
a=0
while(a==0):
    if(audio[-4:-1] == ".mp3"):

        b=0
        while(b==0):
            if(currentTime == wakeUpTime[0:16]):
                pygame.mixer.music.load(audio)
                pygame.mixer.music.play(0)

                c=0
                while(c==0):
                    userAnswer = input(question)
                    #put answer checking code here
                    check=1     #check=1 if answer is good

                    if(check==1):
                        pygame.mixer.music.stop()
                        c=1

                    
                
            else:
                b=0

        a=1
    else:
        print("Enter the name of an mp3 file: ")
