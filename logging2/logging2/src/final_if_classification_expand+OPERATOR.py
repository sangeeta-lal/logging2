
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


#"""
project  = "tomcat_"
ada_est = 100
rf_est = 65
dt_est = 83
knnl=2
knnb=1
#"""

"""
project = "cloudstack_"
ada_est = 100
rf_est = 65
dt_est = 83
knnl=2
knnb=1
#limit is defined 0, 50000
"""
"""
port=3306
user="root"
password="123"
database="logging_level"
table_if_feature =project+ "if_train"
result_table = "result_if_expand_operator"
"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level"
table_if_feature = project+"if_train"
result_table = "result_if_expand_operator"
#"""

random_seed_val = 0
db1= MySQLdb.connect(host="localhost", user=user, passwd=password,db=database, port=port)
select_cursor = db1.cursor()
insert_cursor  =db1.cursor()

def clean(val):
   # val ="hello + remove a*b a<>b abc(10) int a[20] int b=10^10 int fun(){print hello c/d /*smd*/ //dfdn @override<?:?>};"
   
    #val = re.sub(r"[\+\*%-/&|^=!]", " ", val) #Operators are not removed
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
str_logged = "select   package, class, method,  expr, if_train, logged from "+ table_if_feature +" where expr not like \
'%.isDebugEnabled()' and expr not like '%.isInfoEnabled()' and expr not like '%.isTraceEnabled()'\
  and expr not like '%.isErrorEnabled()' and expr not like '%.isFatalEnabled()' and expr not like '%.isWarnEnabled()'\
  and expr!='' and logged= 1 limit 0, 4000"

print "str_logged = ", str_logged
select_cursor.execute(str_logged)

logged_if_feature = list()
target = list()

logged_data = select_cursor.fetchall()
for temp in logged_data:
    package_name= temp[0]
    class_name= temp[1]
    method_name = temp[2]
    expr = temp[3]
    if_train = temp[4]
    
    package_name = clean(package_name)
    class_name = clean(class_name)
    method_name = clean(method_name)
    expr = clean(expr)
    if_train = clean(if_train)
    
    total_con = (package_name+" "+class_name+" "+method_name+" "+expr+" "+if_train)
    total_con_arr = total_con.split(" ")
    
    #print "Total con=", total_con
    train_con = " "
    for tca in total_con_arr:
        temp = convert(tca)
        train_con =train_con+" "+ temp
        
    #print "Total Code modified=", train_con
    
    train_con = stem_it(train_con.strip())
    logged_if_feature.append(train_con.strip())
    #target.append(1)

print "target size(logged)=", len(logged_if_feature)
print logged_if_feature

knn_10_acc = 0.0
knn_10_pre = 0.0
knn_10_re = 0.0
knn_10_f1 = 0.0

rf_10_acc = 0.0
rf_10_pre = 0.0
rf_10_re = 0.0
rf_10_f1 = 0.0

ada_10_acc = 0.0
ada_10_pre = 0.0
ada_10_re = 0.0
ada_10_f1 = 0.0

dt_10_acc = 0.0
dt_10_pre = 0.0
dt_10_re = 0.0
dt_10_f1 = 0.0

#======== Not Logged===========#
str_not_logged = "select   package, class, method,  expr, if_train, logged from "+table_if_feature+" where expr not like \
'%.isDebugEnabled()' and expr not like '%.isInfoEnabled()' and expr not like '%.isTraceEnabled()'\
  and expr not like '%.isErrorEnabled()' and expr not like '%.isFatalEnabled()' and expr not like '%.isWarnEnabled()'\
  and expr!='' and logged= 0 "

#store_target=list()
#for t in target:
#    store_target.append(1)
    
print "str_not_logged = ", str_not_logged
select_cursor.execute(str_not_logged)

rand_array  = [0]#,1,2,3,4,5,6,7,8,9,10]
not_logged_data = select_cursor.fetchall()
#print "before=", not_logged_data

