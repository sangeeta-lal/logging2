

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

import utill


project  = "tomcat_"
#project = "cloudstack_"

#=#

"""
port=3306
user="root"
password="1234"
database="logging_level2"
table_catch_feature =project+ "catch_training2"
"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level2"
table_catch_feature = project+"catch_training2"
#"""

random_seed_val_cross_validation = 0
random_seed_val_tuple_selection = 0
#rand_array  = [0,1,2,3,4,5,6,7,8,9]

db1= MySQLdb.connect(host="localhost", user=user, passwd=password,db=database, port=port)
select_cursor = db1.cursor()
insert_cursor  =db1.cursor()


#Read if blocks which are logged
str_logged = "select  catch_exc, package_name, class_name, method_name, try_loc, is_try_logged, try_log_count, try_log_levels, have_previous_catches, previous_catches_logged, \
                      is_return_in_try, is_return_in_catch, is_catch_object_ignore, is_interrupted_exception, is_thread_sleep_try,\
                       throw_throws_try,  throw_throws_catch, if_in_try, if_count_in_try, is_assert_in_try, is_assert_in_catch, \
                      is_method_have_param, method_param_type, method_param_name, method_param_count, method_call_names_try, \
                      method_call_count_try, operators_in_try, operators_count_in_try, variables_in_try, variables_count_try,\
                      method_call_names_till_try, method_call_count_till_try, operators_till_try, operators_count_till_try, variables_till_try,\
                      variables_count_till_try, loc_till_try, is_till_try_logged, till_try_log_count, till_try_log_levels,is_return_till_try, throw_throws_till_try, \
                     if_in_till_try, if_count_in_till_try,  is_assert_till_try  from "+ table_catch_feature +" where catch_exc!='' and  is_catch_logged= 1"
   



print "str_logged = ", str_logged
select_cursor.execute(str_logged)
logged_data = select_cursor.fetchall()

target = list()

logged_catch_block_count = 0
logged_catch_block_count = len(logged_data)
print  " size = ", logged_catch_block_count

logged_catch_n_features = list()
logged_catch_t_features = list()
#logged_complete_catch_features = list()


