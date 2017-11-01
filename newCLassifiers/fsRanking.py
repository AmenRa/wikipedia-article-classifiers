print(__doc__)

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

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier

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

features_cols = ["d_a", "citationCount", "characterCount", "syllableCount", "citationCountPerSection", "subordinatingPrepositionAndConjunctionCount", "meanParagraphSize", "toBeVerbCount", "wordCount"]

# Select only the columns corresponding to the features in the list
X = data[features_cols]

X.sample(frac=1)

# Select qualityClass as the response (y)
y = data.qualityClass




# Build a forest and compute the feature importances
# forest = RandomForestClassifier(n_estimators=200, random_state=5, n_jobs=-1, class_weight='auto')
#
# forest.fit(X, y)
# importances = forest.feature_importances_
# std = np.std([tree.feature_importances_ for tree in forest.estimators_],
#              axis=0)
# indices = np.argsort(importances)[::-1]
#
# # Print the feature ranking
# print("Feature ranking:")
#
# for f in range(X.shape[1]):
#     print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
#
# # Plot the feature importances of the forest
# plt.figure()
# plt.title("Feature importances")
# plt.bar(range(X.shape[1]), importances[indices],
#        color="r", yerr=std[indices], align="center")
# plt.xticks(range(X.shape[1]), indices)
# plt.xlim([-1, X.shape[1]])
# plt.show()




print 'RandomForestClassifier'
# 10-fold cross-validation with random forst PREDICTIONS
clf = RandomForestClassifier(n_estimators=200, random_state=5, n_jobs=-1, class_weight='auto')
y_pred = cross_val_predict(clf, X, y, cv=20)

print metrics.classification_report(y, y_pred)
print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))
