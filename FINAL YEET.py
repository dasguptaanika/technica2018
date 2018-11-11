#Anika Dasgupta
#Technica 2018
#Code analysis

import pygame
import enchant
import random
import time
import pygame.mixer
from datetime import datetime

"""

Categories:

1. Deep
    a. What are your future goals?
    b. "What do you want to be when you grow up, and why?"
    c. "What's your favorite meme? Give a brief description of it for us."
    d. "What is your meaning of life?"

    Music:
    a. Guile theme
    b. What does the fox say

2. Math
    a. "What is 6 ÷2(1 + 2)?"
    b. "What is 2+0? "
    c. "If 9(x^2)+6x + 1 = (x-h)^2, find h(no spaces)"
    d. What is 0/0?

     Music:
    a. ?
    b. ?
    
3. Recite a nursery rhyme
    a. Twinkle twinkle
    b. Roses are red, Violets are blue
    c. baa baa black sheep
    d. the itsy bitsy spider

     Music:
    a. Baby shark
    b. duck song
    
4.Riddles
    a. What is often returned but is never borrowed? Thanks
    b. What do you call a famous lobster? a lobstar
    c. I have cities but no houses, moutains but no trees,
    and water but no fish. What am I? a map
    d. What month do all soldiers hate?

     Music:
    a. dhmis
    b. tacos?

"""

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
            category = "null"
            choice1 = random.randint(0,3)
            choice2 = random.randint(0,3)
            print("WAKEY WAKEY! This morning, you will have to: ")
            pygame.mixer.init()
            num = random.randint(0,1)
            time.sleep(1)


            #Deep

            if choice1 == 0:
                  
                  print("Respond to a deep question! Make sure you answer with detail! Hit enter to continue.")
                  category = "Deep"
                  if(choice2 == 0):
                      phrase = "What are your future goals?"
                  elif(choice2 == 1):
                      phrase = "What do you want to be when you grow up, and why?"
                  elif(choice2 == 2):
                      phrase = "What's your favorite meme? Give a brief description of it for us."
                  else:
                      phrase = "What is the meaning of life?"

                  #Pygame music stuff
                  if (num == 0):
                        audio = "guile.mp3"
                  else:
                        audio = "fox.mp3"
                  pygame.mixer.music.load(audio)
                  pygame.mixer.music.play(-1)

            #Math
                  
            elif choice1 == 1:
                  print("Solve a math problem! Make sure you solve it right! No spaces! Hit enter to continue.")
                  category = "Math"
                  if(choice2 == 0):
                      problem = "What is 6 ÷2(1 + 2)?"
                      corrAnswer = "9"
                  elif(choice2 == 1):
                      problem = "What is 2+0? "
                      corrAnswer = "2"
                  elif(choice2 == 2):
                      problem = "If 9(x^2)+6x + 1 = (ax-h)^2, find a and h and enter them in the form (a,h)."
                      corrAnswer = "(3,-1)"
                  else:
                      problem = "What is 0/0?"
                      corrAnswer = "undefined"
                      
                  #Pygame music stuff
                  if (num == 0):
                        audio = "qf.mp3"
                  else:
                        audio = "pi.mp3"
                  pygame.mixer.music.load(audio)
                  pygame.mixer.music.play(-1)


            #Nursery Rhyme

            elif choice1 == 2:
                  category = "Nursery rhyme"
                  print("Enter a nursery rhyme(the entire thing)! No punctuation! Hit enter to continue.")
                  if(choice2 == 0):
                      rhyme = "***Twinkle Twinkle Little Star***: "
                      corrAnswer = ("twinkle twinkle little star how I wonder what you are up above the world so high like a diamond in the sky twinkle twinkle little star how I wonder what you are").lower()
                  elif(choice2 == 1):
                      rhyme = "Baa Baa Black Sheep! "
                      corrAnswer = ("baa baa black sheep have you any wool yes sir yes sir three bags full one for the master one for the dame one for the little boy who lives down the lane").lower()
                  elif(choice2 == 2):
                      rhyme = "The Itsy Bitsy Spider! "
                      corrAnswer = ("the itsy bitsy spider climbed up the waterspout down came the rain and washed the spider out out came the sun and dried up all the rain and the itsy bitsy spider climbed up the spout again").lower()
                  else:
                      rhyme = "Roses are red: "
                      corrAnswer = ("roses are red violets are blue sugar is sweet and so are you").lower()
                  
                  #Pygame music stuff
                  if (num == 0):
                        audio = "baby_shark.mp3"
                  else:
                        audio = "dhmis.mp3"
                  pygame.mixer.music.load(audio)
                  pygame.mixer.music.play(-1)

                  
            #Riddles!
                
            else:
                  category = "Riddles"
                  print("Solve a riddle! The answer will be a single word. Hit enter to continue.")
                  if(choice2 == 0):
                      riddle = "What is often returned but is never borrowed? "
                      corrAnswer = "thanks"
                  elif(choice2 == 1):
                      riddle = "What do you call a famous lobster? "
                      corrAnswer = "lobstar"
                  elif(choice2 == 2):
                      riddle = "I have cities but no houses, moutains but no trees, and water but no fish. What am I? "
                      corrAnswer = "map"
                  else:
                      riddle = "What month do all soldiers hate?"
                      corrAnswer = "march"

                  #Pygame music stuff
                  if (num == 0):
                        audio = "tacos.mp3"
                  else:
                        audio = "duck.mp3"
                  pygame.mixer.music.load(audio)
                  pygame.mixer.music.play(-1)



            punctuation = [".",",","?","/", "\\", ":", ";", "\"", "(", ")", "\'"]


            #
            #
            #Deep category
            #
            #
            if(category=="Deep"):
                condition = True
                while(condition == True):
                    words = input(phrase)
                    wordlist = words.split();
                    listlen = len(wordlist)
                    finalList = []

                    #Figuring out if the words are unique
                    minwords = False
                    english = False
                    while((minwords==False)or(english == False)):
                        #Making sure the words are enough
                        for x in range(listlen):
                            if((wordlist[x] not in finalList)and(wordlist[x] not in punctuation)):
                                finalList.append(wordlist[x])
                        if(len(finalList)>=10):
                            minwords = True
                        else:
                            input("Your answer must be thorough and detailed, containing more than 10 unique words. Try again. ")
                            time.sleep(1)
                            words = input(phrase)
                            wordlist = words.split();
                            listlen = len(wordlist)
                            finalList = []

                        #Figuring out if the words are english words
                        wrong = []
                        d = enchant.Dict("en_US")
                        english = True
                        for(word) in (wordlist):
                              accuracy = d.check(word)
                              if accuracy == False:
                                    wrong.append(word)
                              english =(english and accuracy)
                        if(english == False):
                              print("This is apparently not the formal english language. The words you got wrong were: ")
                              for n in wrong:
                                    print(n)
                              print("Try again. ")
                              time.sleep(1)
                              words = input(phrase)
                              wordlist = words.split();
                              listlen = len(wordlist)
                              finalList = [] 
                        else:
                            for x in range(listlen):
                                if(wordlist[x] not in finalList):
                                    finalList.append(wordlist[x])
                            if(len(finalList)>=10):
                                minwords = True
                            else:
                                input("Your answer must be thorough and detailed, containing more than 10 unique words. Try again. ")
                                time.sleep(1)
                                words = input(phrase)
                                wordlist = words.split();
                                listlen = len(wordlist)
                                finalList = []
                    #Stop music      
                    print("Good job! Time to get ready for the day!")
                    condition = False
                    pygame.mixer.music.stop()

            #
            #
            #Math
            #
            #
            elif(category == "Math"):
                  answer = str(input(problem))
                  while(answer!=corrAnswer):
                      print("Oopsie...wrong! Try again! ")
                      time.sleep(1)
                      answer = str(input(problem))

                  #Stop music
                  print("Great job! Now, go conquer this day!")
                  pygame.mixer.music.stop()

                

            #
            #
            #Nursery rhymes!
            #
            #
            elif(category == "Nursery rhyme"):
                  print("Note: No numbers")
                  answer = (input(rhyme))
                  correct = True
                  for word in answer:
                      if (word) in (corrAnswer):
                          correct = correct and True
                      else:
                          correct = correct and False
                  while(correct == False):
                      print("Oopsie...wrong! Try again! ")
                      time.sleep(1)
                      answer = str(input(rhyme))

                  #Stop music      
                  print("Great job! Have a nice day!")
                  pygame.mixer.music.stop()



            #
            #
            #Riddles
            #
            #
            else:
                  answer = str(input(riddle))
                  while(answer not in corrAnswer):
                      print("Oopsie...wrong! Try again! ")
                      time.sleep(1)
                      answer = str(input(riddle))
                  print("Great job! Now, go conquer this day!")
                  pygame.mixer.music.stop()
                
                    
