

"""======================================================================================
@Uses: This file will be used to create classifier using numeric and non-numeric features
======================================================================================="""



#===========================================================================#
##==========This file wiil be used for classification======================##
# EXPR uses only the exception of the catch condition for classification
#==========================================================================##
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

"""
project  = "tomcat_"
ada_est = 100
rf_est = 75
dt_est = 57
knnl=1
knnb=1
"""

#"""
project = "cloudstack_"
ada_est =100
rf_est = 75
dt_est = 57
knnl=1
knnb=1
#"""

#"""
port=3306
user="root"
password="1234"
database="logging_level2"
table_catch_feature =project+ "catch_training2"
#result_table = "result_catch_expr"
"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level"
table_catch_feature = project+"catch_training2"
#result_table = "result_catch_expr"
#"""

random_seed_val = 0
db1= MySQLdb.connect(host="localhost", user=user, passwd=password,db=database, port=port)
select_cursor = db1.cursor()
insert_cursor  =db1.cursor()

def clean(val):
   # val ="hello + remove a*b a<>b abc(10) int a[20] int b=10^10 int fun(){print hello c/d /*smd*/ //dfdn @override<?:?>};"
    val = re.sub(r"[\+\*%-/&|^=!]", " ", val)
    val = re.sub(r"[<>\{\}\(\)\[\]]", " ", val)
    val = re.sub(r"[@#$_\\\'\":;\.,\?0-9]", " ", val)
    val = re.sub(r" +"," ", val)
    return val

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s1= re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    s2 = s1.split("_")
    
    final= " "
    for s in s2:
        final = final+" "+s
    final = final.strip()
    return final    
    
def stem_it(val):
    #print "val=", val
    temp = " ".join(PorterStemmer().stem_word(word) for word in val.split(" "))
    #print "temp=", temp
    return temp


#Read if blocks which are logged
str_logged = "select  try_loc, is_try_logged, try_log_count, have_previous_catches, previous_catches_logged, \
                      is_return_in_try, is_return_in_catch, is_catch_object_ignore, is_interrupted_exception, is_thread_sleep_try,\
                      is_throwable_exception, throw_throws_catch, if_in_try, is_assert_in_try, is_assert_in_catch, \
                      catch_exc from "+ table_catch_feature +" where catch_exc!='' and  is_catch_logged= 1"
                      
                      

print "str_logged = ", str_logged
select_cursor.execute(str_logged)
data = select_cursor.fetchall()
target = list()
logged_catch_features = list()
for d in data:
    temp = list()
    try_loc = d[0]
    is_try_logged = d[1]
    try_log_count = d[2]    
    have_previous_catches =d[3]
    previous_catches_logged = d[4]
    is_return_in_try = d[5]
    is_return_in_catch = d[6]
    is_catch_object_ignore = d[7]
    is_interrupted_exception = d[8]
    is_thread_sleep_try = d[9]
    is_throwable_exception = d[10]
    throw_throws_catch  =d[11]
    if_in_try = d[12]
    is_assert_in_try=d[13]
    is_assert_in_catch = d[14]
                      
    temp.append(try_loc)
    temp.append(is_try_logged)
    temp.append(try_log_count)    
    temp.append(have_previous_catches)
    temp.append(previous_catches_logged)
    temp.append(is_return_in_try)
    temp.append(is_return_in_catch)
    temp.append(is_catch_object_ignore)
    temp.append(is_interrupted_exception)
    temp.append(is_thread_sleep_try)
    temp.append(is_throwable_exception )
    temp.append(throw_throws_catch)
    temp.append(if_in_try)
    temp.append(is_assert_in_try)
    temp.append(is_assert_in_catch)
    #"""
    logged_catch_features.append(temp)
    target.append(1)                  

str_non_logged = "select  try_loc, is_try_logged, try_log_count, have_previous_catches, previous_catches_logged, \
                      is_return_in_try, is_return_in_catch, is_catch_object_ignore, is_interrupted_exception, is_thread_sleep_try,\
                      is_throwable_exception, throw_throws_catch, if_in_try, is_assert_in_try, is_assert_in_catch, \
                      catch_exc from "+ table_catch_feature +" where catch_exc!='' and  is_catch_logged= 0 limit 0, 827"
                      
                      

