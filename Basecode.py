#Anika Dasgupta
#Technica 2018
#Code analysis


#Input
#There will be more code for this later, when we decide on input stuff
import enchant
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
    repeatedWords = []

    #Figuring out if the words are unique
    uniqueness = False
    minwords = False
    while((uniqueness == False)and(minwords == False)):
        flag = 0
        print(wordlist)
        for x in range(listlen):
            if(wordlist[x] not in finalList):
                finalList.append(wordlist[x])
                uniqueness = True
                if(len(finalList)>=10):
                    minwords = True
                    print("success!")
                else:
                    input("Your answer must be thorough and detailed, containing \
more than 10 unique words.")
                    phrase = "Hello! What do you plan to achieve in your life?"
                    words = input(phrase)
                    wordlist = words.split();
                    listlen = len(wordlist)
                    finalList = []
                
        print(finalList)
    input("Press enter")
    

