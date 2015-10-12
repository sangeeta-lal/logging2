#!/usr/bin/python

#
# Example boxplot code
#


import numpy as np
import pylab
import matplotlib
import sklearn
from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import MySQLdb
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn import cross_validation
import scipy.sparse
import re
from nltk.stem.porter import PorterStemmer
from sklearn import metrics



target  =list()

target.append(1)
target.append(1)
target.append(1)
target.append(1)

temp_p =list()
temp_p.append(30)
temp_p.append(25)
temp_p.append(32)
temp_p.append(26)  

text_p_features = list()
text_p_features.append("rain rain")
text_p_features.append("rain")
text_p_features.append("rain wind")
text_p_features.append("rain")

target.append(0)
target.append(0)
target.append(0)
target.append(0)

temp_n = list()
temp_n.append(25)
temp_n.append(30)
temp_n.append(25)
temp_n.append(32)  

text_n_features = list()
text_n_features.append("wind wind")
text_n_features.append("wind")
text_n_features.append("wind")
text_n_features.append("wind wind ")

print temp_p,  " tempn = ", temp_n
print "text p = ", text_p_features,  "  text n = ", text_n_features

total_text = text_p_features + text_n_features


print "total text = ", total_text
vectorizer = TfidfVectorizer(min_df=1)
total_data =  vectorizer.fit_transform( np.asarray(total_text))
print total_data

"""
 x_data_tfidf=vectorizer.fit_transform( np.asarray(temp_total_data))
     target_arr = np.asarray(target)
     
     print "total_data", temp_total_data
     print "Tf-idf= ", x_data_tfidf.toarray()
     
     n_samples = x_data_tfidf.shape[0]
     cv = cross_validation.ShuffleSplit(n_samples, n_iter=10, test_size=0.3, random_state=0)
    
"""


"""
vectorizer = TfidfVectorizer(min_df=1)
total_catch_t_features =  logged_catch_t_features + non_logged_catch_t_features
x_total_catch_t_features=vectorizer.fit_transform(total_catch_t_features)
print "shape of the feature", x_total_catch_t_features.shape

total_catch_n_features =  logged_catch_n_features  +  non_logged_catch_n_features
x_total_catch_n_features_array = np.asarray(total_catch_n_features)
print x_total_catch_n_features_array.shape

total_data = np.hstack([x_total_catch_t_features.toarray(), x_total_catch_n_features_array])
print total_data
"""

cv = cross_validation.ShuffleSplit(len(target), n_iter=10, test_size=0.30, 
                                   random_state=0)

knn = KNeighborsClassifier(algorithm='auto', leaf_size=59, metric='minkowski',
    n_neighbors=4, p=2, weights='uniform')
dt  =DecisionTreeClassifier(max_depth=5)
gnb = GaussianNB() # Guasian Niave Bayes
rf =  RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
ada =    AdaBoostClassifier(n_estimators=100)
svc =     SVC(kernel="linear", C=0.025)

dt_score = cross_validation.cross_val_score(dt,total_data.toarray(),
                                            np.asarray(target), cv=cv)
dt_acc = cross_validation.cross_val_score(dt,total_data.toarray(),
         np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
dt_precision = cross_validation.cross_val_score(dt,total_data.toarray(),
              np.asarray(target), cv=cv,score_func=metrics.precision_score)
dt_recall = cross_validation.cross_val_score(dt,total_data.toarray(),
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
dt_f1= cross_validation.cross_val_score(dt,total_data.toarray(),
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
dt_roc = cross_validation.cross_val_score(dt,total_data.toarray(),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
print "dt =", dt_score.mean()
print "dt accuracy =", dt_acc.mean()
print "dt precision =", dt_precision.mean()
print "dt reacll =", dt_recall.mean()
print "dt f1=", dt_f1.mean()
print "dt roc=", dt_roc.mean()

  