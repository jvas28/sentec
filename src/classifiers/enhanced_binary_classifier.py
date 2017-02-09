import nltk
import pickle
import os
from nlp.spanish import stem 

def extract_feature(w):
	return {"word":w}


lexicon_lines=open("../res/lexicons/binary_lexicon.txt","r", encoding='utf-8').readlines();
lexicon_lines_enhance=open("../res/lexicons/ecuador_binary_lexicon.csv","r", encoding='mbcs').readlines();
classifier_file_name="../res/training/enhanced_binary_classifier.pickle"

labeled_words=[]
word_list=[]

#construct features
for line in lexicon_lines:
	split=line.replace("\n","").split("\t");
	word=stem(split[0].strip().replace(" ","_"))
	word_list.append(word);
	labeled_words.append((word,split[2]))
for line in lexicon_lines_enhance:
	split=line.replace("\n","").split(";");
	word=stem(split[0].strip().replace(" ","_"))
	word_list.append(word);
	labeled_words.append((word,split[1]))

feature_set=[(extract_feature(n), sentiment) for (n, sentiment) in labeled_words]

def getClassifier():
	if not (os.path.isfile(classifier_file_name)):
		classifier = nltk.NaiveBayesClassifier.train(feature_set)
		f = open(classifier_file_name, 'wb')
		pickle.dump(classifier, f)
		f.close();
	else:
		f = open(classifier_file_name, 'rb')
		classifier = pickle.load(f)
		f.close()
	return classifier

def getFeatureSet():
	return feature_set
def getWordList():
	return word_list
