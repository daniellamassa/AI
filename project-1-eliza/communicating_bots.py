
import random
import sys
from emily_bot import *

class MassaChatAgent: #replace this with your last name, like RieffelChatAgent
   """ChatAgent - This is a very simple ELIZA-like computer program in python.
      Your assignent in Programming Assignment 1 is to improve upon it.

      I've created this as a python object so that your agents can chat with one another
      (and also so you can have some practice with python objects)
      """

   def introduction(self):

       string1 = "\nHi! My name is Eliza, and I'm a virtual chatbot. I'm excited to talk with you."
       string2 = "Before we begin, there are a couple of important things you should know about my program."
       string3 = "- if you want to exit the coversation, simply type 'goodbye' and I will stop chatting with you."
       string4 = "- because I'm not perfect, avoid using contractions when responding to me. For example:"
       string5 = "      - instead of saying \"I\'m\", please use 'I am', as it will make my life easier!"
       string6 = "That being said, I have a question for you:"
       stringList = [string1, string2, string3, string4, string5, string6]
       return '\n'.join(stringList)


   def generateReply(self,inString):
       """Pick a random function, and call it on the input string """
       randFunction = random.choice(self.ReplyFunctionList) #pick a random function, I love python
       reply = randFunction(inString) + "\n"
       return reply


   def driverLoop(self):
       other_bot = BallouChatAgent()
       """The main driver loop for the chat agent"""
       reply = random.choice(self.questionList) + "\n"
       print(reply)
       response = ''
       while response != 'goodbye':
           response = other_bot.otherReply(response)
           print(response)
           isQuestion = self.detectQuestion(response)
           self.Memory.append(response)
           if isQuestion == True:
               reply = random.choice(self.questionReply) + "\n"
           else:
               reply = self.generateReply(response)
               print(reply)

       print("I hope to talk to you again!")

   def swapPerson(self,inWord):
       """Replace 'I' with 'You', etc"""
       if (inWord in self.PronounDictionary.keys()):   #if the word is in the list of keys
           return self.PronounDictionary[inWord]
       else:
           return inWord

   def switchPerson(self, inString):
       """change the pronouns etc. of inString"""
       inWordList = str.split(inString) #turn input string into a list
       newWordList = list(map(self.swapPerson,inWordList))
       return ' '.join(newWordList)

   '''
   def changePerson(self,inString): #this function is deliberately awful. fix it.
       """change the pronouns etc of inString
       by iterating through the PrononDictionary
       and substituting keywords for subwords

       n.b. this is an absolutely awful way of doing this
       and you'll be asked to change it in the assignment"""
       inWordList = str.split(inString)
       newWordList = []
       for keyword, subword in self.PronounDictionary.items(): #iterate through the dictionary
           for word in inWordList:  #and then through the sentence
               if (word == keyword):
                   newWordList.append(subword)  #replace if it matches
               else:
                   newWordList.append(word)
           inWordList,newWordList = newWordList,[]
       reply = ' '.join(inWordList)  #glue things back together
       return reply
   '''

   '''
   def changePersonAndAddPrefix(self,inString):
        """this function is no longer used because all the prefixes were
        turned into suffixes. The memory function below now accounts for prefixes,
        as well as the suffixes."""
        reply = self.switchPerson(inString)
        randomPrefix = random.choice(self.MemoryPrefixList)
        return ''.join([randomPrefix,reply])
        #return randomPrefix + '"' + reply + '"?'
   '''

   def memoryWithPrefixAndSuffix(self, inString):
        """ utilizes switchPerson() to generate proper formatting. Randomly recalls
        a previous user response (a memory), and generates a prefix and suffix in
        tangent with the memory."""
        memory = random.choice(self.Memory)
        formattedMemory = self.switchPerson(memory)
        randomPrefix = random.choice(self.MemoryPrefixList)
        randomSuffix = random.choice(self.SuffixList)
        return randomPrefix + formattedMemory + "\n" + randomSuffix


   def generateHedge(self,inString):
        return random.choice(self.HedgeList);

   def generateBackwards(self, inString):
       backwardString = inString[::-1]
       return "I can mirror what you say: " + backwardString

   def detectQuestion(self, inString):
       questionDetected = False
       for item in inString:
           if item == "?":
               questionDetected = True
           else:
               questionDetected = False
       return questionDetected

   def generateQuestion(self, inString):
       return random.choice(self.questionList)


   def __init__(self):
       self.Memory = []
       self.PronounDictionary = {
        'i':'you',
        'I':'You',
        'you':'i',
        'You':'I',
        'am':'are',
        'are':'am',
        'my':'your',
        'My':'Your',
        'your':'my',
        'Your':'My',
        }
       self.questionReply = ["That's a good question!", "I don't have an answer for that :(", "Try asking me something else."]
       self.questionList = ["how are you today?", "what's your favorite color?", "are you a professor or a student?", "what's your spirit animal?",
       "people tell me that I'm made up of artificial intelligence... am I real?"]
       self.HedgeList = ["Hmm.","That is fascinating!","Let's change the subject.","Cool!","Yikes.", "I don't understand.", "My friend Siri agrees!"]
       self.SuffixList = ["Why did you say that?", "What did you mean by that?", "How could you have said that?"]
       self.MemoryPrefixList = ["Earlier you said ", "A while ago you mentioned ", "Some time ago you said "]
       self.ReplyFunctionList = [self.generateHedge,self.switchPerson,self.memoryWithPrefixAndSuffix, self.generateBackwards, self.generateQuestion] #this is what makes Python so powerful
   #End of ChatAgent

if __name__ == '__main__': #will only be called if this is invoked directly by python, as opposed to included in a larger file

    #version checking
    MIN_PYTHON = (3, 7)
    assert sys.version_info >= MIN_PYTHON, "requires Python 3, run with `python3 eliza.py`"

    #program starts here
    random.seed() #if given no value, it uses system time
    agent = MassaChatAgent()
    #print(agent.introduction())
    agent.driverLoop()
