import es_nlp as lang_tools
from classifier import nbclassifier,known_words,extract_feature
print("Ingrese una frase para el análisis:")
t=input()
exp_count=0;
exp_value=0;

tokens=lang_tools.tokenize(t)
for e in tokens:
	if e in known_words:
		exp_count+=1
		sentiment=nbclassifier.classify(extract_feature(e))
		exp_value+=float(sentiment)-1
if exp_count>0:
	scale_sentiment=exp_value/exp_count
	acceptance=scale_sentiment/2*100 
	print("Valor de Sentimiento: "+str(scale_sentiment+1))
	print("Aceptacion: "+str(acceptance)+"%")
else:
	print("No se pudo determinar")