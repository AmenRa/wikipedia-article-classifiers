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

# IMPORT DATASET
data = pd.read_csv(open('dataset.csv'))
#data = shuffle(data)

# only featured/non-featured articles classification
#data = pd.read_csv(open('dataset_FA_Random.csv'))

# Feature list
features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerSentence", "citationCountPerSection", "externalLinksCount", "externalLinksPerSentence", "externalLinksPerSection", "imageCount", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "linsearWriteFormula", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "adjectiveCount", "adjectivesPerSentence", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord"]


#features_cols = ["characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCountPerSentence", "citationCountPerSection", "externalLinksPerSentence", "externalLinksPerSection", "imagePerSentence", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionRatio", "exclamationRatio", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "linsearWriteFormula", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounsPerSentence", "nounsRate", "differentNounsPerSentence", "differentNounsRate", "verbsPerSentence", "verbsRate", "differentVerbsPerSentence", "differentVerbsRate", "pronounsPerSentence", "pronounsRate", "differentPronounsPerSentence", "differentPronounsRate", "adjectivesPerSentence", "differentAdjectivesPerSentence", "differentAdjectivesRate","adverbsPerSentence", "adverbsRate", "differentAdverbsPerSentence", "differentAdverbsRate", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate",  "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate",  "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate",  "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "syllablesPerWord", "charactersPerWord"]


################################################################################
# Size Matters: Word Count as a Measure of Quality on Wikipedia FEATURES
#features_cols = ["wordCount"]
################################################################################


# Select only the columns corresponding to the features in the list
X = data[features_cols]

# Select qualityClass as the response (y)
y = data.qualityClass

# NORMALIZE DATASET
#scaler = Normalizer().fit(X)
#normalizedX = scaler.transform(X)

# 10-fold cross-validation with linear regression and all features
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
scores = cross_val_score(lm, X, y, cv=10, scoring='neg_mean_squared_error')
# fox the sign of MSE scores
mse_scores = -scores
# convert from MSE to RMSE
rmse_scores = np.sqrt(mse_scores)
# calculate the avarage RMSE
print rmse_scores.mean()