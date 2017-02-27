# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:12:56 2016

@author: Elias
"""
from sklearn.preprocessing import Normalizer
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
import csv
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt
# Import classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier

# Change it with the name of your dataset
filename = 'MHDataset.csv'
# filename = 'MH_FA_NON-FA_Dataset.csv'


# filename = 'MHParallelDataset.csv'
# filename = 'MH_FA_NON-FA_ParallelDataset.csv'
# filename = 'MH_Stub_NON-Stub_ParallelDataset.csv'
# filename = 'MHTwoClassesParallelDataset.csv'

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

# Automatic Quality Assessment of Content Created Collaboratively by Web Communities: A Case Study of Wikipedia'S Feature
# features_cols = ["characterCount", "wordCount", "sentenceCount", "sectionCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "sectionSizeStandardDeviation", "subsectionCount", "meanOfSubsectionsPerSection", "abstractSize", "citationCount", "citationCountPerTextLength", "citationCountPerSection", "externalLinksPerTextLength", "externalLinksCount", "externalLinksPerSection", "imageCount", "imagePerSection", "largestSentenceSize", "largeSentenceRate", "shortSentenceRate", "modalAuxiliaryVerbCount", "questionCount", "pronounCount", "passiveVoiceCount", "coordinatingConjunctionsRate", "subordinatingPrepositionsAndConjunctionsRate", "toBeVerbRate", "numberOfSentencesThatStartWithACoordinatingConjunction", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction", "numberOfSentencesThatStartWithAPronoun", "numberOfSentencesThatStartWithAnArticle", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "age", "agePerReview", "reviewPerDay", "reviewsPerUser", "reviewsPerUserStdDev", "discussionCount", "userCount", "anonymouseUserCount", "reviewCount", "modifiedLinesRate", "lastThreeMonthsReviewRate", "mostActiveUsersReviewRate", "pageRank", "indegree", "outdegree", "assortativity_inin", "assortativity_inout", "assortativity_outin", "assortativity_outout", "localClusteringCoefficient", "reciprocity", "linkCount", "translationCount"]


# Parallel Features
# features_cols = ['characterCount', 'wordCount', 'syllableCount', 'sentenceCount', 'sectionCount', 'subsectionCount', 'paragraphCount', 'meanSectionSize', 'meanParagraphSize', 'largestSectionSize', 'shortestSectionSize', 'largestShortestSectionRatio', 'sectionSizeStandardDeviation', 'meanOfSubsectionsPerSection', 'abstractSize', 'abstractSizeArtcileLengthRatio', 'citationCount', 'citationCountPerTextLength', 'citationCountPerSection', 'externalLinksCount', 'externalLinksPerTextLength', 'externalLinksPerSection', 'imageCount', 'imagePerTextLength', 'imagePerSection', 'meanSentenceSize', 'largestSentenceSize', 'shortestSentenceSize', 'largeSentenceRate', 'shortSentenceRate', 'questionCount', 'questionRatio', 'exclamationCount', 'exclamationRatio', 'toBeVerbCount', 'toBeVerbRatio', 'toBeVerbPerSentence', 'toBeVerbRate', 'modalAuxiliaryVerbCount', 'modalAuxiliaryVerbsRatio', 'modalAuxiliaryVerbsPerSentence', 'modalAuxiliaryVerbsRate', 'passiveVoiceCount', 'passiveVoiceRatio', 'passiveVoicePerSentence', 'passiveVoiceRate', 'numberOfSentencesThatStartWithACoordinatingConjunction', 'numberOfSentencesThatStartWithADeterminer', 'numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction', 'numberOfSentencesThatStartWithAnAdjective', 'numberOfSentencesThatStartWithANoun', 'numberOfSentencesThatStartWithAPronoun', 'numberOfSentencesThatStartWithAnAdverb', 'numberOfSentencesThatStartWithAnArticle', 'numberOfSentencesThatStartWithACoordinatingConjunctionRatio', 'numberOfSentencesThatStartWithADeterminerRatio', 'numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunctionRatio', 'numberOfSentencesThatStartWithAnAdjectiveRatio', 'numberOfSentencesThatStartWithANounRatio', 'numberOfSentencesThatStartWithAPronounRatio', 'numberOfSentencesThatStartWithAnAdverbRatio', 'numberOfSentencesThatStartWithAnArticleRatio', 'automatedReadabilityIndex', 'colemanLiauIndex', 'fleshReadingEase', 'fleschKincaidGradeLevel', 'gunningFogIndex', 'lasbarhetsIndex', 'smogGrading', 'daleChallReadabilityFormula', 'differentWordCount', 'differentWordsPerSentence', 'differentWordsRate', 'nounCount', 'nounsPerSentence', 'nounsRate', 'differentNounCount', 'differentNounsPerSentence', 'differentNounsRate', 'differentNounsDifferentWordsRatio', 'verbCount', 'verbsPerSentence', 'verbsRate', 'differentVerbCount', 'differentVerbsPerSentence', 'differentVerbsRate', 'differentVerbsDifferentWordsRatio', 'pronounCount', 'pronounsPerSentence', 'pronounsRate', 'differentPronounCount', 'differentPronounsPerSentence', 'differentPronounsRate', 'differentPronounsDifferentWordsRatio', 'adjectiveCount', 'adjectivesPerSentence', 'adjectivesRate', 'differentAdjectiveCount', 'differentAdjectivesPerSentence', 'differentAdjectivesRate', 'differentAdjectivesDifferentWordsRatio', 'adverbCount', 'adverbsPerSentence', 'adverbsRate', 'differentAdverbCount', 'differentAdverbsPerSentence', 'differentAdverbsRate', 'differentAdverbsDifferentWordsRatio', 'coordinatingConjunctionCount', 'coordinatingConjunctionsPerSentence', 'coordinatingConjunctionsRate', 'differentCoordinatingConjunctionCount', 'differentCoordinatingConjunctionsPerSentence', 'differentCoordinatingConjunctionsRate', 'differentCoordinatingConjunctionsDifferentWordsRatio', 'subordinatingPrepositionAndConjunctionCount', 'subordinatingPrepositionsAndConjunctionsPerSentence', 'subordinatingPrepositionsAndConjunctionsRate', 'differentSubordinatingPrepositionAndConjunctionCount', 'differentSubordinatingPrepositionsAndConjunctionsPerSentence', 'differentSubordinatingPrepositionsAndConjunctionsRate', 'differentSubordinatingPrepositionsAndConjunctionsDifferentWordsRatio', 'syllablesPerWord', 'charactersPerWord', 'NNP,NNP,NNP', 'VBD,DT,JJ', 'IN,DT,NNP', 'NNP,IN,DT', 'DT,NNP,NNP', 'JJ,NN,IN', 'NN,IN,DT', 'IN,DT,NN', 'NN,IN,NNP', 'IN,NNP,NNP', 'NNP,VBD,DT', 'VBD,DT,NN', 'DT,NN,IN', 'VBD,VBN,IN', 'NNP,NNP,VBD', 'IN,NN,IN', 'NNP,NNP,IN', 'NNP,IN,NNP', 'VBD,IN,DT', 'IN,DT,JJ', 'JJ,NNS,IN', 'DT,JJ,NN', 'IN,DT,NNS', 'IN,CD,NNP', 'VBN,IN,DT', 'DT,NN,NN', 'IN,PRP$,NN', 'NNP,VBD,VBN', 'NNP,CC,NNP', 'NNS,IN,DT', 'NN,IN,NN', 'DT,NN,VBD', 'NN,VBD,VBN', 'TO,VB,DT', 'NNP,POS,NN', 'ter', 'er_', '_wa', 'was', 'as_', 's_a', '_a_', 'an_', 'e_a', '_an', 'and', 'nd_', '_re', 'ent', '_of', 'of_', 'f_t', '_th', 'the', 'he_', 'on_', ',_a', 'at_', 'ed_', '_on', 'n_t', 'or_', 'ing', 'ng_', '_in', 'in_', 'd_t', 'd_a', '_he', '_to', 'ted', 'th_', 'al_', 'es_', 'ate', '_co', 'ion', 'ere', '_fo', 'for', 's,_', 'to_', 'ati', 'st_', 're_', '_be', 'ly_', 'her', '_hi', 'his', 'is_', 'e_t', 'en_', 'e_o', 't_t', 'tio', '_Th', 'age', 'agePerReview', 'reviewPerDay', 'reviewsPerUser', 'reviewsPerUserStdDev', 'discussionCount', 'reviewCount', 'registeredReviewCount', 'anonymouseReviewCount', 'registeredReviewRate', 'anonymouseReviewRate', 'registeredAnonymouseReviewRatio', 'userCount', 'occasionalUserCount', 'occasionalUserRate', 'registeredUserCount', 'anonymouseUserCount', 'registerdAnonymouseUserRatio', 'registeredUserRate', 'anonymouseUserRate', 'revertCount', 'revertReviewRatio', 'diversity', 'modifiedLinesRate', 'mostActiveUsersReviewCount', 'mostActiveUsersReviewRate', 'lastThreeMonthsReviewCount', 'lastThreeMonthsReviewRate']

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
# y[y < 7] = 1
# y[y == 7] = 2





print 'Decision Tree'
# 10-fold cross-validation with decision tree PREDICTIONS
clf = DecisionTreeClassifier(random_state=8)
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


print 'KNN'
# 10-fold cross-validation with knn PREDICTIONS
clf = KNeighborsClassifier(n_neighbors=49) # NORMAL
# clf = KNeighborsClassifier(n_neighbors=25) # PARALLEL
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


print 'Logistic Regression'
# 10-fold cross-validation with logistic regression PREDICTIONS
clf = LogisticRegression()
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


print 'Naive Bayes'
# 10-fold cross-validation with naive bayes PREDICTIONS
clf = GaussianNB()
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


print 'Random Forest'
# 10-fold cross-validation with knn PREDICTIONS
clf = RandomForestClassifier(n_estimators=146, random_state=5)
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


print 'Support Vector Classifier'
# 10-fold cross-validation with support vector classifier PREDICTIONS
clf = LinearSVC(dual=False)
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


# #NORMALIZE DATASET
# scaler = Normalizer().fit(X)
# X = scaler.transform(X)
#
# print 'Neural Network'
# # 10-fold cross-validation with mlp PREDICTIONS
# layers = (50, 30)
# clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(layers), max_iter=1000, random_state=1)
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print 'Layers: ' + str(layers)
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))














#print 'AFTER Feature Selection'
#X_new = SelectKBest(chi2, k=163).fit_transform(X, y)
## 10-fold cross-validation with logistic regression PREDICTIONS
#clf = clf = RandomForestClassifier(n_estimators=200, random_state=5)
#y_pred = cross_val_predict(clf, X_new, y, cv=20)
#
#print metrics.classification_report(y, y_pred)
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))



## Find features
#inverted_X_new = [list(x) for x in zip(*X_new)]
#
#for pos in features_cols:
#  for x in inverted_X_new:
#    if (X[pos]==x).all():
#      print pos
















# USE THIS TO FIND BEST FEATURES
#print "Starting features selection"
#k_range = range(1, len(features_cols))
#k_scores = []
#for k in k_range:
#  X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
#  clf = RandomForestClassifier(n_estimators=200, random_state=5)
#  y_pred = cross_val_predict(clf, X_new, y, cv=20)
#  print str(k) + ' Accuracy: ' + str(metrics.accuracy_score(y, y_pred))
#  k_scores.append(metrics.accuracy_score(y, y_pred))
#print k_scores
#
##%matplotlib inline
#
## plot the value of K (x-axis) versus the cross-validated accuracy (y-axis)
#plt.plot(k_range, k_scores)
#plt.xlabel('Value of K')
#plt.ylabel('Cross-Validated Accuracy')




# FEATURE SELECTION
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import LogisticRegression
#model = LogisticRegression()
#rfe = RFE(model, 3)
#fit = rfe.fit(X, y)
#print("Num Features: %d") % fit.n_features_
#print("Selected Features: %s") % fit.support_
#print("Feature Ranking: %s") % fit.ranking_
