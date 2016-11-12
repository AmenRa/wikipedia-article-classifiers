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


# IMPORT DATASET
#data = pd.read_csv(open('charTrigramsDataset.csv'))

data = pd.read_csv(open('charTrigramsDatasetLessThen10.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen20.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen30.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen40.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen50.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen60.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen70.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen80.csv'))
data = pd.read_csv(open('charTrigramsDatasetLessThen90.csv'))

# Feature list

# Less then 10
featured_cols = [  ]

# Less then 20
featured_cols = [  ]

# Less then 30
featured_cols = [  ]

# Less then 40
featured_cols = [  ]

# Less then 50
featured_cols = [  ]

# Less then 60
featured_cols = [  ]

# Less then 70

featured_cols = [  ]
# Less then 80
featured_cols = [  ]

# Less then 90
featured_cols = [  ]


################################################################################
# Size Matters: Word Count as a Measure of Quality on Wikipedia FEATURES
#features_cols = ["wordCount"]
################################################################################


# Select only the columns corresponding to the features in the list
#X = data[features_cols]

# Select qualityClass as the response (y)
y = data.qualityClass

X = data

#print X.shape

print 'BEFORE Feature Selection'
# 10-fold cross-validation with logistic regression PREDICTIONS
clf = LogisticRegression()
y_pred = cross_val_predict(clf, X, y, cv=10)

print metrics.classification_report(y, y_pred) 
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))



from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
#X_new = SelectKBest(chi2, k=23).fit_transform(X, y)
#
#print 'AFTER Feature Selection'
## 10-fold cross-validation with logistic regression PREDICTIONS
#clf = LogisticRegression()
#y_pred = cross_val_predict(clf, X_new, y, cv=10)
#
#print metrics.classification_report(y, y_pred) 
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))







# Find features
#inverted_X_new = [list(x) for x in zip(*X_new)]
#
#for pos in features_cols:
#    for x in inverted_X_new:
#        if (X[pos]==x).all():
#            print pos
#    

#23
#Accuracy: 0.375714285714
#MSE: 3.08714285714



#k_range = range(1, 50)
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
## plot the value of K (x-axis) versus the cross-validated accuracy (y-axis)
#plt.plot(k_range, k_scores)
#plt.xlabel('Value of K')
#plt.ylabel('Cross-Validated Accuracy')





