for random_seed_val in rand_array:
     np.random.seed(random_seed_val)
     indices = np.random.permutation(len(not_logged_data))[:len(logged_if_feature)]
     target = list()
     for temp_count in  range(1,len(logged_if_feature)+1):
         target.append(1)
    
     print indices     
     index=-1
     not_logged_if_feature = list()     
     for temp in not_logged_data:
         index= index+1
         if index in indices:
             package_name= temp[0]
             class_name= temp[1]
             method_name = temp[2]
             expr = temp[3]
             if_train = temp[4]
    
             package_name = clean(package_name)
             class_name = clean(class_name)
             method_name = clean(method_name)
             expr = clean(expr)
             if_train = clean(if_train)
    
             total_con = (package_name+" "+class_name+" "+method_name+" "+expr+" "+if_train)
             total_con_arr = total_con.split(" ")
    
             #print "Total con=", total_con
             train_con = " "
             for tca in total_con_arr:
                 temp = convert(tca)
                 train_con =train_con+" "+ temp
        
             #print "Total Code modified=", train_con
             train_con = stem_it(train_con.strip())
             not_logged_if_feature.append(train_con.strip())
             target.append(0)

     print "target size=", len(target)
     print " not logged final", not_logged_if_feature
    

     temp_total_data = logged_if_feature+ not_logged_if_feature
    
     vectorizer = TfidfVectorizer(min_df=1)
     x_data_tfidf=vectorizer.fit_transform( np.asarray(temp_total_data))
     target_arr = np.asarray(target)
     
     print "total_data", temp_total_data
     print "Tf-idf= ", x_data_tfidf.toarray()
     
     n_samples = x_data_tfidf.shape[0]
     cv = cross_validation.ShuffleSplit(n_samples, n_iter=10, test_size=0.3, random_state=0)
     gnb =  GaussianNB() # Guasian Niave Bayes
     #svc =  SVC(kernel="linear", C=0.025)
     
     """
     #knn = KNeighborsClassifier()
     knn=KNeighborsClassifier(algorithm='auto', leaf_size=knnl, metric='minkowski', n_neighbors=knnb, p=2, weights='uniform')                               
     knn_acc = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(), target_arr, cv=cv,scoring= 'accuracy')
     knn_f1 = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(),target_arr, cv=cv,scoring= 'f1')
     knn_pre = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(),target_arr, cv=cv,scoring= 'precision')
     knn_re = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(),target_arr, cv=cv,scoring= 'recall')    
     """   
     dt  =  DecisionTreeClassifier(max_depth=dt_est)
     dt_acc = cross_validation.cross_val_score(dt,x_data_tfidf.toarray(), target_arr, cv=cv, scoring='accuracy')
     dt_f1 = cross_validation.cross_val_score(dt,x_data_tfidf.toarray(), target_arr, cv=cv,scoring='f1')
     dt_pre = cross_validation.cross_val_score(dt,x_data_tfidf.toarray(), target_arr, cv=cv, scoring='precision')     
     dt_re = cross_validation.cross_val_score(dt,x_data_tfidf.toarray(), target_arr, cv=cv, scoring='recall')    
     
     rf  =  RandomForestClassifier(n_estimators=rf_est)
     rf_acc = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='accuracy')
     rf_f1 = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='f1')
     rf_pre = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='precision')
     rf_re = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='recall')
     
     ada =  AdaBoostClassifier(n_estimators=ada_est)
     ada_acc = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='accuracy')
     ada_f1 = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='f1')
     ada_pre = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='precision')
     ada_re = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='recall')
     """              
     knn_10_acc = knn_10_acc + knn_acc.mean()*100
     knn_10_pre = knn_10_pre +knn_pre.mean()*100
     knn_10_re = knn_10_re + knn_re.mean()*100
     knn_10_f1 = knn_10_f1 + knn_f1.mean()*100
     """
                               
     dt_10_acc = dt_10_acc + dt_acc.mean()*100
     dt_10_pre = dt_10_pre + dt_pre.mean()*100
     dt_10_re = dt_10_re +  dt_re.mean()*100
     dt_10_f1 = dt_10_f1 +  dt_f1.mean()*100
        
     rf_10_acc = rf_10_acc + rf_acc.mean()*100
     rf_10_pre = rf_10_pre + rf_pre.mean()*100
     rf_10_re = rf_10_re +  rf_re.mean()*100
     rf_10_f1 = rf_10_f1 +  rf_f1.mean()*100
        
     
     ada_10_acc = ada_10_acc + ada_acc.mean()*100
     ada_10_pre = ada_10_pre + ada_pre.mean()*100
     ada_10_re = ada_10_re +  ada_re.mean()*100
     ada_10_f1 = ada_10_f1 +  ada_f1.mean()*100

#final_knn_acc=  knn_10_acc#/10
#final_knn_pre=  knn_10_pre#/10
#final_knn_re=  knn_10_re#/10
#final_knn_f1=  knn_10_f1#/10



final_dt_acc=  dt_10_acc # /10
final_dt_pre=  dt_10_pre #/10
final_dt_re=  dt_10_re #/10
final_dt_f1=  dt_10_f1 #/10

final_rf_acc=  rf_10_acc#/10
final_rf_pre=  rf_10_pre#/10
final_rf_re=  rf_10_re#/10
final_rf_f1=  rf_10_f1#/10

