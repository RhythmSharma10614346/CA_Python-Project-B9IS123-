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