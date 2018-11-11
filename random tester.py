#Random stuff
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
      elif(choice2 == 1):
          problem = "What is 2+0? "
      elif(choice2 == 2):
          problem = "If 9(x^2)+6x + 1 = (x-h)^2, find h."
      else:
          problem = "What is 0/0?"

#Nursery Rhyme

elif choice1 == 2:
      category = "Nursery rhyme"
      print("Enter a nursery rhyme! Enter it without all punctuation. Hit enter to continue.")
      if(choice2 == 0):
          rhyme = "***Twinkle Twinkle Little Star***: "
      elif(choice2 == 1):
          rhyme = "Baa Baa Black Sheep! "
      elif(choice2 == 2):
          rhyme = "The Itsy Bitsy Spider! "
      else:
          rhyme = "Roses are red: "

#Riddles!
    
else:
      category = "Riddles"
      print("Solve a riddle! Hit enter to continue.")
      if(choice2 == 0):
          riddle = "What is often returned but is never borrowed? "
      elif(choice2 == 1):
          riddle = "What do you call a famous lobster? a => (Finish the answer) "
      elif(choice2 == 2):
          riddle = "I have cities but no houses, moutains but no trees, and water but no fish. What am I? a => (Finish the answer)"
      else:
          riddle = "What month do all soldiers hate?"





        
