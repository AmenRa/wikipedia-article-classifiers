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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import csv
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

import random

# Change it with the name of your dataset
# filename = 'MHDataset.csv'
filename = 'MHParallelDataset.csv'

# Extract columns names (fieldnames)
with open(filename, 'r') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

# Remove last column (qualityClass)
fieldnames.pop()

# IMPORT DATASET
data = pd.read_csv(open(filename))


# Feature list
features_cols = fieldnames

# Text features
# features_cols = [ "characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerTextLength", "citationCountPerSection", "externalLinksCount", "externalLinksPerTextLength", "externalLinksPerSection", "imageCount", "imagePerTextLength", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "modalAuxiliaryVerbCount", "modalAuxiliaryVerbsRatio", "modalAuxiliaryVerbsPerSentence", "modalAuxiliaryVerbsRate", "passiveVoiceCount", "passiveVoiceRatio", "passiveVoicePerSentence", "passiveVoiceRate", "numberOfSentencesThatStartWithACoordinatingConjunction", "numberOfSentencesThatStartWithADeterminer", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction", "numberOfSentencesThatStartWithAnAdjective", "numberOfSentencesThatStartWithANoun", "numberOfSentencesThatStartWithAPronoun", "numberOfSentencesThatStartWithAnAdverb", "numberOfSentencesThatStartWithAnArticle", "numberOfSentencesThatStartWithACoordinatingConjunctionRatio", "numberOfSentencesThatStartWithADeterminerRatio", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunctionRatio", "numberOfSentencesThatStartWithAnAdjectiveRatio", "numberOfSentencesThatStartWithANounRatio", "numberOfSentencesThatStartWithAPronounRatio", "numberOfSentencesThatStartWithAnAdverbRatio", "numberOfSentencesThatStartWithAnArticleRatio", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "differentNounsDifferentWordsRatio", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "differentVerbsDifferentWordsRatio", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "differentPronounsDifferentWordsRatio", "adjectiveCount", "adjectivesPerSentence", "adjectivesRate", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "differentAdjectivesDifferentWordsRatio", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "differentAdverbsDifferentWordsRatio", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "differentCoordinatingConjunctionsDifferentWordsRatio", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionsAndConjunctionsDifferentWordsRatio", "syllablesPerWord", "charactersPerWord", "NNP,NNP,NNP", "VBD,DT,JJ", "IN,DT,NNP", "NNP,IN,DT", "DT,NNP,NNP", "JJ,NN,IN", "NN,IN,DT", "IN,DT,NN", "NN,IN,NNP", "IN,NNP,NNP", "NNP,VBD,DT", "VBD,DT,NN", "DT,NN,IN", "VBD,VBN,IN", "NNP,NNP,VBD", "IN,NN,IN", "NNP,NNP,IN", "NNP,IN,NNP", "VBD,IN,DT", "IN,DT,JJ", "JJ,NNS,IN", "DT,JJ,NN", "IN,DT,NNS", "IN,CD,NNP", "VBN,IN,DT", "DT,NN,NN", "IN,PRP$,NN", "NNP,VBD,VBN", "NNP,CC,NNP", "NNS,IN,DT", "NN,IN,NN", "DT,NN,VBD", "NN,VBD,VBN", "TO,VB,DT", "NNP,POS,NN", "ter", "er_", "_wa", "was", "as_", "s_a", "_a_", "an_", "e_a", "_an", "and", "nd_", "_re", "ent", "_of", "of_", "f_t", "_th", "the", "he_", "on_", ",_a", "at_", "ed_", "_on", "n_t", "or_", "ing", "ng_", "_in", "in_", "d_t", "d_a", "_he", "_to", "ted", "th_", "al_", "es_", "ate", "_co", "ion", "ere", "_fo", "for", "s,_", "to_", "ati", "st_", "re_", "_be", "ly_", "her", "_hi", "his", "is_", "e_t", "en_", "e_o", "t_t", "tio", "_Th" ]

# Review Features
# features_cols = [ "age", "agePerReview", "reviewPerDay", "reviewsPerUser", "reviewsPerUserStdDev", "discussionCount", "reviewCount", "registeredReviewCount", "anonymouseReviewCount", "registeredReviewRate", "anonymouseReviewRate", "registeredAnonymouseReviewRatio", "userCount", "occasionalUserCount", "occasionalUserRate", "registeredUserCount", "anonymouseUserCount", "registerdAnonymouseUserRatio", "registeredUserRate", "anonymouseUserRate", "revertCount", "revertReviewRatio", "diversity", "modifiedLinesRate", "mostActiveUsersReviewCount", "mostActiveUsersReviewRate", "lastThreeMonthsReviewCount", "lastThreeMonthsReviewRate" ]

