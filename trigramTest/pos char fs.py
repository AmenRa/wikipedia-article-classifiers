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


# IMPORT DATASET
data = pd.read_csv(open('datasetWithTrigrams.csv'))

# Feature list
features_cols = [ "he_","ing","ng_","_th","the","_of","of_","in_","_in","ion","on_","ed_","_an","and","nd_","er_","_to","to_","as_","DT,NNP,NNP","NNP,NNP,NNP","DT,NN,IN","NN,IN,DT","IN,DT,NNP","NNP,NNP,IN","NNP,IN,NNP","NNP,IN,DT","IN,DT,NN","DT,NN,VBD","NNS,IN,DT","NNP,NNP,VBD","JJ,NN,IN","IN,DT,JJ","DT,JJ,NN","NN,IN,NNP","IN,NNP,NNP","VBD,DT,NN","VBD,VBN,IN","VBN,IN,DT","NN,IN,NN","IN,NN,IN","JJ,NNS,IN","NN,CC,NN","IN,JJ,NNS","IN,DT,NNS","TO,VB,DT","DT,NN,NN","NNP,NNP,CC","IN,JJ,NN","NNP,CC,NNP","NNP,POS,NN","NN,IN,JJ" ]

#features_cols = [ "he ","ing","ng "," th","the"," of","of ","in "," in","ion","on ","ed "," an","and","nd ","er "," to","to ","as ","DT,NNP,NNP","NNP,NNP,NNP","DT,NN,IN","NN,IN,DT","IN,DT,NNP","NNP,NNP,IN","NNP,IN,NNP","NNP,IN,DT","IN,DT,NN","DT,NN,VBD","NNS,IN,DT","NNP,NNP,VBD","JJ,NN,IN","IN,DT,JJ","DT,JJ,NN","NN,IN,NNP","IN,NNP,NNP","VBD,DT,NN","VBD,VBN,IN","VBN,IN,DT","NN,IN,NN","IN,NN,IN","JJ,NNS,IN","NN,CC,NN","IN,JJ,NNS","IN,DT,NNS","TO,VB,DT","DT,NN,NN","NNP,NNP,CC","IN,JJ,NN","NNP,CC,NNP","NNP,POS,NN","NN,IN,JJ" ]

################################################################################
# Size Matters: Word Count as a Measure of Quality on Wikipedia FEATURES
#features_cols = ["wordCount"]
################################################################################


# Select only the columns corresponding to the features in the list
X = data[features_cols]

# Select qualityClass as the response (y)
y = data.qualityClass


print 'BEFORE Feature Selection'
# 10-fold cross-validation with logistic regression PREDICTIONS
clf = LogisticRegression()
y_pred = cross_val_predict(clf, X, y, cv=10)

print metrics.classification_report(y, y_pred) 
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))

#X_new = SelectKBest(chi2, k=25).fit_transform(X, y)
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




#k_range = range(1, 53)
#k_scores = []
#for k in k_range:
#   X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
#   clf = LogisticRegression()
#   y_pred = cross_val_predict(clf, X_new, y, cv=10)
#   print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#   k_scores.append(metrics.accuracy_score(y, y_pred))
#print k_scores
#
#import matplotlib.pyplot as plt
##%matplotlib inline
#
## plot the value of K (x-axis) versus the cross-validated accuracy (y-axis)
#plt.plot(k_range, k_scores)
#plt.xlabel('Value of K')
#plt.ylabel('Cross-Validated Accuracy')


