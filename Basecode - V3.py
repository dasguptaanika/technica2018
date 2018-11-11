#Anika Dasgupta
#Technica 2018
#Code analysis


import enchant
import random
import time


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
import random
import time
category = "null"
choice1 = random.randint(0,3)
choice2 = random.randint(0,3)
print("Good Morning sunshine! This morning, you will have to: ")
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

#Math
      
elif choice1 == 1:
      print("Solve a math problem! Make sure you solve it right! Hit enter to continue.")
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

#Nursery Rhyme

elif choice1 == 2:
      category = "Nursery rhyme"
      print("Enter a nursery rhyme! Hit enter to continue.")
      if(choice2 == 0):
          rhyme = "***Twinkle Twinkle Little Star***: "
          corrAnswer = ("twinkle twinkle little star how I wonder what you are up above the world so high like a diamond in the sky twinkle twinkle little star how I wonder what you are").split()
      elif(choice2 == 1):
          rhyme = "Baa Baa Black Sheep! "
          corrAnswer = ("baa baa black sheep have you any wool yes sir yes sir three bags full one for the master one for the dame one for the little boy who lives down the lane").split()
      elif(choice2 == 2):
          rhyme = "The Itsy Bitsy Spider! "
          corrAnswer = ("the itsy bitsy spider climbed up the waterspout down came the rain and washed the spider out out came the sun and dried up all the rain and the itsy bitsy spider climbed up the spout again").split()
      else:
          rhyme = "Roses are red: "
          corrAnswer = ("roses are red violets are blue sugar is sweet and so are you").split()

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
                if(wordlist[x] not in finalList):
                    finalList.append(wordlist[x])
            if(len(finalList)>=10):
                minwords = True
            else:
                input("Your answer must be thorough and detailed, containing more than 10 unique words. Try again. ")
                time.sleep(0.5)
                words = input(phrase)
                wordlist = words.split();
                listlen = len(wordlist)
                finalList = []

            #Figuring out if the words are english words
            d = enchant.Dict("en_US")
            english = True
            for(word) in (wordlist):
                accuracy = d.check(word)
                english =(english and accuracy)
            if(english == False):
                input("What you put was not in common english. Try again. ")
                time.sleep(0.5)
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
                    time.sleep(0.5)
                    words = input(phrase)
                    wordlist = words.split();
                    listlen = len(wordlist)
                    finalList = []
        #Stop music      
        print("Good job! Time to get ready for the day!")
        condition = False

#
#
#Math
#
#
elif(category == "Math"):
    answer = str(input(problem))
    while(answer!=corrAnswer):
        print("Oopsie...wrong! Try again! ")
        time.sleep(0.5)
        answer = str(input(problem))
    print("Great job! Now, go conquer this day!")

    

#
#
#Nursery rhymes!
#
#
elif(category == "Nursery rhyme"):
    print("Note: No numbers")
    answer = ((str(input(rhyme))).lower()).split()
    correct = True
    for word in answer:
        if (word) in (corrAnswer):
            correct = correct and True
        else:
            correct = correct and False
    while(correct!=True):
        print("Oopsie...wrong! Try again! ")
        time.sleep(0.5)
        answer = str(input(rhyme))
    print("Great job! Have a nice day!")



#
#
#Riddles
#
#
else:
    answer = str(input(riddle))
    while(answer not in corrAnswer):
        print("Oopsie...wrong! Try again! ")
        time.sleep(0.5)
        answer = str(input(riddle))
    print("Great job! Now, go conquer this day!")
    
        
