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
from sklearn.neighbors import KNeighborsClassifier

import random

# Change it with the name of your dataset
filename = 'MHDataset.csv'

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

# features_cols = ["characterCount", "wordCount", "sentenceCount", "sectionCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "sectionSizeStandardDeviation", "subsectionCount", "meanOfSubsectionsPerSection", "abstractSize", "citationCount", "citationCountPerTextLength", "citationCountPerSection", "externalLinksPerTextLength", "externalLinksCount", "externalLinksPerSection", "imageCount", "imagePerSection", "largestSentenceSize", "largeSentenceRate", "shortSentenceRate", "modalAuxiliaryVerbCount", "questionCount", "pronounCount", "passiveVoiceCount", "coordinatingConjunctionsRate", "subordinatingPrepositionsAndConjunctionsRate", "toBeVerbRate", "numberOfSentencesThatStartWithACoordinatingConjunction", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction", "numberOfSentencesThatStartWithAPronoun", "numberOfSentencesThatStartWithAnArticle", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "age", "agePerReview", "reviewPerDay", "reviewsPerUser", "reviewsPerUserStdDev", "discussionCount", "userCount", "anonymouseUserCount", "reviewCount", "modifiedLinesRate", "lastThreeMonthsReviewRate", "mostActiveUsersReviewRate", "pageRank", "indegree", "outdegree", "assortativity_inin", "assortativity_inout", "assortativity_outin", "assortativity_outout", "localClusteringCoefficient", "reciprocity", "linkCount", "translationCount"]


# Select only the columns corresponding to the features in the list
X = data[features_cols]

# X.sample(frac=1)

# Select qualityClass as the response (y)
y = data.qualityClass


# print 'BEFORE Feature Selection'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = KNeighborsClassifier(n_neighbors=50)
# y_pred = cross_val_predict(clf, X, y, cv=10)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))



# print 'AFTER Feature Selection'
# X_new = SelectKBest(chi2, k=35).fit_transform(X, y)
# # 10-fold cross-validation with logistic regression PREDICTIONS
# clf = LogisticRegression()
# y_pred = cross_val_predict(clf, X_new, y, cv=10)
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
# print "Starting features selection"
# k_range = range(1, len(features_cols))
# k_scores = []
# for k in k_range:
#   X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
#   clf = LogisticRegression()
#   y_pred = cross_val_predict(clf, X_new, y, cv=10)
#   print str(k) + ' Accuracy: ' + str(metrics.accuracy_score(y, y_pred))
#   k_scores.append(metrics.accuracy_score(y, y_pred))
# print k_scores
#
# #%matplotlib inline
#
# # plot the value of K (x-axis) versus the cross-validated accuracy (y-axis)
# plt.plot(k_range, k_scores)
# plt.xlabel('Value of K')
# plt.ylabel('Cross-Validated Accuracy')



# search for an optimal value of K for KNN
k_range = range(1, 100)
k_scores = []
for k in k_range:
   clf = KNeighborsClassifier(n_neighbors=k)
   scores = cross_val_score(clf, X, y, cv=20, scoring='accuracy')
   k_scores.append(scores.mean())
print k_scores

import matplotlib.pyplot as plt
#%matplotlib inline

# plot the value of K for KNN (x-axis) versus the cross-validated accuracy (y-axis)
plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
