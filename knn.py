# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:12:56 2016

@author: Elias
"""

#import pandas as pd
#data = pd.read_csv(open('dataset.csv'))
#target = data['qualityClass']
#del data['qualityClass']
#
#print data


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import Normalizer
import numpy
import pandas as pd
from sklearn.utils import shuffle
#from sklearn.cross_validation import KFold
#kf = KFold(700, n_folds=10, shuffle=False)
from sklearn.model_selection import cross_val_score

# IMPORT DATASET
data = pd.read_csv(open('dataset.csv'))
#X = shuffle(X)

# only featured/non-featured articles classification
#data = pd.read_csv(open('twoClassDataset.csv'))

# Feature list
features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerSentence", "citationCountPerSection", "externalLinksCount", "externalLinksPerSentence", "externalLinksPerSection", "imageCount", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "linsearWriteFormula", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "adjectiveCount", "adjectivesPerSentence", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord"]


#features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCountPerSentence", "citationCountPerSection", "externalLinksPerSentence", "externalLinksPerSection", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionRatio", "exclamationRatio", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "linsearWriteFormula", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounsPerSentence", "nounsRate", "differentNounsPerSentence", "differentNounsRate", "verbsPerSentence", "verbsRate", "differentVerbsPerSentence", "differentVerbsRate", "pronounsPerSentence", "pronounsRate", "differentPronounsPerSentence", "differentPronounsRate", "adjectivesPerSentence", "differentAdjectivesPerSentence", "differentAdjectivesRate","adverbsPerSentence", "adverbsRate", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate",  "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate",  "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate",  "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord"]


################################################################################
# Size Matters: Word Count as a Measure of Quality on Wikipedia FEATURES
#features_cols = ["wordCount"]
################################################################################


# Select only the columns corresponding to the features in the list
X = data[features_cols]

# Select qualityClass as the response (y)
y = data.qualityClass

# FEATURE SELECTION
#from sklearn.feature_selection import VarianceThreshold
#sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
#X = sel.fit_transform(X)

# NORMALIZE DATASET
#scaler = Normalizer().fit(X)
#X = scaler.transform(X)



# 10-fold cross-validation with K=5 for KNN (the n_neighbors parameter)
#knn = KNeighborsClassifier(n_neighbors=5)
#scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
#print scores
#print scores.mean()




## search for an optimal value of K for KNN
#k_range = range(1, 31)
#k_scores = []
#for k in k_range:
#    clf = KNeighborsClassifier(n_neighbors=k)
#    scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
#    k_scores.append(scores.mean())
#print k_scores
#
#import matplotlib.pyplot as plt
##%matplotlib inline
#
## plot the value of K for KNN (x-axis) versus the cross-validated accuracy (y-axis)
#plt.plot(k_range, k_scores)
#plt.xlabel('Value of K for KNN')
#plt.ylabel('Cross-Validated Accuracy')







# 10-fold cross-validation with KNN PREDICTIONS
clf = KNeighborsClassifier(n_neighbors=1)
y_pred = cross_val_predict(clf, X, y, cv=10)

print metrics.classification_report(y, y_pred) 
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))



















