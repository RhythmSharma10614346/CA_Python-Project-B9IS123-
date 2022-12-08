import numpy as np 
import nltk
import string
import random

#import and read the corpus
f=open('whatismentalhealth.txt', 'r', errors='ignore')
raw_document=f.read()
raw_document=raw_document.lower() #for converting text to lowercase
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


