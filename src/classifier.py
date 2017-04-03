import nltk
import pickle
import os
# Del modulo creado en la Parte I del microcurso importamos la funcion stem
from es_nlp import stem 

# Declaramos las las rutas de los archivos de lexico y clasificador
classifier_file="../res/train/classifier.pickle"
lexicon_file="../res/lexicon/sdal_lexicon.csv"

global nbclassifier
global known_words
# funcion para extraer caracteristicas para el clasificador
def extract_feature(w):
	return {"word":w}

# funcion que construye el set para entrenamiento del algoritmo clasificador
# lexico para el entrenamiento
lexicon_lines=open(lexicon_file,"r", encoding='utf-8').readlines();
labeled_words=[]
known_words=[]
for line in lexicon_lines:
	split=line.replace("\n","").split(";")
	word=split[0].split("_")
	word=stem(word[0])
	known_words.append(word)
	labeled_words.append((word,split[1]))
feature_set=[(extract_feature(n), sentiment) for (n, sentiment) in labeled_words]

# Para evitar crear y entrenar el clasificador una y otra vez 
# usamos pickle para grabar el objeto entrenado como archivo binario
if not (os.path.isfile(classifier_file)):
	nbclassifier = nltk.NaiveBayesClassifier.train(feature_set)
	f = open(classifier_file, 'wb')
	pickle.dump(nbclassifier, f)
	f.close();
else:
	f = open(classifier_file, 'rb')
	nbclassifier = pickle.load(f)
	f.close()