for d in logged_data:
    temp = list()
       
    t_catch_exc     = d[0]
    t_package_name  = d[1]
    t_class_name    = d[2]
    t_method_name   = d[3]
 
    n_try_loc       = d[4]
    n_is_try_logged = d[5]
    n_try_log_count  =d[6]
    
    t_try_log_levels =  d[7]
    
    n_have_previous_catches   =d[8]
    n_previous_catches_logged =d[9]
    n_is_return_in_try        =d[10]                     
    n_is_return_in_catch       =d[11]
    n_is_catch_object_ignore   =d[12]
    n_is_interrupted_exception  =d[13]
    n_is_thread_sleep_try      =d[14]
    n_throw_throws_try          =d[15]                             
    n_throw_throws_catch     =d[16]
    n_if_in_try           =d[17]
    n_if_count_in_try     =d[18]
    n_is_assert_in_try    =d[19]
    n_is_assert_in_catch  =d[20]
    n_is_method_have_param =d[21]
    
    t_method_param_type =d[22]
    t_method_param_name =d[23]
   
    n_method_param_count =d[24]
   
    t_method_call_names_try =d[25]
    
    n_method_call_count_try=d[26]
   
    t_operators_in_try =d[27]
   
    n_operators_count_in_try =d[28]
    
    t_variables_in_try =d[29]
    
    n_variables_count_try =d[30]
    
    t_method_call_names_till_try =d[31]
    
    n_method_call_count_till_try =d[32]
    
    t_operators_till_try  =d[33]
    
    n_operators_count_till_try =d[34]
    
    t_variables_till_try =d[35]
    
    n_variables_count_till_try =d[36] 
    n_loc_till_try =d[37]
    n_is_till_try_logged =d[38] 
    n_till_try_log_count =d[39]
    
    t_till_try_log_levels =d[40]
    
    n_is_return_till_try =d[41]
    n_throw_throws_till_try =d[42]
    n_if_in_till_try =d[43]
    n_if_count_in_till_try =d[44] 
    n_is_assert_till_try =d[45]
    
    
    temp.append( n_try_loc)
    temp.append(n_is_try_logged )
    temp.append( n_try_log_count)  
    temp.append( n_have_previous_catches)
    temp.append(n_previous_catches_logged)
    temp.append( n_is_return_in_try)
                            
    temp.append( n_is_return_in_catch )
    temp.append(n_is_catch_object_ignore)
    temp.append(n_is_interrupted_exception)
    temp.append(n_is_thread_sleep_try) 
    temp.append(n_throw_throws_try )
                             
    temp.append(n_throw_throws_catch)
    temp.append(n_if_in_try )
    temp.append( n_if_count_in_try) 
    temp.append(n_is_assert_in_try) 
    temp.append(n_is_assert_in_catch)
    temp.append( n_is_method_have_param )
    
    #t_method_param_type =temp[22]
    #t_method_param_name =temp[23]
   
    temp.append(n_method_param_count )
   
    #t_method_call_names_try =temp[25]
    
    temp.append(n_method_call_count_try)
   
   # t_operators_in_try =temp[27]

   
    temp.append(n_operators_count_in_try )
    
   # t_variables_in_try =temp[29]
    
    temp.append(n_variables_count_try )
    
    #t_method_call_names_till_try =temp[31]
    
    temp.append(n_method_call_count_till_try)
    
    #t_operators_till_try  =temp[33]
    
    temp.append(n_operators_count_till_try )
    
    #t_variables_till_try =temp[35]
    
    temp.append(n_variables_count_till_try )
    temp.append(n_loc_till_try )
    temp.append(n_is_till_try_logged )
    temp.append(n_till_try_log_count )
    
    #t_till_try_log_levels =temp[40]
    
    temp.append(n_is_return_till_try)
    temp.append(n_throw_throws_till_try)
    temp.append(n_if_in_till_try)
    temp.append(n_if_count_in_till_try) 
    temp.append(n_is_assert_till_try )
     
    
    text_features =      t_catch_exc+ " "+            t_package_name +" "                  + t_class_name+" "        + t_method_name  +" "+\
                         t_method_param_type + " " +  t_method_param_name +" " +            t_method_call_names_try +" " +\
                         t_variables_in_try  +" " +   t_try_log_levels +" "+                  t_method_call_names_till_try +" "+   t_variables_till_try +"  "+\
                         t_till_try_log_levels
    
    #Applying camel casing
    text_features = utill.camel_case_convert(text_features)
    text_features = utill.stem_it(text_features)
    
    operator_string =  t_operators_in_try +" "+ t_operators_till_try
    
    text_features =  text_features +" " + operator_string
    
    text_features =  text_features.strip()
 
    
      
    #Call a cleaning function
    
    logged_catch_n_features.append(temp)     
    logged_catch_t_features.append(text_features)
    target.append(1)                  


#Read if blocks which are logged
str_non_logged = "select  catch_exc, package_name, class_name, method_name, try_loc, is_try_logged, try_log_count, try_log_levels, have_previous_catches, previous_catches_logged, \
                      is_return_in_try, is_return_in_catch, is_catch_object_ignore, is_interrupted_exception, is_thread_sleep_try,\
                       throw_throws_try,  throw_throws_catch, if_in_try, if_count_in_try, is_assert_in_try, is_assert_in_catch, \
                      is_method_have_param, method_param_type, method_param_name, method_param_count, method_call_names_try, \
                      method_call_count_try, operators_in_try, operators_count_in_try, variables_in_try, variables_count_try,\
                      method_call_names_till_try, method_call_count_till_try, operators_till_try, operators_count_till_try, variables_till_try,\
                      variables_count_till_try, loc_till_try, is_till_try_logged, till_try_log_count, till_try_log_levels,is_return_till_try, throw_throws_till_try, \
                     if_in_till_try, if_count_in_till_try,  is_assert_till_try  from "+ table_catch_feature +" where catch_exc!='' and  is_catch_logged= 0 "#limit 0,"+ (str)(logged_catch_block_count)
   

