
import random
from secrets import choice
import sys

class BallouChatAgent: #replace this with your last name, like RieffelChatAgent
   """ChatAgent - This is a very simple ELIZA-like computer program in python.
      Your assignent in Programming Assignment 1 is to improve upon it.

      I've created this as a python object so that your agents can chat with one another
      (and also so you can have some practice with python objects)
      """
  
   
   def otherReply(self,inString):
       """Pick a random function, and call it on the input string """
       randFunction = random.choice(self.ReplyFunctionList) #pick a random function, I love python
       reply = randFunction(inString) 
       return reply
 

   def driverLoop(self):
       """The main driver loop for the chat agent"""
       reply = "how are you today?"
       #print("\n")
       while True:
           response = input(reply)
           if response == "Exit":
               return False
           #reply = self.switchPerson(response)
           #reply = self.earlierReply(response)
           else:
            reply = self.generateReply(response)
           #return reply

   def swapPerson(self,inWord):
       """Replace 'I' with 'You', etc"""
       if (inWord in self.PronounDictionary.keys()):   #if the word is in the list of keys
           return self.PronounDictionary[inWord] 
       else:
           return inWord


#    def changePerson(self,inString): #this function is deliberately awful. fix it.
#        """change the pronouns etc of inString
#        by iterating through the PrononDictionary
#        and substituting keywords for subwords

#        n.b. this is an absolutely awful way of doing this
#        and you'll be asked to change it in the assignment"""
#        inWordList = str.split(inString)
#        newWordList = [] 
#        for keyword, subword in self.PronounDictionary.items(): #iterate through the dictionary
#            for word in inWordList:  #and then through the sentence
#                if (word == keyword):
#                    newWordList.append(subword)  #replace if it matches
#                else:
#                    newWordList.append(word)
#            inWordList,newWordList = newWordList,[]
#        reply = ' '.join(inWordList)  #glue things back together
#        return reply 

    #new function for change person
   def switchPerson(self, inString):
       inWordList = str.split(inString)
       updated = list(map(self.swapPerson,inWordList)) #Python Map function
       #print(list(updated))
       reply = ' '.join(updated)
       return reply

   def changePersonAndAddPrefix(self,inString):
        reply = self.switchPerson(inString)
        randomPrefix = random.choice(self.PrefixList)
        return ''.join([randomPrefix,reply])
  
   def generateHedge(self,inString):
        return random.choice(self.HedgeList)

    #Creates a reply to something the user said earlier
   def earlierReply(self, inString):
       earlierClause = random.choice(self.PrefixToEarlier)
       self.MemList.append(inString)
       prevStatement = random.choice(self.MemList)
       reply = self.switchPerson(prevStatement)
       return ' '.join([earlierClause,reply])

    #function to generate a random fact
   def generateRandomFact(self, inString):
       starter = "Did you know that"
       fact = random.choice(self.RandomFact)
       return ' '.join([starter,fact])
   

   def __init__(self):
       self.PronounDictionary = {'i':'you','I':'you','am':'are','my':'your', 'you':'i', 'you':'I', 'myself':'yourself', 'mine':'yours', 'this':'that'}
       self.HedgeList = ["Hmm","That is fascinating","Let's change the subject","Tell me more...", "It is nice to chat with you", "Lets try another topic", "I'm not sure I understand"]
       self.PrefixList = ["Why do you say that ","What do you mean that ", "How long have you been ", "Are you sure that " ]
       self.MemList = []
       self.PrefixToEarlier = ["Earlier you said that", "Earlier you mentioned","Earlier you talked about how"]
       self.RandomFact = ["dolphins sleep with one eye open?", "pigs don't sweat?", "Scottland's national animal is a unicorn?","LEGO is the biggest tire manufacturer in the world?", "a group of ferrets is called a buisness?", "peanuts are not nuts, they are legumes?"]
       self.ReplyFunctionList = [self.generateHedge,self.switchPerson,self.changePersonAndAddPrefix, self.earlierReply, self.generateRandomFact] #this is what makes Python so powerful
   #End of ChatAgent

if __name__ == '__main__': #will only be called if this is invoked directly by python, as opposed to included in a larger file
    
    #version checking
    MIN_PYTHON = (3, 7)
    assert sys.version_info >= MIN_PYTHON, "requires Python 3, run with `python3 eliza.py`"

    #program starts here
    random.seed() #if given no value, it uses system time
    agent = BallouChatAgent()
    agent.driverLoop()
