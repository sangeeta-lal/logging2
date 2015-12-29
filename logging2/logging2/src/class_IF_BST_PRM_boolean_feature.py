


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

import utill


"""=================================================================================================
@Uses: This file will be used to create classifier using boolean features 
1. This file will use best parameters used in the classifier
2. This file will report the average value of classifier 10 runs
======================================================================================="""

#==Parameters========#
#"""
project  = "tomcat_"
knn_leaf_size  = 62
knn_nbr  =3
dt_depth  =86
ada_estimators  =99
rf_estimators  =82

"""
#project = "cloudstack_"
knn_leaf_size  = 62
knn_nbr  =3
dt_depth  =86
ada_estimators  =99
rf_estimators  =82
#"""

#"""
port=3306
user="root"
password="1234"
database="logging_level2"
table_if_feature =project+ "if_training2"
final_result_table = "final_result_table_if_training2_boolean_features"
"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level2"
table_if_feature = project+"if_training2"
final_result_table = "final_result_table_if_training2_boolean_features"
#"""

random_seed_val_cross_validation = 0
random_seed_val_tuple_selection = 0
#rand_array  = [0,1,2,3,4,5,6,7,8,9]

db1= MySQLdb.connect(host="localhost", user=user, passwd=password,db=database, port=port)
select_cursor = db1.cursor()
insert_cursor  =db1.cursor()


#Read if blocks which are logged
str_logged = "select  if_expr, loc_till_if, is_till_if_logged, till_if_log_count, till_if_log_levels, operators_till_if, operators_count_till_if, variables_till_if,  \
                       variables_count_till_if,method_call_names_till_if, method_call_count_till_if,  is_return_in_till_if, throw_throws_till_if, \
                       if_in_till_if, if_count_in_till_if, is_assert_till_if, is_method_have_param,  method_param_type, method_param_name, method_param_count,\
                       is_return_in_if, throw_throws_if, is_assert_if, is_null_condition_if, is_instance_of_condition_if, package_name, class_name, method_name\
                       from "+ table_if_feature +" where if_expr not like '%isTraceEnabled()' and \
                       if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
                       and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()' and if_expr!='' and  is_if_logged= 1"
   


print "str_logged = ", str_logged
select_cursor.execute(str_logged)
logged_data = select_cursor.fetchall()

target = list()

logged_if_block_count = 0
logged_if_block_count = len(logged_data)
print  " size = ", logged_if_block_count

logged_if_n_features = list()
logged_if_t_features = list()
#logged_complete_if_features = list()


for d in logged_data:
    temp = list()
       
    
    n_is_till_if_logged   = d[2]
    n_is_return_in_till_if        =d[11]
    n_throw_throws_till_if        =d[12]
    n_if_in_till_if               =d[13]   
    n_is_assert_till_if          =d[15]
    n_is_method_have_param        =d[16]      
    n_is_return_in_if           = d[20]
    n_throw_throws_if          = d[21]
    n_is_assert_if              =d[22]
    n_is_null_condition_if          = d[23] 
    n_is_instance_of_condition_if = d[24] 
                              
    temp.append(n_is_till_if_logged )        
    temp.append(n_is_return_in_till_if )
    temp.append(n_throw_throws_till_if )
    temp.append(n_if_in_till_if )
    temp.append(n_is_assert_till_if )
    temp.append(n_is_method_have_param )    
    temp.append(n_is_return_in_if)         
    temp.append(n_throw_throws_if)         
    temp.append(n_is_assert_if )           
    temp.append(n_is_null_condition_if )          
    temp.append(n_is_instance_of_condition_if) 
               
    logged_if_n_features.append(temp)     
    target.append(1)                  

#====Inserting for negative class======#
for i  in range(len(logged_if_n_features)):
    target.append(0)

total_knn_acc = 0.0
total_knn_precision = 0.0
total_knn_recall = 0.0
total_knn_f1 = 0.0
total_knn_roc = 0.0

total_dt_acc = 0.0
total_dt_precision = 0.0
total_dt_recall = 0.0
total_dt_f1 = 0.0
total_dt_roc = 0.0

total_gnb_acc = 0.0
total_gnb_precision = 0.0
total_gnb_recall = 0.0
total_gnb_f1 = 0.0
total_gnb_roc = 0.0