print "str_non_logged = ", str_non_logged
select_cursor.execute(str_non_logged)
non_logged_data = select_cursor.fetchall()


non_logged_catch_n_features = list()
non_logged_catch_t_features = list()
#non_logged_complete_catch_feature = list()



np.random.seed(random_seed_val_tuple_selection)
indices = np.random.permutation(len(non_logged_data))[:len(logged_catch_n_features)]

print "len not logged tuples=", len(non_logged_data), " indices len=", len(indices)

valid_index=-1



for d in non_logged_data:
   
    valid_index= valid_index+1
    #print "I am here"
    if valid_index in indices:   
        temp = list()
    
        t_catch_exc     = d[0]
        t_package_name  = d[1]
        t_class_name    = d[2]
        t_method_name   = d[3]
 
        n_try_loc       = d[4]
        n_is_try_logged = d[5]
        n_try_log_count  =d[6]
    
        t_try_log_levels =  d[7]
    
        n_have_previous_catches=d[8]
        n_previous_catches_logged =d[9]
        n_is_return_in_try =d[10]                     
        n_is_return_in_catch  =d[11]
        n_is_catch_object_ignore =d[12]
        n_is_interrupted_exception =d[13]
        n_is_thread_sleep_try =d[14]
        n_throw_throws_try =d[15]                             
        n_throw_throws_catch=d[16]
        n_if_in_try =d[17]
        n_if_count_in_try =d[18]
        n_is_assert_in_try =d[19]
        n_is_assert_in_catch =d[20]
        n_is_method_have_param =d[21]
    
        t_method_param_type =d[22]
        t_method_param_name =d[23]
   
        n_method_param_count =d[24]
   
        t_method_call_names_try =d[25]
    
        n_method_call_count_try=d[26]
   
        t_operators_in_try =d[27]
   
        n_operators_count_in_try =d[28]
    
        t_variables_in_try =d[29]
    
        n_variables_count_try =d[30]
    
        t_method_call_names_till_try =d[31]
    
        n_method_call_count_till_try =d[32]
    
        t_operators_till_try  =d[33]
    
        n_operators_count_till_try =d[34]
    
        t_variables_till_try =d[35]
    
        n_variables_count_till_try =d[36] 
        n_loc_till_try =d[37]
        n_is_till_try_logged =d[38] 
        n_till_try_log_count =d[39]
    
        t_till_try_log_levels =d[40]
    
        n_is_return_till_try =d[41]
        n_throw_throws_till_try =d[42]
        n_if_in_till_try =d[43]
        n_if_count_in_till_try =d[44] 
        n_is_assert_till_try =d[45]
    
    
        temp.append( n_try_loc)
        temp.append(n_is_try_logged )
        temp.append( n_try_log_count)  
        temp.append( n_have_previous_catches)
        temp.append(n_previous_catches_logged)
        temp.append( n_is_return_in_try)
                            
        temp.append( n_is_return_in_catch )
        temp.append(n_is_catch_object_ignore)
        temp.append(n_is_interrupted_exception)
        temp.append(n_is_thread_sleep_try) 
        temp.append(n_throw_throws_try )
                             
        temp.append(n_throw_throws_catch)
        temp.append(n_if_in_try )
        temp.append( n_if_count_in_try) 
        temp.append(n_is_assert_in_try) 
        temp.append(n_is_assert_in_catch)
        temp.append( n_is_method_have_param )
    
        #t_method_param_type =temp[22]
        #t_method_param_name =temp[23]
   
        temp.append(n_method_param_count )
   
        #t_method_call_names_try =temp[25]
    
        temp.append(n_method_call_count_try)
   
        # t_operators_in_try =temp[27]

   
        temp.append(n_operators_count_in_try )
    
        # t_variables_in_try =temp[29]
    
        temp.append(n_variables_count_try )
    
        #t_method_call_names_till_try =temp[31]
    
        temp.append(n_method_call_count_till_try)
    
        #t_operators_till_try  =temp[33]
    
        temp.append(n_operators_count_till_try )
    
        #t_variables_till_try =temp[35]
    
        temp.append(n_variables_count_till_try )
        temp.append(n_loc_till_try )
        temp.append(n_is_till_try_logged )
        temp.append(n_till_try_log_count )
    
        #t_till_try_log_levels =temp[40]
    
        temp.append(n_is_return_till_try)
        temp.append(n_throw_throws_till_try)
        temp.append(n_if_in_till_try)
        temp.append(n_if_count_in_till_try) 
        temp.append(n_is_assert_till_try )
     
    
        text_features =      t_catch_exc+ " "+            t_package_name +" "                  + t_class_name+" "        + t_method_name  +" "+\
                         t_method_param_type + " " +  t_method_param_name +" " +            t_method_call_names_try +" " +\
                         t_variables_in_try  +" " +   t_try_log_levels +" "+                  t_method_call_names_till_try +" "+   t_variables_till_try +"  "+\
                         t_till_try_log_levels
    
        #Applying camel casing
        text_features = utill.camel_case_convert(text_features)
        text_features = utill.stem_it(text_features)
    
        operator_string =  t_operators_in_try +" "+ t_operators_till_try
    
        text_features =  text_features +" " + operator_string
    
        text_features =  text_features.strip()
 
    
      
        #Call a cleaning function
    
        non_logged_catch_n_features.append(temp)     
        non_logged_catch_t_features.append(text_features)
        target.append(0)                  
                      


