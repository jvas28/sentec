import nltk  
from nltk.corpus import stopwords  
from nltk import word_tokenize  
from nltk.stem import SnowballStemmer  
from string import punctuation  
stopwords=stopwords.words('spanish')
# inicializar el extractor de raices lexicales
stemmer = SnowballStemmer('spanish')
# inicializar la lista de palabras ignoradas 
non_words = list(punctuation)  
# agregar a la lista los signos de apertura y los digitos [1-9]
non_words.extend(['¿', '¡'])  
non_words.extend(map(str,range(10)))

# funcion de extraccion de raices lexicales
def stem(word):
    return stemmer.stem(word)

# funcion de extraccion de raices lexicales sobre una lista
def stem_tokens(tokens):  
    stemmed = []
    for item in tokens:
        stemmed.append(stem(item))
    return stemmed
# funcion de disgregacion de palabras 
'''
    Separa las palabras y construye expresiones multipalabras
'''
def tokenize(text):  
    qgrams=[];
    trigrams=[];
    bigrams=[];
    text=text.lower()
    text = ''.join([c for c in text if c not in non_words])
    unigrams =  word_tokenize(text)
    #tokens = [t for t in tokens if t not in stopwords]
    if len(unigrams)>1:
        bigrams=[ x.lower()+"_"+y.lower() for (x,y) in zip(unigrams,unigrams[1:])]
    if len(unigrams)>2:
        trigrams=[ x.lower()+"_"+y.lower() for (x,y) in zip(bigrams,unigrams[2:])]
    if len(unigrams)>3:
        qgrams=[ x.lower()+"_"+y.lower() for (x,y) in zip(trigrams,unigrams[3:])]
    tokens=qgrams+trigrams+bigrams+unigrams
    tokens = stem_tokens(tokens)
    return tokens