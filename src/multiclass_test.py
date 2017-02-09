import classifiers.multiclass_classifier as mc_classifier
import classifiers.enhanced_multiclass_classifier as emc_classifier
import nlp.spanish as language_tools
import matplotlib.pyplot as plot
import matplotlib.animation as animation
from matplotlib import style
import nltk
from data.resources import getDataCollection

style.use("dark_background")
plot.title("Comparacion Algortimos Multiclase")
classified_words={"basic":0,"enhanced":0}
sentiment_sum={"basic":0,"enhanced":0}
classification_features={"basic":[],"enhanced":[]}
def classifyTweets(classifier_module,tweets,plt,line_color,name):
	classifier=classifier_module.getClassifier()
	x=0
	y=0
	xar=[]
	yar=[]
	word_list=classifier_module.getWordList()
	for t in tweets:
		tokens=language_tools.tokenize(t)
		for word in tokens:
			if word in word_list:
				classified_words[name] += 1
				sent=int(classifier.classify(classifier_module.extract_feature(word)))
				classification_features[name].append((classifier_module.extract_feature(word),sent))
				y += sent-3
				sentiment_sum[name] += sent
					

		x += 1
		xar.append(x)
		yar.append(y)
	plt.plot(xar,yar,line_color)
	



result=getDataCollection()
tweets=[t["msg"] for t in result]
#tweets=list(set(tweets))
print("********Inicio de Test********")
print("Cantidad Tweets a Evaluar:"+str(len(tweets)))
classifyTweets(mc_classifier,tweets,plot,"g","basic")
classifyTweets(emc_classifier,tweets,plot,"b","enhanced")
#classifyTweets(emc_classifier,tweets,plot)
print("Sentimiento segun Classificador Multiclase Basico: "+str(sentiment_sum["basic"]/classified_words["basic"]))
print("Sentimiento segun Classificador Multiclase Mejorado: "+str(sentiment_sum["enhanced"]/classified_words["enhanced"]))
print("Palabras reconocidas Clasificador Multiclase Basico: "+str(classified_words["basic"]))
print("Palabras reconocidas Clasificador Multiclase Mejorado: "+str(classified_words["enhanced"]))
print("Precision Clasificador Multiclase Basico contra Mejorado: ",(nltk.classify.accuracy(mc_classifier.getClassifier(),classification_features["enhanced"]))*100)
plot.show()