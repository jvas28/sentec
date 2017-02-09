import nltk  
import scipy
from nltk.corpus import stopwords  
from nltk import word_tokenize  
from nltk.stem import SnowballStemmer  
from string import punctuation  

spanish_stopwords = stopwords.words('spanish') 
stemmer = SnowballStemmer('spanish')

non_words = list(punctuation)  
non_words.extend(['¿', '¡'])  
non_words.extend(map(str,range(10)))

def stem(word):
    return stemmer.stem(word)

def stem_tokens(tokens):  
    stemmed = []
    for item in tokens:
        stemmed.append(stem(item))
    return stemmed

def tokenize(text):  
    text = ''.join([c for c in text if c not in non_words])
    tokens =  word_tokenize(text)
    tokens = stem_tokens(tokens)
    bigrams=[ x.lower()+"_"+y.lower() for (x,y) in zip(tokens,tokens[1:])]
    trigrams=[ x.lower()+"_"+y.lower() for (x,y) in zip(bigrams,tokens[2:])]
    tokens=[t.lower() for t in tokens ]+bigrams+trigrams	
    return tokens