print "str_non_logged = ", str_non_logged
select_cursor.execute(str_non_logged)
data = select_cursor.fetchall()

non_logged_catch_features = list()
for d in data:
    temp = list()
    try_loc = d[0]
    is_try_logged = d[1]
    try_log_count = d[2]    
    have_previous_catches =d[3]
    previous_catches_logged = d[4]
    is_return_in_try = d[5]
    is_return_in_catch = d[6]
    is_catch_object_ignore = d[7]
    is_interrupted_exception = d[8]
    is_thread_sleep_try = d[9]
    is_throwable_exception = d[10]
    throw_throws_catch  =d[11]
    if_in_try = d[12]
    is_assert_in_try=d[13]
    is_assert_in_catch = d[14]
                      
    temp.append(try_loc)
    
    temp.append(is_try_logged)
    temp.append(try_log_count)    
    temp.append(have_previous_catches)
    temp.append(previous_catches_logged)
    temp.append(is_return_in_try)
    temp.append(is_return_in_catch)
    temp.append(is_catch_object_ignore)
    temp.append(is_interrupted_exception)
    temp.append(is_thread_sleep_try)
    temp.append(is_throwable_exception )
    temp.append(throw_throws_catch)
    temp.append(if_in_try)
    temp.append(is_assert_in_try)
    temp.append(is_assert_in_catch)
    #"""
    non_logged_catch_features.append(temp)
    target.append(0)
                      

 
total_data = logged_catch_features   + non_logged_catch_features
cv = cross_validation.ShuffleSplit(len(target), n_iter=10, test_size=0.30, 
                                   random_state=random_seed_val)

knn = KNeighborsClassifier(algorithm='auto', leaf_size=59, metric='minkowski',
    n_neighbors=6, p=2, weights='uniform')
dt  =DecisionTreeClassifier(max_depth=5)
gnb = GaussianNB() # Guasian Niave Bayes
rf =  RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
ada =    AdaBoostClassifier(n_estimators=100)
svc =     SVC(kernel="linear", C=0.025)

dt_score = cross_validation.cross_val_score(dt,np.asarray(total_data), 
                                            np.asarray(target), cv=cv)
