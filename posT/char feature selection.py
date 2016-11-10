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
data = pd.read_csv(open('charTrigramsDataset.csv'))

# Feature list
#features_cols = [ "The","nt ","ng ","s t","he ","e o","f t","men","wit"," th","e i","ent","ion"," of","ed ","in "," an","d t","s o","te ","the",". T","for","by ","en "," to","on "," 20"," ar","ing"," be","ts ","com","tio","ati","ere","d i","n t","all","of ","nd ","ate","and","ist"," pr"," in","er ","se ","to ","an ","sta"," se"," co","ver","es ",", a","e a","s, ","n i","e t","al ","e c","ons"," fo"," wa","iti"," wh"," de","re ","s a","as "," Th"," a ","ith"," is","ity","e s","ly ","rs ","le ","e w","ter","th ","or ","s. ","is ","ry "," re"," 19"," wi","was","d a","ica","est"," on","ers","tin","at "," by","s i","n a"," as","me ","g t","st ","ted","s w","ns "," hi" ]

#features_cols = [ "200","The"," Pa","ame","nt ","ng ","s t","he ","e o","f t","men","t a","wit"," th","ge ","e i","ent","str","ion"," of","e b","din","enc","ed ","in "," an","d t","ber","s o","te ","the","mbe",". T","for","by ","en "," to","ce ","on "," 20","ric",", t","lan"," ar","t w","des","ing"," be","ts ","com","tio","ati","r o","ere","d i","n t","era","all","ch ","of ","nd ","ate","d o","and","ist","rat","ive","t o"," pr","ded"," in","fro","y o","er ","se ","to ","one","par","ore","an ","sta"," se","rom"," co","con","ver","es ",", a","e a","ll ","tic","d b","ian","s, "," me","n i","e t","h a","sti","al "," ma","her"," ha","e c","ons","cti"," fo"," wa","iti"," wh","rea","lis","t i","o t","ich"," de"," we","re ","s a","ic ","as ","ect"," Th","eve"," a ","e, ","e p"," wo","rou","inc","ith","out"," pa","ear","rit","tur","res"," is","ity","ntr","e s","ite","ly ","sed","rs ","le ","e w"," bo","y t"," st"," si","ste","'s ","e. "," so","ter","ide","th ","or ","rin","s. ","is ","s b","ry ","eat"," re","nce"," 19"," wi","clu","man","om ","was","ure"," at","d a","ica","e f","r t"," di","ty ","ain","est","ove","ut ","art","ies","int","n o","mer"," on","ill","s c","ers","tin","s r","at ","tha","hen","orm","his","ren","tor","t t","ome"," by","nal","hat","s i","n a","der"," as","sin","me ","g t","st ","nti","ran","oun","ted","d s","pro","are","n, ","nte"," he","s w","nat","y, ","ve "," Ma","ina","ns "," al","ort","tra","red","cal"," Co",".  ",". I","nde","e m","ine","ne "," It","d w","de "," In"," or","s f"," ba"," mo","per","ess","eri"," fr","ase"," hi","age","e e","rt ","lin","wor","ial"," fi","has","tes",". H"," He","ali"," Ch" ]