total_ada_acc = 0.0
total_ada_precision = 0.0
total_ada_recall = 0.0
total_ada_f1 = 0.0
total_ada_roc = 0.0

total_rf_acc = 0.0
total_rf_precision = 0.0
total_rf_recall = 0.0
total_rf_f1 = 0.0
total_rf_roc = 0.0


#Read if blocks which are non logged
str_non_logged = "select  if_expr, loc_till_if, is_till_if_logged, till_if_log_count, till_if_log_levels, operators_till_if, operators_count_till_if, variables_till_if,  \
                       variables_count_till_if,method_call_names_till_if, method_call_count_till_if,  is_return_in_till_if, throw_throws_till_if, \
                       if_in_till_if, if_count_in_till_if, is_assert_till_if, is_method_have_param,  method_param_type, method_param_name, method_param_count,\
                       is_return_in_if, throw_throws_if, is_assert_if, is_null_condition_if, is_instance_of_condition_if, package_name, class_name, method_name\
                       from "+ table_if_feature +" where if_expr not like '%isTraceEnabled()'  and \
                       if_expr not like '%isDebugEnabled()'  and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'  \
                       and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and if_expr!='' and  is_if_logged= 0"
   
   
   


print "str_non_logged = ", str_non_logged
select_cursor.execute(str_non_logged)
non_logged_data = select_cursor.fetchall()



rand_array = [0,1,2,3,4,5,6,7,8,9]
for  random_seed_val_cross_validation in rand_array:
    
    np.random.seed(random_seed_val_tuple_selection)
    indices = list()
    indices = np.random.permutation(len(non_logged_data))[:len(logged_if_n_features)]

    print "len not logged tuples=", len(non_logged_data), " indices len=", len(indices),  "  logged if n features=", len(logged_if_n_features)

    non_logged_if_n_features = list()
    #non_logged_if_t_features = list()

    valid_index=-1

    for d in non_logged_data:
   
        valid_index= valid_index+1
        #print "I am here"
        if valid_index in indices:   
            temp = list()
    
            n_is_till_if_logged   = d[2]
            n_is_return_in_till_if        =d[11]
            n_throw_throws_till_if        =d[12]
            n_if_in_till_if               =d[13]   
            n_is_assert_till_if          =d[15]
            n_is_method_have_param        =d[16]      
            n_is_return_in_if           = d[20]
            n_throw_throws_if          = d[21]
            n_is_assert_if              =d[22]
            n_is_null_condition_if          = d[23] 
            n_is_instance_of_condition_if = d[24] 
                              
            temp.append(n_is_till_if_logged )        
            temp.append(n_is_return_in_till_if )
            temp.append(n_throw_throws_till_if )
            temp.append(n_if_in_till_if )
            temp.append(n_is_assert_till_if )
            temp.append(n_is_method_have_param )    
            temp.append(n_is_return_in_if)         
            temp.append(n_throw_throws_if)         
            temp.append(n_is_assert_if )           
            temp.append(n_is_null_condition_if )          
            temp.append(n_is_instance_of_condition_if) 
               
    
            non_logged_if_n_features.append(temp)     
            
    #=======================================
    vectorizer = TfidfVectorizer(min_df=1)    
    total_data =  logged_if_n_features  +  non_logged_if_n_features
    
    #=======================================
 
    #========================================================= 
    #total_data = logged_if_data   + non_logged_if_data
    #=========================================================

    cv = cross_validation.ShuffleSplit(len(target), n_iter=10, test_size=0.30, 
                                   random_state=random_seed_val_cross_validation)


    temp_leaf_size = knn_leaf_size
    temp_nbr = knn_nbr
    knn = KNeighborsClassifier(algorithm='auto', leaf_size=temp_leaf_size+1, metric='minkowski',
                               n_neighbors=temp_nbr+1, p=2, weights='uniform')
  
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
   
   
    total_knn_acc =        total_knn_acc          + knn_acc.mean()
    total_knn_precision =  total_knn_precision    + knn_precision.mean()
    total_knn_recall =     total_knn_recall       + knn_recall.mean()
    total_knn_f1 =         total_knn_f1           + knn_f1.mean()
    total_knn_roc =        total_knn_roc          + knn_roc.mean()
  
       
