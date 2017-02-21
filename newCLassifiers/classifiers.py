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

# Select only the columns corresponding to the features in the list
X = data[features_cols]

X.sample(frac=1)

# Select qualityClass as the response (y)
y = data.qualityClass

# print 'Decision Tree'
# # 10-fold cross-validation with decision tree PREDICTIONS
# clf = DecisionTreeClassifier(random_state=8)
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


# print 'KNN'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = KNeighborsClassifier(n_neighbors=25)
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


# print 'Logistic Regression'
# # 10-fold cross-validation with logistic regression PREDICTIONS
# clf = LogisticRegression()
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))
#
#
# print 'Naive Bayes'
# # 10-fold cross-validation with naive bayes PREDICTIONS
# clf = GaussianNB()
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))
#
#
# print 'Random Forest'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = RandomForestClassifier(n_estimators=200, random_state=5)
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))
#
#
# print 'Support Vector Classifier'
# # 10-fold cross-validation with support vector classifier PREDICTIONS
# clf = LinearSVC(dual=False)
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))
#
#
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
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, y)
print("Num Features: %d") % fit.n_features_
print("Selected Features: %s") % fit.support_
print("Feature Ranking: %s") % fit.ranking_