#=======================================
vectorizer = TfidfVectorizer(min_df=1)
total_catch_t_features =  logged_catch_t_features + non_logged_catch_t_features
x_total_catch_t_features=vectorizer.fit_transform(total_catch_t_features)
print "shape of the feature", x_total_catch_t_features.shape

total_catch_n_features =  logged_catch_n_features  +  non_logged_catch_n_features
x_total_catch_n_features_array = np.asarray(total_catch_n_features)
print x_total_catch_n_features_array.shape

total_data = np.hstack([x_total_catch_t_features.toarray(), x_total_catch_n_features_array])
print total_data
#=======================================
 
#========================================================= 
#total_data = logged_catch_data   + non_logged_catch_data
#=========================================================

cv = cross_validation.ShuffleSplit(len(target), n_iter=10, test_size=0.30, 
                                   random_state=random_seed_val_cross_validation)

#"""
#====1.  KNN algorithm====================#
for temp_leaf_size in range(100):
    for temp_nbr  in range(20):
        print "Knn temp leaf size = ", temp_leaf_size+1, " Nbr =",temp_nbr+1

        knn = KNeighborsClassifier(algorithm='auto', leaf_size=temp_leaf_size+1, metric='minkowski',
                               n_neighbors=temp_nbr+1, p=2, weights='uniform')
        #knn_score = cross_validation.cross_val_score(knn,np.asarray(total_data), np.asarray(target), cv=cv)
        #print "knn = ", knn_score.mean()

        knn_score = 0.0 #cross_validation.cross_val_score(knn,np.asarray(total_data), 
                                            #np.asarray(target), cv=cv)
        knn_acc= 0.0 #= cross_validation.cross_val_score(knn,np.asarray(total_data), 
         #np.asarray(target), cv=cv, score_func=metrics.accuracy_score)
        knn_precision = 0.0 #cross_validation.cross_val_score(knn,np.asarray(total_data), 
            #  np.asarray(target), cv=cv,score_func=metrics.precision_score)
        knn_recall =0.0 # cross_validation.cross_val_score(knn,np.asarray(total_data), 
           # np.asarray(target), cv=cv,score_func=metrics.recall_score)
        knn_f1= cross_validation.cross_val_score(knn,np.asarray(total_data), 
            np.asarray(target), cv=cv,score_func=metrics.f1_score)
        knn_roc = 0.0# cross_validation.cross_val_score(knn,np.asarray(total_data),
        # np.asarray(target), cv=cv, score_func=metrics.roc_auc_score)
        
        #print "knn =", knn_score.mean()
        #print "knn accuracy=", knn_acc.mean()
        #print "knn precision=", knn_precision.mean()
        #print "knn recall=", knn_recall.mean()
        print "knn f1=", knn_f1.mean()
        #print "knn roc=", knn_roc.mean()
       
        insert_knn_str  =  "insert into knn_catch_training2_results values( \"knn\",  '"+project+"',"+ (str)(temp_leaf_size+1)+"," + (str)(temp_nbr+1)+ ", "+ (str)(knn_acc) + ", "+ (str)(knn_precision)+ \
        "," + (str)(knn_recall) +","+ (str)(knn_f1.mean()) +","+ (str)(knn_roc)+")"
        print "insert str = ",insert_knn_str
        insert_cursor.execute(insert_knn_str)
        db1.commit()

 #"""
 
 #"""       

