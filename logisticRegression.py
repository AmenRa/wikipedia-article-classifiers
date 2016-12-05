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
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split


# IMPORT DATASET
data = pd.read_csv(open('dataset.csv'))
#data = pd.read_csv(open('oldDataset.csv'))
#data = shuffle(data)

# only featured/non-featured articles classification
#data = pd.read_csv(open('twoClassDataset.csv'))

# Feature list
#features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerSentence", "citationCountPerSection", "externalLinksCount", "externalLinksPerSentence", "externalLinksPerSection", "imageCount", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "adjectiveCount", "adjectivesPerSentence", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord", "differentNounsDifferentWordsRatio", "differentVerbsDifferentWordsRatio", "differentPronounsDifferentWordsRatio", "differentAdjectivesDifferentWordsRatio", "differentAdverbsDifferentWordsRatio", "differentCoordinatingConjunctionsDifferentWordsRatio", "differentSubordinatingPrepositionsAndConjunctionsDifferentWordsRatio"]



#features_cols = ["largestShortestSectionRatio", "sectionSizeStandardDeviation"]



features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerSentence", "citationCountPerSection", "externalLinksCount", "externalLinksPerSentence", "externalLinksPerSection", "imageCount", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "modalAuxiliaryVerbCount", "modalAuxiliaryVerbsRatio", "modalAuxiliaryVerbsPerSentence", "modalAuxiliaryVerbsRate", "passiveVoiceCount", "passiveVoiceRatio", "passiveVoicePerSentence", "passiveVoiceRate", "numberOfSentencesThatStartWithACoordinatingConjunction", "numberOfSentencesThatStartWithADeterminer", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction", "numberOfSentencesThatStartWithAnAdjective", "numberOfSentencesThatStartWithANoun", "numberOfSentencesThatStartWithAPronoun", "numberOfSentencesThatStartWithAnAdverb", "numberOfSentencesThatStartWithAnArticle", "numberOfSentencesThatStartWithACoordinatingConjunctionRatio", "numberOfSentencesThatStartWithADeterminerRatio", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunctionRatio", "numberOfSentencesThatStartWithAnAdjectiveRatio", "numberOfSentencesThatStartWithANounRatio", "numberOfSentencesThatStartWithAPronounRatio", "numberOfSentencesThatStartWithAnAdverbRatio", "numberOfSentencesThatStartWithAnArticleRatio", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "differentNounsDifferentWordsRatio", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "differentVerbsDifferentWordsRatio", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "differentPronounsDifferentWordsRatio", "adjectiveCount", "adjectivesPerSentence", "adjectivesRate", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "differentAdjectivesDifferentWordsRatio", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "differentAdverbsDifferentWordsRatio", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "differentCoordinatingConjunctionsDifferentWordsRatio", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionsAndConjunctionsDifferentWordsRatio", "syllablesPerWord", "charactersPerWord"]


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
#normalizedX = scaler.transform(X)





# 10-fold cross-validation with logistic regression
#logreg = LogisticRegression()
#
#accuracy = str(cross_val_score(logreg, X, y, cv=10, scoring='accuracy').mean())
#print 'Accuracy: ' + accuracy
#
#neg_mse = cross_val_score(logreg, X, y, cv=10, scoring='neg_mean_squared_error')
## fox the sign of MSE scores
#mse_scores = -neg_mse
#mse = mse_scores.mean()
#
### convert from MSE to RMSE (Root MSE)
##rmse_scores = np.sqrt(mse_scores)
### calculate the avarage RMSE
##rmse = rmse_scores.mean()
#
#print 'RMSE: ' + str(mse)



# 10-fold cross-validation with logistic regression PREDICTIONS
#clf = LogisticRegression()
#y_pred = cross_val_predict(clf, X, y, cv=10)
#
#print metrics.classification_report(y, y_pred) 
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))








print 'BEFORE Feature Selection'
# 10-fold cross-validation with logistic regression PREDICTIONS
clf = LogisticRegression()
y_pred = cross_val_predict(clf, X, y, cv=10)

#print metrics.classification_report(y, y_pred) 
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))







from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#k_range = range(1, 100)
#k_scores = []
#for k in k_range:
#    X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
#    clf = LogisticRegression()
#    y_pred = cross_val_predict(clf, X_new, y, cv=10)
#    print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#    k_scores.append(metrics.accuracy_score(y, y_pred))
#print k_scores
#
#import matplotlib.pyplot as plt
##%matplotlib inline
#
## plot the value of K for KNN (x-axis) versus the cross-validated accuracy (y-axis)
#plt.plot(k_range, k_scores)
#plt.xlabel('Value of K ')
#plt.ylabel('Cross-Validated Accuracy')

            
            



#X_new = SelectKBest(chi2, k=89).fit_transform(X, y)
#print 'AFTER Feature Selection'
## 10-fold cross-validation with logistic regression PREDICTIONS
#clf = LogisticRegression()
#y_pred = cross_val_predict(clf, X_new, y, cv=10)
#
##print metrics.classification_report(y, y_pred) 
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
##print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))






















# use train/test split with different random_state values
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=7)

#check classification accuracy random_state values
#clf = LogisticRegression()
#clf.fit(X_train, y_train)
#y_pred = clf.predict(X_test)
#print "Accuracy: " + str(metrics.accuracy_score(y_test, y_pred))
#print metrics.classification_report(y_test, y_pred)








