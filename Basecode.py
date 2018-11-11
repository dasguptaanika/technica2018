#Anika Dasgupta
#Technica 2018
#Code analysis


#Input
#There will be more code for this later, when we decide on input stuff

phrase = "Hello! What do you plan to achieve in your life?"
words = input(phrase)
wordlist = words.split();
listlen = len(wordlist)
finalList = []

#Figuring out if the words are unique
wordlist.sort()
flag = 0
print(wordlist)
for x in range(listlen):
    if(wordlist[x] not in finalList):
        finalList.append(wordlist[x])
input("press enter to exit!")
