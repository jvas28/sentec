import classifiers.enhanced_binary_classifier as b_classifier
from nlp.spanish import stem
word = input()
classifier = b_classifier.getClassifier()
print(classifier.classify(b_classifier.extract_feature(stem(word))))

