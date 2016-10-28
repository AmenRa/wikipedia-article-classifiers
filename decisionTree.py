# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:12:56 2016

@author: Elias
"""
from sklearn.preprocessing import Normalizer
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


# IMPORT DATASET
data = pd.read_csv(open('dataset.csv'))
#data = shuffle(data)

# Feature list
features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerSentence", "citationCountPerSection", "externalLinksCount", "externalLinksPerSentence", "externalLinksPerSection", "imageCount", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "linsearWriteFormula", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "adjectiveCount", "adjectivesPerSentence", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord", "differentNounsDifferentWordsRatio", "differentVerbsDifferentWordsRatio", "differentPronounsDifferentWordsRatio", "differentAdjectivesDifferentWordsRatio", "differentAdverbsDifferentWordsRatio", "differentCoordinatingConjunctionsDifferentWordsRatio", "differentSubordinatingPrepositionsAndConjunctionsDifferentWordsRatio"]


#features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCountPerSentence", "citationCountPerSection", "externalLinksPerSentence", "externalLinksPerSection", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionRatio", "exclamationRatio", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "linsearWriteFormula", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounsPerSentence", "nounsRate", "differentNounsPerSentence", "differentNounsRate", "verbsPerSentence", "verbsRate", "differentVerbsPerSentence", "differentVerbsRate", "pronounsPerSentence", "pronounsRate", "differentPronounsPerSentence", "differentPronounsRate", "adjectivesPerSentence", "differentAdjectivesPerSentence", "differentAdjectivesRate","adverbsPerSentence", "adverbsRate", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate",  "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate",  "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate",  "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord"]


###############################################################################
# Measuring Article Quality in Wikipedia: Lexical Clue Model FEATURES
#features_cols = ["meanSentenceSize", "differentWordsPerSentence", "differentWordsRate", "nounsRate", "differentNounsDifferentWordsRatio", "verbsRate", "differentVerbsDifferentWordsRatio"]

###############################################################################


# Select only the columns corresponding to the features in the list
X = data[features_cols]

# Select qualityClass as the response (y)
y = data.qualityClass

# FEATURE SELECTION
#from sklearn.feature_selection import VarianceThreshold
#sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
#X = sel.fit_transform(X)

# STANDARDIZE DATASET
#X = preprocessing.scale(X)
#y = preprocessing.scale(y)

# NORMALIZE DATASET
#scaler = Normalizer().fit(X)
#normalizedX = scaler.transform(X)

# 10-fold cross-validation with random forest
clf = DecisionTreeClassifier(random_state=7)
y_pred = cross_val_predict(clf, X, y, cv=10)

print metrics.classification_report(y, y_pred) 
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))











