#==== Decition Trees Classifieer= ======#        
for temp_max_depth in range(100):
        print " temp max depth =", temp_max_depth
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

        insert_dt_str =  "insert into dt_catch_training2_results values( \"dt\",  '"+ project+"',"+ (str)(temp_max_depth+1)+","+ (str)(dt_acc.mean()) + ", "+ (str)(dt_precision.mean())+ \
        "," + (str)(dt_recall.mean()) +","+ (str)(dt_f1.mean()) +","+ (str)(dt_roc.mean())+")"
        print "insert str = ",insert_dt_str
        insert_cursor.execute(insert_dt_str)
        db1.commit()

 #"""
 
 #"""    

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


insert_gnb_str =  "insert into gnb_catch_training2_results values( \"gnb\",  '"+project+"',"+  (str)(gnb_acc.mean()) +","+ (str)(gnb_precision.mean())+ \
        "," + (str)(gnb_recall.mean()) +","+ (str)(gnb_f1.mean()) +","+ (str)(gnb_roc.mean())+")"
print "insert str = ",insert_gnb_str
insert_cursor.execute(insert_gnb_str)
db1.commit()

 #"""
 
 #"""    

#===================Adaboost=================================#
for temp_estimators in range(100):
    print " temp estimators =" , temp_estimators+1
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
    
    insert_ada_str =   "insert into ada_catch_training2_results values( \"adaboost\",  '"+project+"',"+ (str)(temp_estimators+1)+","+ (str)(ada_acc.mean()) + ", "+ (str)(ada_precision.mean())+ \
        "," + (str)(ada_recall.mean()) +","+ (str)(ada_f1.mean()) +","+ (str)(ada_roc.mean())+")"
    print "insert str = ",insert_ada_str
    insert_cursor.execute(insert_ada_str)
    db1.commit()


 #"""
 
 #"""    
#========================Random Forest===================================#

#rf =  RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),

for temp_estimators in range (100):
    print  " temp estimators = ", temp_estimators+1
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
   
   
    insert_rf_str =   "insert into rf_catch_training2_results values( \"rf\", '"+project+ "'," +(str)(temp_estimators+1)+","+(str)(rf_acc.mean()) + ", "+ (str)(rf_precision.mean())+ \
        "," + (str)(rf_recall.mean()) +","+ (str)(rf_f1.mean()) +","+ (str)(rf_roc.mean())+")"
    print "insert str = ",insert_rf_str
    insert_cursor.execute(insert_rf_str)
    db1.commit()

 #"""
 