#==== Decition Trees Classifieer= ======#        

    temp_max_depth  = dt_depth   
    dt  =DecisionTreeClassifier(max_depth= temp_max_depth+1)
        
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
    
    total_dt_acc =        total_dt_acc          + dt_acc.mean()
    total_dt_precision =  total_dt_precision    + dt_precision.mean()
    total_dt_recall =     total_dt_recall       + dt_recall.mean()
    total_dt_f1 =         total_dt_f1           + dt_f1.mean()
    total_dt_roc =        total_dt_roc          + dt_roc.mean()


#========= GnB===================================================#        
    gnb = GaussianNB() # Guasian Niave Bayes
    
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
    
    total_gnb_acc =        total_gnb_acc          + gnb_acc.mean()
    total_gnb_precision =  total_gnb_precision    + gnb_precision.mean()
    total_gnb_recall =     total_gnb_recall       + gnb_recall.mean()
    total_gnb_f1 =         total_gnb_f1           + gnb_f1.mean()
    total_gnb_roc =        total_gnb_roc          + gnb_roc.mean()



    #===================Adaboost=================================#
    temp_estimators  =  ada_estimators
  
    ada =    AdaBoostClassifier(n_estimators=temp_estimators+1)
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
    
    print "ada =",          ada_score.mean()
    print "ada accuracy=",  ada_acc.mean()
    print "ada precision=", ada_precision.mean()
    print "ada recall=",    ada_recall.mean()
    print "ada f1=",        ada_f1.mean()
    print "ada roc=",       ada_roc.mean()
    
    total_ada_acc =        total_ada_acc          + ada_acc.mean()
    total_ada_precision =  total_ada_precision    + ada_precision.mean()
    total_ada_recall =     total_ada_recall       + ada_recall.mean()
    total_ada_f1 =         total_ada_f1           + ada_f1.mean()
    total_ada_roc =        total_ada_roc          + ada_roc.mean()


  
