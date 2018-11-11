#Anika Dasgupta
#Technica 2018
#Code analysis


#Input
#There will be more code for this later, when we decide on input stuff
import enchant
import random

condition = True
while(condition == True):
    """
    Code that plays a song
    """
    phrase = "Hello! What do you plan to achieve in your life?"
    words = input(phrase)
    wordlist = words.split();
    listlen = len(wordlist)
    finalList = []

    #Figuring out if the words are unique
    minwords = False
    while(minwords==False):
        for x in range(listlen):
            if(wordlist[x] not in finalList):
                finalList.append(wordlist[x])
        if(len(finalList)>=10):
            minwords = True
        else:
            input("Your answer must be thorough and detailed, containing\
more than 10 unique words. Press enter to continue. ")
            phrase = "Hello! What do you plan to achieve in your life?"
            words = input(phrase)
            wordlist = words.split();
            listlen = len(wordlist)
            finalList = []

    #Figuring out if the words are english words
    english = False
    while(english == False):
        d = enchant.Dict("en_US")
        english = True
        for(word) in (wordlist):
            accuracy = d.check(word)
            english =(english and accuracy)
        if(english == False):
            input("What you put was not in common english. Press enter to try again. ")
            phrase = "Hello! What do you plan to achieve in your life?"
            words = input(phrase)
            wordlist = words.split();
            listlen = len(wordlist)
            finalList = [] 
        else:
            print("Good job! You can speak in english!")
    print("you have terminated")    
        
    print(finalList)
    input("Press enter")
        