final_ada_acc=  ada_10_acc#/10
final_ada_pre=  ada_10_pre#/10
final_ada_re=  ada_10_re#/10
final_ada_f1=  ada_10_f1#/10


db2= MySQLdb.connect(host="localhost", user=user, passwd=password,db=database, port=port)
insert_cursor  =db2.cursor()
#insert_str =  "insert into " +result_table+" values('"+project+"\',\'knn\',"+(str)(final_knn_acc)+","+(str)(final_knn_pre)+","+(str)(final_knn_re)+","+(str)(final_knn_f1)+")"
#insert_cursor.execute(insert_str)
insert_str =  "insert into " +result_table+" values('"+project+"\',\'dt\',"+(str)(final_dt_acc)+","+(str)(final_dt_pre)+","+(str)(final_dt_re)+","+(str)(final_dt_f1)+")"
print " dt=", insert_str
insert_cursor.execute(insert_str)
insert_str =  "insert into " +result_table+" values('"+project+"\',\'rf\',"+(str)(final_rf_acc)+","+(str)(final_rf_pre)+","+(str)(final_rf_re)+","+(str)(final_rf_f1)+")"
print "rf=", insert_str
insert_cursor.execute(insert_str)
insert_str =  "insert into " +result_table+" values('"+project+"\',\'ada\',"+(str)(final_ada_acc)+","+(str)(final_ada_pre)+","+(str)(final_ada_re)+","+(str)(final_ada_f1)+")"
print "ada=", insert_str
insert_cursor.execute(insert_str)
db2.commit()


#print "dt=", dt_10_acc/10
#print "rf=", rf_10_acc/10
#print "ada=", ada_10_acc/10   



"""
     for i in range(1,1001):
        for j in range(1, 1001):
            for k in range(1, 1001):
                knn = KNeighborsClassifier()
                KNeighborsClassifier(algorithm='auto', leaf_size=i, metric='minkowski', n_neighbors=j, p=k, weights='uniform')                               
                knn_acc = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(), target_arr, cv=cv,scoring= 'accuracy')
                knn_f1 = cross_validation.cross_val_score(knn, x_data_tfidf.toarray(),target_arr, cv=cv,scoring= 'f1')
                n_str = "insert into knn_temp_result_if values(\'"+project+"\',"+(str)(i)+","+(str)(j)+","+(str)(k)+","+(str)(knn_acc.mean())+","+(str)(knn_f1.mean())+")"
                insert_cursor.execute(n_str)
                db1.commit() 
     
     for i in range(1,1001):
         dt  =  DecisionTreeClassifier(max_depth=i)
         dt_acc = cross_validation.cross_val_score(dt,   x_data_tfidf.toarray(), target_arr, cv=cv)
         dt_f1 = cross_validation.cross_val_score(dt,   x_data_tfidf.toarray(), target_arr, cv=cv, scoring='f1')
         n_str = "insert into dt_temp_result_if values(\'"+project+"\',"+(str)(i)+","+(str)(dt_acc.mean())+","+(str)(dt_f1.mean())+")"
         insert_cursor.execute(n_str)
         db1.commit() 
     
     for i in range(1,1001):
         for j in range(1, 1001):
             for k in range(1, 1001):
                 rf  =  RandomForestClassifier(max_depth=i, n_estimators=j, max_features=j)
                 rf_acc = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv)
                 rf_f1 = cross_validation.cross_val_score(rf, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='f1')
                 n_str = "insert into rf_temp_result_if values(\'"+project+"\',"+(str)(i)+","+(str)(j)+","+(str)(k)+","+(str)(rf_acc.mean())+","+(str)(rf_f1.mean())+")"
                 insert_cursor.execute(n_str)
                 db1.commit() 
      
     for i in range(1,1001):
         ada =  AdaBoostClassifier(n_estimators=i)
         ada_acc = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv)
         #ada_pre = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='precision')
         #ada_re = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv, scoring='recall')
         ada_f1 = cross_validation.cross_val_score(ada, x_data_tfidf.toarray(), target_arr, cv=cv,scoring='f1')
         n_str = "insert into ada_temp_result_if values(\'"+project+"\',"+(str)(i)+","+(str)(ada_acc.mean())+","+(str)(ada_f1.mean())+")"
         insert_cursor.execute(n_str)
         db1.commit()         
         
"""     
#svc_score = cross_validation.cross_val_score(svc, x_data_tfidf.toarray(), target_arr, cv=cv)     
#print "knn accuracy", knn_acc.mean()
# print "dt accuracy",  dt_score.mean()
# print "rf accuracy",  rf_score.mean()
# print "ada accuracy", ada_score.mean()
     
    
     
     
     