features_cols = [ "199","200","The","ish"," Pa","rli","ame","nt ","ng ","s t","he ","e o","f t","men","t a","d, ","wit","hin"," th","e U","ld ","ita","ge ","e i","n c","ent","ral","str","uct","ion"," of","e b","din","omm","enc","ed ","in ","e 1"," an","d t","ber","s o","hei","irs","te ","the"," ne","g o"," Se","pte","mbe",". T","for","by ","en "," to","ok ","pla","ce ","on ","cto"," 20","ric"," Mi","les",", t","lan"," ar","chi","t w","ho ","des","ign"," bu","ing","ied"," be","ts ","com","ple","tio","n. "," un","ew "," ro","ati","cha","r o","ere"," ho","use","d i","n t","era","all","e C","ch ","of ","nd ","ate","d o","and"," ad","min","ist","rat","ive"," ac","por","t o"," pr","ded"," in","s l","eas","fro","m t","y o","gh ","tis"," br","oug","er ","se ","fer"," el","eme","nts","to ","one"," pu","par","tar","y c","omp",", h","ous","ore","an ","sta"," se","rom","g a","its"," co","nst","n h","ave","con","ver"," ch","es ","on,","t, ",", a","mpa","ny ","wer","e a","ll ","cri","tic","d b","y p","oli","ian","s, "," me","pub","lic","che","ope","n i","n 2",", i","so ","e t","han","ree"," la","h a","n e","sti","mat","al "," mi","lli"," ma","her","ini","tia",". A","bli"," ha","e c","ons","tru","cti"," fo","ord"," wa","s e","she","lud","tem"," cr","iti"," wh","ct ","rea","lis","t i","o t","ich"," de","sig"," we","re "," De","s a","a m","d p","ic ","as ","arc","ect","l a"," Th","ime","o a","eve"," a ","e, "," pe","e p"," wo","ume","rou","war","ds ","inc"," St","ize","d h","our","aft","lit","y w","ith","out"," pa","e l","ast","ear","rit","tur","ris","res","e S"," is","cat","ity"," ce","ntr","e s","ite","evi","ly ","hou","sed","e h","rte","rs ","le ","hic","e w","ay ","g. "," bo","und","ary","y t","ong"," st","ret"," no","rth","ern"," si","ste","rn ","sid","whe","anc","'s ","e. ","d's","ose","ood","ad "," so","uth","ter","n s","ide","th "," vi","sit","or ","att","rac","n w","h o","rin"," Sa","s. ","In "," im","med","nit","is ","lac",", w","s b","ans","nta","ry ","d A","eat","hav","een"," ex","ten"," re","nce"," 19"," wi","tai","el ","fic","e d","clu","man","om ","was","end","own"," le","lat","ure"," at"," Un",", s","cre","d a"," po","ica","two","Uni","e f","r t"," di","pre","us ","ty ","ain","s h","est","r i","ond","on.","s d","ire","ove","d f","n f","tho","ut ","r a","h t","ona","art","y a","mon","ies","int","sio","n o","mer"," Hi"," on"," Ca","ill","off","t. ","thi","s c","ers","tin","s r"," Ne"," it","ned","at "," fa","s s","tat","pos","e (","tha","). ","low","e A","pri","hen","r w","ele","a c","et ","ss ","Sta","rti","orm","his","lar","ula","ren","lec","tor","r 1","abl","rec","t t","ome","led"," by","nal","r, ","hat","be ","lly","s i","n a","der"," kn"," as","sin","ton"," An","me ","ia ","g t","ant"," ra","st ","not"," en","nti","fte","ran","oun","it ","ey ","oin","eci","nto","e r","ust"," cl","New","ted","any","uld"," ab"," ag","d s","hor","pro","ice","ssi","y s","pec","ifi","are","llo","n, ","nte","tit"," he","ner","esi","shi","hoo","s w"," su","tte","nat","rch","y, ","ard","ve "," Ma","whi","ina","dis","ns ","ani","ngs"," te","unt"," al"," sh","ort","tra","ke ","sen","d d"," Ju","red","lle","rk ","cal"," Co","gin","nin","mpl","cia","l o",".  ","ght","t c","den","y. ","act"," ta",". I","app","tal","g i","itu"," ou","t f"," Ar","es,"," ge","nde","o u","ndi","nic","y f"," us"," ca","met","vid","eir","ari"," fe","atu","e m","ost","rel","ine","ins","ne "," It"," sa","fir","d w","thr","ont","ble","rie","ein","val","spe","d. "," gr","ass","de "," In","owe",", b"," tr","als","n p","ack"," li","ks ","ora","tiv","s p","ces","ser","rig","ger","gra"," ev","rs,"," or","ene","ow ","k. ","ban","s f"," ba","ced"," mo","d c","t s","ir ","yea","nor","uri","ece","per","can","ee ","ess"," On","eri","fea"," fr","ase","urc"," hi","f c","ute","tan","y i","r s","es.","age","tom"," ri","ves"," do","wn ","e e","ile","cle","mil","ar ","oth","emb","e \"","rt ","tab"," sp","sto","lin","ori","igh","y b","ork","d e","uti","s m","ved","wor","lso","  T","ial","ell","erv","r e"," fi","a f","ck ","ual","lea","has","who"," na","ath","nes","edi","a a","col","cor","eng","l t","fou","son","ook","ily","th.","t h","old","ncl","udi"," Bo"," So","y h","ang","suc","a s"," Ba","ono","kin","rst","ors","spo","ram","il ","rge","omi","n A","g e","tes","r \"","sts","n 1","ima"," No","rsi","ade","mar"," Au","uar","ude","rre","dit","rd ","sec",". H","cou","e F","kno"," La","van","ls ","imi"," ti"," He","eca","eco","ali","log","ugh"," Pe","201","Mar","cie","hir","ria","olo"," Am",". \"","but","uni","hil"," Da","He "," Di","o i","bod"," Ch","It ","tri","gen"," \"S","usi","n N"," Re","ert","All","nam","vel","e N","bec","ick","f A","gan","rm ","bor","rts","ero","rld","y D","t u","bas","da ","y I","mig","yer","ne.","s k"," Al","me," ]

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

#print 'BEFORE Feature Selection'
# 10-fold cross-validation with logistic regression PREDICTIONS
#clf = LogisticRegression()
#y_pred = cross_val_predict(clf, X, y, cv=10)
#
#print metrics.classification_report(y, y_pred) 
#print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
#print 'MSE: ' + str(metrics.mean_squared_error(y, y_pred))



#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2
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



k_range = range(1, 50)
k_scores = []
for k in k_range:
    X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
    clf = LogisticRegression()
    y_pred = cross_val_predict(clf, X_new, y, cv=10)
    print 'Accuracy: ' + str(metrics.accuracy_score(y, y_pred) )
    k_scores.append(metrics.accuracy_score(y, y_pred))
print k_scores

import matplotlib.pyplot as plt
#%matplotlib inline

# plot the value of K (x-axis) versus the cross-validated accuracy (y-axis)
plt.plot(k_range, k_scores)
plt.xlabel('Value of K')
plt.ylabel('Cross-Validated Accuracy')





















