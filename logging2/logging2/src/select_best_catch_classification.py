
#===========================================================================#
##==========This file wiil be used for classification======================##
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


project  = "tomcat_"
#project = "cloudstack_"
#"""
port=3306
user="root"
password="1234"
database="logging_level2"
table_catch_feature =project+ "catch_train"

"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level2"
table_catch_feature = project+"catch_train"
#"""

random_seed_val = 0
db1= MySQLdb.connect(host="localhost", user=user, passwd=password,db=database, port=port)
select_cursor = db1.cursor()
insert_cursor = db1.cursor()

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
str_logged = "select   package, class, method,  exp, catch_train, logged from "+ table_catch_feature +" where exp!='' and \
 logged= 1"

print "str_logged = ", str_logged
select_cursor.execute(str_logged)

logged_catch_feature = list()
target = list()

logged_data = select_cursor.fetchall()
for temp in logged_data:
    package_name= temp[0]
    class_name= temp[1]
    method_name = temp[2]
    expr = temp[3]
    catch_train = temp[4]
    
    package_name = clean(package_name)
    class_name = clean(class_name)
    method_name = clean(method_name)
    expr = clean(expr)
    catch_train = clean(catch_train)
    
    total_con = (package_name+" "+class_name+" "+method_name+" "+expr+" "+catch_train)
    total_con_arr = total_con.split(" ")
    
    #print "Total con=", total_con
    train_con = " "
    for tca in total_con_arr:
        temp = convert(tca)
        train_con =train_con+" "+ temp
        
    #print "Total Code modified=", train_con
    
    train_con = stem_it(train_con.strip())
    logged_catch_feature.append(train_con.strip())
    #target.append(1)

print "target size=", len(target)

#======== Not Logged===========#
str_not_logged = "select   package, class, method,  exp, catch_train, logged from "+table_catch_feature+" where \
exp!='' and logged= 0"

#store_target=list()
#for t in target:
#    store_target.append(1)
    
print "str_not_logged = ", str_not_logged
select_cursor.execute(str_not_logged)

rand_array  = [0]
not_logged_data = select_cursor.fetchall()
#print "before=", not_logged_data