#========================Random Forest===================================#

    temp_estimators  = rf_estimators
   
    rf  =  RandomForestClassifier(n_estimators=temp_estimators+1)
    
    rf_score = cross_validation.cross_val_score(rf,np.asarray(total_data), 
                                            np.asarray(target), cv=cv)
    rf_acc = cross_validation.cross_val_score(rf,np.asarray(total_data), 
         np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
    rf_precision = cross_validation.cross_val_score(rf,np.asarray(total_data), 
              np.asarray(target), cv=cv,score_func=metrics.precision_score)
    rf_recall = cross_validation.cross_val_score(rf,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.recall_score)
    rf_f1= cross_validation.cross_val_score(rf,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
    rf_roc = cross_validation.cross_val_score(rf,np.asarray(total_data),
         np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
   
    total_rf_acc =        total_rf_acc          + rf_acc.mean()
    total_rf_precision =  total_rf_precision    + rf_precision.mean()
    total_rf_recall =     total_rf_recall       + rf_recall.mean()
    total_rf_f1 =         total_rf_f1           + rf_f1.mean()
    total_rf_roc =        total_rf_roc          + rf_roc.mean()


total_knn_acc =        (total_knn_acc*100)/10       
total_knn_precision =  (total_knn_precision*100)/10    
total_knn_recall =     (total_knn_recall*100)/10       
total_knn_f1 =         (total_knn_f1 *100)/10          
total_knn_roc =        (total_knn_roc*100)/10

total_dt_acc =        (total_dt_acc*100)/10       
total_dt_precision =  (total_dt_precision*100)/10    
total_dt_recall =     (total_dt_recall*100)/10       
total_dt_f1 =         (total_dt_f1 *100)/10          
total_dt_roc =        (total_dt_roc*100)/10

total_gnb_acc =        (total_gnb_acc*100)/10       
total_gnb_precision =  (total_gnb_precision*100)/10    
total_gnb_recall =     (total_gnb_recall*100)/10       
total_gnb_f1 =         (total_gnb_f1 *100)/10          
total_gnb_roc =       (total_gnb_roc*100)/10

total_ada_acc =        (total_ada_acc*100)/10       
total_ada_precision =  (total_ada_precision*100)/10    
total_ada_recall =     (total_ada_recall*100)/10       
total_ada_f1 =         (total_ada_f1 *100)/10          
total_ada_roc =        (total_ada_roc*100)/10

total_rf_acc =        (total_rf_acc*100)/10       
total_rf_precision =  (total_rf_precision*100)/10    
total_rf_recall =     (total_rf_recall*100)/10       
total_rf_f1 =         (total_rf_f1 *100)/10          
total_rf_roc =        (total_rf_roc*100)/10


param ="knn leaf size ="+(str)(knn_leaf_size)+"  knn nbr="+(str)(knn_nbr)
insert_knn_str =   "insert into  " +final_result_table+" values( \"knn\", '"+project+ "','" +param+"',"+(str)(total_knn_acc.mean()) + ", "+ (str)(total_knn_precision.mean())+ \
        "," + (str)(total_knn_recall.mean()) +","+ (str)(total_knn_f1.mean()) +","+ (str)(total_knn_roc.mean())+")"
print "insert str = ",insert_knn_str
insert_cursor.execute(insert_knn_str)

param ="dt depth ="+(str)(dt_depth)
insert_dt_str =   "insert into  " +final_result_table+" values( \"dt\", '"+project+ "','" +param+"',"+(str)(total_dt_acc.mean()) + ", "+ (str)(total_dt_precision.mean())+ \
        "," + (str)(total_dt_recall.mean()) +","+ (str)(total_dt_f1.mean()) +","+ (str)(total_dt_roc.mean())+")"
print "insert str = ",insert_dt_str
insert_cursor.execute(insert_dt_str)

param ="ada esti ="+(str)(ada_estimators)
insert_ada_str =   "insert into  " +final_result_table+" values( \"ada\", '"+project+ "','" +param+"',"+(str)(total_ada_acc.mean()) + ", "+ (str)(total_ada_precision.mean())+ \
        "," + (str)(total_ada_recall.mean()) +","+ (str)(total_ada_f1.mean()) +","+ (str)(total_ada_roc.mean())+")"
print "insert str = ",insert_ada_str
insert_cursor.execute(insert_ada_str)

param ="rf esti ="+(str)(rf_estimators)
insert_rf_str =   "insert into  " +final_result_table+" values( \"rf\", '"+project+ "','" +param+"',"+(str)(total_rf_acc.mean()) + ", "+ (str)(total_rf_precision.mean())+ \
        "," + (str)(total_rf_recall.mean()) +","+ (str)(total_rf_f1.mean()) +","+ (str)(total_rf_roc.mean())+")"
print "insert str = ",insert_rf_str
insert_cursor.execute(insert_rf_str)

param =" gnb esti "
insert_gnb_str =   "insert into  " +final_result_table+" values( \"gnb\", '"+project+ "','" +param+"',"+(str)(total_gnb_acc.mean()) + ", "+ (str)(total_gnb_precision.mean())+ \
        "," + (str)(total_gnb_recall.mean()) +","+ (str)(total_gnb_f1.mean()) +","+ (str)(total_gnb_roc.mean())+")"
print "insert str = ",insert_gnb_str
insert_cursor.execute(insert_gnb_str)

db1.commit()





"""        
"""

"""        
total_ada_acc = total_ada_acc +ada_acc.mean()
total_ada_precision = total_ada_precision +ada_precision.mean()
total_ada_recall = total_ada_recall +ada_recall.mean()
total_ada_f1 = total_ada_f1 + ada_f1.mean()
total_ada_roc = total_ada_roc +ada_roc.mean()
"""

"""
total_knn_acc = total_knn_acc +knn_acc.mean()
total_knn_precision = total_knn_precision +knn_precision.mean()
total_knn_recall = total_knn_recall +knn_recall.mean()
total_knn_f1 = total_knn_f1 + knn_f1.mean()
total_knn_roc = total_knn_roc +knn_roc.mean()
""" 
   
"""
total_gnb_acc = total_gnb_acc +gnb_acc.mean()
total_gnb_precision = total_gnb_precision +gnb_precision.mean()
total_gnb_recall = total_gnb_recall +gnb_recall.mean()
total_gnb_f1 = total_gnb_f1 + gnb_f1.mean()
total_gnb_roc = total_gnb_roc +gnb_roc.mean()
"""


