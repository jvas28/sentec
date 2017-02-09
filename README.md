# Sentimiento Ecuatoriano (SENTEC)

Es un conjunto de herramientas para Análisis de Sentimiento basado en Léxicos programada en Python. Creada en base a un estudio del léxico ecuatoriano y la incidencia que pueden tener las expresiones idiomáticas sobre la presición de los algoritmos de Análisis de Sentimiento de la Universidad Católica Santiago de Guayaquil.

## Requerimientos:
- Python 3.X
- NLTK
- Requests 
- Matplotlib

## Ejemplos 
### 1. Clasificador básico
```python
import classifiers.enhanced_binary_classifier as b_classifier
from nlp.spanish import stem
word = input()
classifier = b_classifier.getClassifier()
print(classifier.classify(b_classifier.extract_feature(stem(word))))
```
### 2. Descargando Tweets
- Actualizar en twitter_api/client.py las credenciales del app de twitter
```
cd twitter_api
python get_tweets.py
```
- Ingresar la cuenta de twitter para obtener los tweets. 

### 3. Comparando resultado de clasificadores

```python

import classifiers.binary_classifier as b_classifier
import classifiers.enhanced_binary_classifier as eb_classifier
import nlp.spanish as language_tools
import matplotlib.pyplot as plot
import matplotlib.animation as animation
from matplotlib import style
import nltk
from data.resources import getDataCollection
style.use("dark_background")
plot.title("Comparacion Algortimos Binarios")
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
		sentiment_word_count=0
		sum_sentiment=0
		for word in tokens:
			if word in word_list:
				classified_words[name] += 1
				sentiment_word_count += 1
				sentiment=classifier.classify(classifier_module.extract_feature(word))
				classification_features[name].append((classifier_module.extract_feature(word),sentiment))
				if sentiment=="pos":
					sentiment_sum[name] += 1
					y+=1
				else:
					y-=1
		x += 1
		xar.append(x)
		yar.append(y)
	plt.plot(xar,yar,line_color)
	
result=getDataCollection()
tweets=[t["msg"] for t in result]
#tweets=list(set(tweets))
print("********Inicio de Test********")
print("Cantidad Tweets a Evaluar:"+str(len(tweets))+"\n")
classifyTweets(b_classifier,tweets,plot,"g","basic")
classifyTweets(eb_classifier,tweets,plot,"b","enhanced")
print("Sentimiento segun Classificador Binario Basico: "+str(sentiment_sum["basic"]/classified_words["basic"]))
print("Sentimiento segun Classificador Binario Mejorado: "+str(sentiment_sum["enhanced"]/classified_words["enhanced"]))
#classifyTweets(emc_classifier,tweets,plot)
print("Palabras reconocidas Clasificador Binario Basico: "+str(classified_words["basic"]))
print("Palabras reconocidas Clasificador Binario Mejorado: "+str(classified_words["enhanced"]))
print("Precision Clasificador Binario Basico contra Mejorado: ",(nltk.classify.accuracy(b_classifier.getClassifier(), classification_features["enhanced"])*100))
plot.show()

```

