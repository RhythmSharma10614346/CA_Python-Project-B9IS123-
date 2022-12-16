#Users can ask general questions about mental health. Smart chatbot can provide some information to users by searching articles. 
#Articals have already given in txt file to chatbot.
#Users can use some keywords like 'early warnings', 'smoking', 'biological factors', 'hearing voice' etc.

import numpy as np 
import nltk
import string
import random




#import and read the corpus
f=open('whatismentalhealth.txt', 'r', errors='ignore')
raw_document=f.read()
raw_document=raw_document.lower() #for converting text to lowercase
nltk.download('omw-1.4')
nltk.download('punkt') #for using the Punkt tokenizer
nltk.download('wordnet') #for using the Wordnet dictionary
sent_tokens=nltk.sent_tokenize(raw_document) #for converting document to list of sentences. We can reach the sentences by index
word_tokens= nltk.word_tokenize(raw_document) #for converting document to list of words. We can reach the words by index

#examples
print(sent_tokens[:2])  #first 2 sentences should be printed in whatismentalhealth.txt file
print(word_tokens[:2])  #first 2 words should be printed in whatismentalhealth.txt file


#nltk.org/Text proccessing
#Lemmatization
#We have to have regular corpus data! Vectors should be organized
#Concider when sentences are broke down to he words, what is happening to the punctuation marks?
lemmer=nltk.stem.WordNetLemmatizer() #Wordnet is a semantically-oriented dictionary of English included nltk
def LemmaTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
remove_punctuation_dict=dict((ord(punct), None) for punct in string.punctuation)
def LemmaNormalize(text):
    return LemmaTokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_dict))) 



#Beginning part should have 'given words' that is going to be used randomly
#Hello function defining
Hello_Inputs=('hi', 'hello', 'how are you', 'hey', "what's up", 'are you here')
Hello_Outputs=('hi', 'hey', 'hello', 'happy to see you', 'hi thanks for talking to me')

def hello(sentence):
    for word in sentence.split():
        if word.lower() in Hello_Inputs:
            return random.choice(Hello_Outputs)


#Tf is for term frequency(How many times all the words each individual word is repeated in the corpus) 
#Idf is for inverse document frequency(how rare is the occurence of the word in the corpus)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    chatbot_response=''
    TfidfVec=TfidfVectorizer(tokenizer=LemmaNormalize, stop_words='english')
    tfidf=TfidfVec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten() 
    flat.sort()
    req_tfidf=flat[-2]
    if(req_tfidf==0): #When type in sth your chatbot doesnt understand
        chatbot_response=chatbot_response+"I am sorry! I do not understand you"
        return chatbot_response
    else:
        chatbot_response=chatbot_response+sent_tokens[idx]
        return chatbot_response

#How to start conversation and how to end 
keep_talking=True
print("Smart ChatBot: Hey! I am Smart Bot. Do you want to learn about MENTAL HEALTH? Let's ask me! If you want to exit, just type Bye")
while(keep_talking==True):
    user_response=input()
    user_response=user_response.lower()
    if(user_response!='bye'): 
        if(user_response=='thanks' or user_response=='thank you'):
            keep_talking=False
            print("Smart ChatBot: It was pleasure for me..")
        else:                                                               #else>>if user_response is any hello word which chatbot knows
            if(hello(user_response)!=None):
                print("Smart ChatBot:"+hello(user_response))
            else:                                                           #else>>if user_response is not 'bye' or is not 'thanks' or is not 'hello'
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("Smart ChatBot: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:                                                                   #else>>if user_response is "bye"
        keep_talking=False
        print("Smart ChatBot: Thanks for asking, bye! Take care")