# Network Features
# features_cols = ["pageRank", "indegree", "outdegree", "assortativity_inin", "assortativity_inout", "assortativity_outin", "assortativity_outout", "localClusteringCoefficient", "reciprocity", "linkCount", "translationCount" ]

# ARTICLE'S Feature
# features_cols = ["characterCount", "wordCount", "sentenceCount", "sectionCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "sectionSizeStandardDeviation", "subsectionCount", "meanOfSubsectionsPerSection", "abstractSize", "citationCount", "citationCountPerTextLength", "citationCountPerSection", "externalLinksPerTextLength", "externalLinksCount", "externalLinksPerSection", "imageCount", "imagePerSection", "largestSentenceSize", "largeSentenceRate", "shortSentenceRate", "modalAuxiliaryVerbCount", "questionCount", "pronounCount", "passiveVoiceCount", "coordinatingConjunctionsRate", "subordinatingPrepositionsAndConjunctionsRate", "toBeVerbRate", "numberOfSentencesThatStartWithACoordinatingConjunction", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction", "numberOfSentencesThatStartWithAPronoun", "numberOfSentencesThatStartWithAnArticle", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "age", "agePerReview", "reviewPerDay", "reviewsPerUser", "reviewsPerUserStdDev", "discussionCount", "userCount", "anonymouseUserCount", "reviewCount", "modifiedLinesRate", "lastThreeMonthsReviewRate", "mostActiveUsersReviewRate", "pageRank", "indegree", "outdegree", "assortativity_inin", "assortativity_inout", "assortativity_outin", "assortativity_outout", "localClusteringCoefficient", "reciprocity", "linkCount", "translationCount"]


# Select only the columns corresponding to the features in the list
X = data[features_cols]

X.sample(frac=1)

# Select qualityClass as the response (y)
y = data.qualityClass

# y[y == 1] = 1
# y[y == 2] = 1
# y[y == 3] = 2
# y[y == 4] = 2
# y[y == 5] = 3
# y[y == 6] = 3
# y[y == 7] = 4

# STUB and NON-STUB
# y[y > 1] = 2

# FEATURED ARTICLES and NON-FEATURED ARTICLES
#y[y < 7] = 1
#y[y == 7] = 2


# FEATURE SELECTION
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# rfe = RFE(model, 3)
# fit = rfe.fit(X, y)
# print("Num Features: %d") % fit.n_features_
# print("Selected Features: %s") % fit.support_
# print("Feature Ranking: %s") % fit.ranking_




# print len(X[0])

# print 'BEFORE Feature Selection'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = RandomForestClassifier(n_estimators=143, random_state=5)
# y_pred = cross_val_predict(clf, X, y, cv=10)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))




# Accuracy 0.58 a 58, partire da 75

# k_range = range(75, 300)
# k_scores = []
# for k in k_range:
#    clf = RandomForestClassifier(n_estimators=k, random_state=5)
#    scores = cross_val_score(clf, X, y, cv=20, scoring='accuracy')
#    print str(k) + ' ' + str(scores.mean())
#    k_scores.append(scores.mean())
# print k_scores
#
# import matplotlib.pyplot as plt
# #%matplotlib inline
#
# # plot the value of K for KNN (x-axis) versus the cross-validated accuracy (y-axis)
# plt.plot(k_range, k_scores)
# plt.xlabel('Value of K for KNN')
# plt.ylabel('Cross-Validated Accuracy')







# print 'BEFORE Feature Selection PARALLEL'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = RandomForestClassifier(n_estimators=200, random_state=5)
# y_pred = cross_val_predict(clf, X, y, cv=10)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))







# print 'AFTER Feature Selection'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = RandomForestClassifier(n_estimators=1000, random_state=6)
# y_pred = cross_val_predict(clf, X, y, cv=10)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))



# # Find features
# inverted_X_new = [list(x) for x in zip(*X_new)]
#
# for pos in features_cols:
#     for x in inverted_X_new:
#         if (X[pos]==x).all():
#             print pos










# USE THIS TO FIND BEST FEATURES
print "Starting features selection"
k_range = range(1, len(features_cols))
k_scores = []
for k in k_range:
  X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
  clf = RandomForestClassifier(n_estimators=200, random_state=5)
  y_pred = cross_val_predict(clf, X_new, y, cv=20)
  print str(k) + ' Accuracy: ' + str(metrics.accuracy_score(y, y_pred))
  k_scores.append(metrics.accuracy_score(y, y_pred))
print k_scores

#%matplotlib inline

# plot the value of K (x-axis) versus the cross-validated accuracy (y-axis)
plt.plot(k_range, k_scores)
plt.xlabel('Value of K')
plt.ylabel('Cross-Validated Accuracy')
