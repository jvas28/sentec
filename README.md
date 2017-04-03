
# Sentec - Análisis de Sentimiento en Ecuador
Es un set de módulos escritos en Python 3.x y un archivo de léxico que permite realizar análisis de Sentimiento Basado en Léxicos. 
Creada en base a un estudio del léxico ecuatoriano y la incidencia que pueden tener las expresiones idiomáticas sobre la presición de los algoritmos de Análisis de Sentimiento de la Universidad Católica Santiago de Guayaquil.

## Requerimientos:
- Python 3.X
- NLTK
- Snowball Stemmer

## Composición
- Léxico Ecuatoriano
- Módulo de Procesamiento de Lenguaje Natural en Español
- Clasificador Bayesiano

## Ejemplos
1.  Ejemplo sencillo de uso del módulo de Procesamiento de Lenguaje Natural en español-

```python

import es_nlp as lang_tools

print("Ingresa una frase para el proceso de NLP:")
t=input();
print(lang_tools.tokenize(t));

```
2. Ejemplo de implementación de script de Análisis de Sentimiento unifrase.
```python
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
```

## Licencia:
GPL License