dt_acc = cross_validation.cross_val_score(dt,np.asarray(total_data), 
         np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
dt_precision = cross_validation.cross_val_score(dt,np.asarray(total_data), 
              np.asarray(target), cv=cv,score_func=metrics.precision_score)
dt_recall = cross_validation.cross_val_score(dt,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
dt_f1= cross_validation.cross_val_score(dt,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
dt_roc = cross_validation.cross_val_score(dt,np.asarray(total_data),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
print "dt =", dt_score.mean()
print "dt accuracy =", dt_acc.mean()
print "dt precision =", dt_precision.mean()
print "dt reacll =", dt_recall.mean()
print "dt f1=", dt_f1.mean()
print "dt roc=", dt_roc.mean()

"""        
total_dt_acc = total_dt_acc +dt_acc.mean()
total_dt_precision = total_dt_precision +dt_precision.mean()
total_dt_recall = total_dt_recall +dt_recall.mean()
total_dt_f1 = total_dt_f1 + dt_f1.mean()
total_dt_roc = total_dt_roc +dt_roc.mean()
"""
    #ada_score = cross_validation.cross_val_score(ada,np.asarray(total_data), np.asarray(target), cv=cv)
    #print "ada = ", ada_score.mean()
ada_score = cross_validation.cross_val_score(ada,np.asarray(total_data), 
                                            np.asarray(target), cv=cv)
ada_acc = cross_validation.cross_val_score(ada,np.asarray(total_data), 
       np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
ada_precision = cross_validation.cross_val_score(ada,np.asarray(total_data), 
              np.asarray(target), cv=cv,score_func=metrics.precision_score)
ada_recall = cross_validation.cross_val_score(ada,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
ada_f1= cross_validation.cross_val_score(ada,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
ada_roc = cross_validation.cross_val_score(ada,np.asarray(total_data),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
print "ada =", ada_score.mean()
print "ada accuracy=", ada_acc.mean()
print "ada precision=", ada_precision.mean()
print "ada recall=", ada_recall.mean()
print "ada f1=", ada_f1.mean()
print "ada roc=", ada_roc.mean()

"""        
total_ada_acc = total_ada_acc +ada_acc.mean()
total_ada_precision = total_ada_precision +ada_precision.mean()
total_ada_recall = total_ada_recall +ada_recall.mean()
total_ada_f1 = total_ada_f1 + ada_f1.mean()
total_ada_roc = total_ada_roc +ada_roc.mean()
"""

knn_score = cross_validation.cross_val_score(knn,np.asarray(total_data), np.asarray(target), cv=cv)
print "knn = ", knn_score.mean()

knn_score = cross_validation.cross_val_score(knn,np.asarray(total_data), 
                                            np.asarray(target), cv=cv)
knn_acc = cross_validation.cross_val_score(knn,np.asarray(total_data), 
         np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
knn_precision = cross_validation.cross_val_score(knn,np.asarray(total_data), 
              np.asarray(target), cv=cv,score_func=metrics.precision_score)
knn_recall = cross_validation.cross_val_score(knn,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
knn_f1= cross_validation.cross_val_score(knn,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
knn_roc = cross_validation.cross_val_score(knn,np.asarray(total_data),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
print "knn =", knn_score.mean()
print "knn accuracy=", knn_acc.mean()
print "knn precision=", knn_precision.mean()
print "knn recall=", knn_recall.mean()
print "knn f1=", knn_f1.mean()
print "knn roc=", knn_roc.mean()

"""
total_knn_acc = total_knn_acc +knn_acc.mean()
total_knn_precision = total_knn_precision +knn_precision.mean()
total_knn_recall = total_knn_recall +knn_recall.mean()
total_knn_f1 = total_knn_f1 + knn_f1.mean()
total_knn_roc = total_knn_roc +knn_roc.mean()
"""   
   
gnb_score = cross_validation.cross_val_score(gnb,np.asarray(total_data), 
                                            np.asarray(target), cv=cv)
gnb_acc = cross_validation.cross_val_score(gnb,np.asarray(total_data), 
      np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
gnb_precision = cross_validation.cross_val_score(gnb,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.precision_score)
gnb_recall = cross_validation.cross_val_score(gnb,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
gnb_f1= cross_validation.cross_val_score(gnb,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
gnb_roc = cross_validation.cross_val_score(gnb,np.asarray(total_data),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
print "gnb =", gnb_score.mean()
print "gnb accuracy=", gnb_acc.mean()
print "gnb precision=", gnb_precision.mean()
print "gnb recall=", gnb_recall.mean()
print "gnb f1=", gnb_f1.mean()
print "gnb roc=", gnb_roc.mean()
"""
total_gnb_acc = total_gnb_acc +gnb_acc.mean()
total_gnb_precision = total_gnb_precision +gnb_precision.mean()
total_gnb_recall = total_gnb_recall +gnb_recall.mean()
total_gnb_f1 = total_gnb_f1 + gnb_f1.mean()
total_gnb_roc = total_gnb_roc +gnb_roc.mean()
"""

rf  =  RandomForestClassifier(n_estimators=75)
rf_score = cross_validation.cross_val_score(rf,np.asarray(total_data), 
                                            np.asarray(target), cv=cv)
rf_acc = cross_validation.cross_val_score(rf,np.asarray(total_data), 
         np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
rf_pre = cross_validation.cross_val_score(rf,np.asarray(total_data), 
              np.asarray(target), cv=cv,score_func=metrics.precision_score)
rf_re = cross_validation.cross_val_score(rf,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
rf_f1= cross_validation.cross_val_score(rf,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
rf_roc = cross_validation.cross_val_score(rf,np.asarray(total_data),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)

  
print "random forest acc= ", rf_acc.mean(), " f1=", rf_f1.mean(), "  rf-pre=", rf_pre.mean(), " rf-re=", rf_re.mean()     
    #rf_score = cross_validation.cross_val_score(rf,np.asarray(total_data), np.asarray(target), cv=cv)
    #print "rf = ", rf_score.mean() 