for random_seed_val in rand_array:
     np.random.seed(random_seed_val)
     indices = np.random.permutation(len(not_logged_data))[:len(logged_catch_feature)]
     target = list()
     for temp_count in  range(1,len(logged_catch_feature)+1):
         target.append(1)
    
     print indices     
     index=-1
     not_logged_catch_feature = list()     
     for temp in not_logged_data:
         index= index+1
         if index in indices:
             package_name= temp[0]
             class_name= temp[1]
             method_name = temp[2]
             expr = temp[3]
             catch_train = temp[4]
    
             package_name = clean(package_name)
             class_name = clean(class_name)
             method_name = clean(method_name)
             expr = clean(expr)
             catch_train = clean(catch_train)
    
             total_con = (package_name+" "+class_name+" "+method_name+" "+expr+" "+catch_train)
             total_con_arr = total_con.split(" ")
    
             #print "Total con=", total_con
             train_con = " "
             for tca in total_con_arr:
                 temp = convert(tca)
                 train_con =train_con+" "+ temp
        
             #print "Total Code modified=", train_con
             train_con = stem_it(train_con.strip())
             not_logged_catch_feature.append(train_con.strip())
             target.append(0)

     print "target size=", len(target)
     print " not logged final", not_logged_catch_feature
    

     temp_total_data = logged_catch_feature+ not_logged_catch_feature
    
     vectorizer = TfidfVectorizer(min_df=1)
     x_data_tfidf=vectorizer.fit_transform( np.asarray(temp_total_data))
     target_arr = np.asarray(target)
     
     print "total_data", temp_total_data
     print "Tf-idf= ", x_data_tfidf.toarray()
     
     n_samples = x_data_tfidf.shape[0]
     cv = cross_validation.ShuffleSplit(n_samples, n_iter=10, test_size=0.3, random_state=0)  
     
     """
     for i in range(1,51):
        for j in range(1, 41):
            for k in range(2, 3):
                #knn = KNeighborsClassifier()
                knn=KNeighborsClassifier(algorithm='auto', leaf_size=i, metric='minkowski', n_neighbors=j, p=k, weights='uniform')                               
                knn_acc = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(), target_arr, cv=cv,scoring= 'accuracy')
                knn_f1 = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(),target_arr, cv=cv,scoring= 'f1')
                n_str = "insert into knn_temp_result_catch values(\'"+project+"\',"+(str)(i)+","+(str)(j)+","+(str)(k)+","+(str)(knn_acc.mean())+","+(str)(knn_f1.mean())+")"
                insert_cursor.execute(n_str)
                db1.commit() 
     """ 
     #"""
     for i in range(1,101):
         dt  =  DecisionTreeClassifier(max_depth=i)
         dt_acc = cross_validation.cross_val_score(dt,   x_data_tfidf.toarray(), target_arr, cv=cv)
         dt_f1 = cross_validation.cross_val_score(dt,   x_data_tfidf.toarray(), target_arr, cv=cv, scoring='f1')
         n_str = "insert into dt_temp_result_catch values(\'"+project+"\',"+(str)(i)+","+(str)(dt_acc.mean())+","+(str)(dt_f1.mean())+")"
         insert_cursor.execute(n_str)
         db1.commit() 
     #"""    
     """
     for j in range(1,101):
          rf  =  RandomForestClassifier(n_estimators=j)
          rf_acc = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='accuracy')
          rf_f1 = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='f1')
          n_str = "insert into rf_temp_result_catch values(\'"+project+"\',"+(str)(0)+","+(str)(j)+","+(str)(0)+","+(str)(rf_acc.mean())+","+(str)(rf_f1.mean())+")"
          insert_cursor.execute(n_str)
          db1.commit() 
     """            
     """
   
     for i in range(1,101):
         ada =  AdaBoostClassifier(n_estimators=i)
         ada_acc = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv)
         #ada_pre = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='precision')
         #ada_re = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='recall')
         ada_f1 = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='f1')
         n_str = "insert into ada_temp_result_catch values(\'"+project+"\',"+(str)(i)+","+(str)(ada_acc.mean())+","+(str)(ada_f1.mean())+")"
         insert_cursor.execute(n_str)
         db1.commit()          
         
    """     
     
     """
     knn = KNeighborsClassifier()
     KNeighborsClassifier(algorithm='auto', leaf_size=1, metric='minkowski', n_neighbors=4, p=2, weights='uniform')
     
     dt  =  DecisionTreeClassifier(max_depth=5)
     gnb =  GaussianNB() # Guasian Niave Bayes
     rf  =  RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
     ada =  AdaBoostClassifier(n_estimators=100)
     svc =  SVC(kernel="linear", C=0.025)
                                
     knn_score = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(), target_arr, cv=cv,scoring= 'accuracy')
    # knn_cm = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(), target_arr, cv=cv, 
    #                                            scoring=metrics.confusion_matrix )
     dt_score = cross_validation.cross_val_score(dt,   x_data_tfidf.toarray(), target_arr, cv=cv)
     rf_score = cross_validation.cross_val_score(rf,   x_data_tfidf.toarray(), target_arr, cv=cv)
     ada_score = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv)
     #svc_score = cross_validation.cross_val_score(svc, x_data_tfidf.toarray(), target_arr, cv=cv)     
     
     print "knn accuracy", knn_score.mean()
     print "dt accuracy",  dt_score.mean()
     print "rf accuracy",  rf_score.mean()
     print "ada accuracy", ada_score.mean()
     #print "svc accuracy", svc_score.mean()
     """                                                        
     
    
     
     
     