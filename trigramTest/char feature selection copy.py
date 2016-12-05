# -*- coding: utf-8 -*-
""", Created on Tue Oct 25 15:12:56 2016

@author: Elias
"""
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
data = pd.read_csv(open('charTrigramsDataset2.csv'))

# Feature list
#features_cols = [ "100", "102", "152", "159", "173", "176", "177", "178", "179", "180", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "225", "262", "500", "795", "804", "920", "942", "944", "945", "970" ]

################################################################################
# Size Matters: Word Count as a Measure of Quality on Wikipedia FEATURES
#features_cols = ["wordCount"]
################################################################################


# Select only the columns corresponding to the features in the list
X = data[features_cols]

# Select qualityClass as the response (y)
y = data.qualityClass

# 10-fold cross-validation with logistic regression PREDICTIONS
clf = LogisticRegression()
y_pred = cross_val_predict(clf, X, y, cv=10)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))