# Project 1: A Chatbot 

Question: Currently, the PronounDictionary will change first person to second person, but not vice versa. Add appropriate values to the PronounDictionary to make that happen (i.e. 'you':'i'), and test it out.   It seems a bit buggy, why?

The code is buggy because because of how changePerson() is set up. Because the code iterates through the dictionary, and then through the sentence, a bug is generating when key value pairs are introduced to change from the first person to the second person in both directions. In essence, the code loops through the inString multiple times for each key value pair in the dictionary. For example, if the sentence given is "I am good", the code will swap out the "I" with "You" (due to the pair 'I':'You') and the code will swap out "am" with "are" (due to the pair 'am':'are'), such that the sentence will be changed to "You are good". However, as the iteration continues, and the first for loop continues to rebuild the sentence for each key value pair, eventually these changes will be reverted. This is because there are also key value pairs to change from the second person back to the first person. So when the code reaches the key value pairs 'You':'I' and 'are':'am', the sentence will be changed again, turning it back into "I am good". 

IMPORTANT NOTES:
- the changePerson() function is no longer used, it is replaced with the switchPerson() function.
- the changePersonAndAddPrefix() function has also been replaced with the memoryWithPrefixAndSuffix() function. 
- the original list of prefixes have been modified to now act like suffixes (which is why changePersonAndAddPrefix() is no longer usable).
- a new list of prefixes was generated. See function documentation of memoryWithPrefixAndSuffix() for further detail.

COMMUNICATING BOTS:
- Emily and I got our two Eliza bots to talk to each other!
- The file that supports this is communicating_bots.py
- We worked on this together in person. We had Emily's Eliza file get imported into my Eliza file.
- Also, the spacing for the output lines is a little wonky, due to both of us using "\n" in our code.
  
TRANSCRIPTS:
<br>
Example 1:
- Bot: How are you today?
- User: I am good.
- Bot: You are good.
- User: You are super cool!
- Bot: My friend Siri agrees!

Example 2:
- Bot: what's your favorite color?
- User: my favorite color is purple
- Bot: I can mirror what you say: elprup si roloc etirovaf ym
- User: that very cool
- Bot: My friend Siri agrees!
- User: how are you doing today?
- Bot: I don't have an answer for that :(
- User: that's too bad
- Bot: Earlier you said how am i doing today?
- Bot: What did you mean by that?
- User: I wanted to know how your day has been
- Bot: Some time ago you said you wanted to know how my day has been
- Bot: How could you have said that?
- User: are you upset?
- Bot: Try asking me something else.
- User: it sounds like you are upset.
- Bot: it sounds like i am upset.
- User: goodbye
- Bot: I hope to talk to you again!

Example 3:
- Bot: are you a professor or a student?
- User: i am a student
- Bot: My friend Siri agrees!
- User: how did Siri know that?
- Bot: I don't have an answer for that :(
- User: that is very sketchy
- Bot: what's your spirit animal?
- User: a phenoix 
- Bot: people tell me that I'm made up of artificial intelligence... am I real?
- User: um... that is kinda hard to answer
- Bot: um... that is kinda hard to answer
- User: are you repeating me?
- Bot: Try asking me something else.
- User: what are you?
- Bot: I don't have an answer for that :(
- User: oh that is okay
- Bot: Hmm.
- User: goodbye
- Bot: I hope to talk to you again!
