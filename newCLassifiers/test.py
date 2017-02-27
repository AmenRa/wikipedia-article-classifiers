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
from boruta import BorutaPy

import random

# Change it with the name of your dataset
filename = 'MHDataset.csv'
#filename = 'MHParallelDataset.csv'

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


# print 'Random Forest'
# # 10-fold cross-validation with knn PREDICTIONS
# clf = RandomForestClassifier(n_estimators=146, random_state=5)
# y_pred = cross_val_predict(clf, X, y, cv=20)
#
# print metrics.classification_report(y, y_pred)
# print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
# print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))




#print 'BEFORE FS'
## 10-fold cross-validation with knn PREDICTIONS
#clf = RandomForestClassifier(n_estimators=200, random_state=5, n_jobs=-1, class_weight='auto')
#y_pred = cross_val_predict(clf, X, y, cv=20)
#
#print metrics.classification_report(y, y_pred)
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))





#from sklearn.feature_selection import SelectFromModel
#
#from sklearn.svm import LinearSVC
#
#print X.shape
#lsvc = RandomForestClassifier(n_estimators=200, random_state=5, n_jobs=-1, class_weight='auto').fit(X, y)
#model = SelectFromModel(lsvc, prefit=True)
#X_new = model.transform(X)
#print X_new.shape
#
#
## 10-fold cross-validation with knn PREDICTIONS
#clf = RandomForestClassifier(n_estimators=200, random_state=5, n_jobs=-1, class_weight='auto')
#y_pred = cross_val_predict(clf, X_new, y, cv=20)
#
#print metrics.classification_report(y, y_pred)
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))


