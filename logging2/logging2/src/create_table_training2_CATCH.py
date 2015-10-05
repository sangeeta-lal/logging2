

import MySQLdb
from pylab import *
import matplotlib.pyplot as plt
import csv

"""
@Author: Sangeeta
@Uses:  This file is used to create tables in the paper
@Data: It will use "training2  catch"  for creating the tables for APSEC-2015 paper
"""
project = "tomcat_"
#project="cloudstack_"

"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level2"
file_path = "E:\\Sangeeta\\Research\\logging\\result"
exception_ratio_file = file_path +"\\_"+project+"exception_ratio.csv"
"""
port=3306
user="root"
password="1234"
database="logging_level2"
file_path = "F:\\Research\\logging\\result"
exception_ratio_file = file_path +"\\"+project+"exception_ratio.csv"
#"""

"""
@Table
"""
catch_training_table =  project+"catch_training2"

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()


"""
@Results 1: 
Total Count of catches, logged  catches and non-logged catches
"""

total_catch_count=0
logged_catch_count = 0
non_logged_catch_count = 0

str1 = "select count(*) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
for d in data1:
    total_catch_count= d[0]
    
str2 = "select count(*) from "+ catch_training_table +" where is_catch_logged =1"    
select_cursor.execute(str2)
data2 = select_cursor.fetchall()
for d in data2:
    logged_catch_count= d[0]
    
str3 = "select count(*) from "+ catch_training_table +" where is_catch_logged =0"    
select_cursor.execute(str3)
data3 = select_cursor.fetchall()
for d in data3:
    non_logged_catch_count= d[0]   
    
print "Total catch=", total_catch_count, " logged catch count=", logged_catch_count, " Non logged Catch Count=", non_logged_catch_count     



"""
Result 2:  Avg LOC values of Try Block in Logged Catch Block and Non- Logged Catch Block
"""
str1 = "select AVG(try_loc) from "+ catch_training_table+ " where is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_loc_logged =  data1[0][0]

str1 = "select AVG(try_loc) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_loc_non_logged =  data1[0][0]

print "[STB]=", " Avg try Loc Logged=", avg_try_loc_logged, " Avg try Loc Non Logged=", avg_try_loc_non_logged


"""
Result 3:  Avg LOC values of "method till try" in Logged Catch Block and Non- Logged Catch Block
"""
str1 = "select AVG(loc_till_try) from "+ catch_training_table+ " where is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_loc_till_try_logged =  data1[0][0]

str1 = "select AVG(loc_till_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_loc_till_try_non_logged =  data1[0][0]

print "[SM]=", " Avg Loc of method_till_try Logged=", avg_loc_till_try_logged, " Avg Loc of method_till_try Non Logged=", avg_loc_till_try_non_logged


"""
Result 4:  Previous catches of given catch block
"""
str1  = "select count(*)  from "+ catch_training_table+  "  where have_previous_catches!=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
total_previous_catches =  data1[0][0]

str1 = "select count(*)  from "+ catch_training_table+ " where have_previous_catches!=0 and is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
previous_catches_logged =  data1[0][0]

str1 = "select  count(*)  from "+ catch_training_table+ " where have_previous_catches!=0  and is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
previous_catches_non_logged =  data1[0][0]

print "[PCC]=", "total =", total_previous_catches , " previous_catches_logged =", previous_catches_logged , " previous_catches_non_logged=", previous_catches_non_logged

"""
Result 5:  Previous catches are logged of given catch block
"""
str1  = "select count(*)  from "+ catch_training_table+  "  where previous_catches_logged !=0  "
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
total_logged_previous_catches =  data1[0][0]

str1 = "select count(*)  from "+ catch_training_table+ " where  previous_catches_logged !=0  and is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
logged_previous_catches_logged =  data1[0][0]

str1 = "select  count(*)  from "+ catch_training_table+ " where  previous_catches_logged !=0   and is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
logged_previous_catches_non_logged =  data1[0][0]

print "[LPCC]=", "total =", total_logged_previous_catches , " logged previous catches =", logged_previous_catches_logged , " logged previous non logged catches=", logged_previous_catches_non_logged


"""
Result 6:  Logged Try block
"""
str1  = "select count(*)  from "+ catch_training_table+  "  where is_try_logged=1  "
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
total_logged_try =  data1[0][0]

str1 = "select count(*)  from "+ catch_training_table+ " where  is_try_logged=1  and is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
logged_try_catches_logged =  data1[0][0]

str1 = "select  count(*)  from "+ catch_training_table+ " where is_try_logged=1 and is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
logged_try_catches_non_logged =  data1[0][0]

print "[LTB]=", "total =", total_logged_try , " logged try block =", logged_try_catches_logged , " logged try block in non logged catch blocks=", logged_try_catches_non_logged




"""
Result 7:  Logged Method Till Try
"""
str1  = "select count(*)  from "+ catch_training_table+  "  where is_till_try_logged=1  "
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
total_logged_method_BT =  data1[0][0]

str1 = "select count(*)  from "+ catch_training_table+ " where  is_till_try_logged=1  and is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
logged_method_BT_catches_logged =  data1[0][0]

str1 = "select  count(*)  from "+ catch_training_table+ " where is_till_try_logged=1 and is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
logged_method_BT_catches_non_logged =  data1[0][0]

print "[LM]=", "total =", total_logged_method_BT , " logged method_BT logged catch =", logged_method_BT_catches_logged , " logged method_BT in non logged catch blocks=", logged_method_BT_catches_non_logged



"""
Result 8:  Logged Count Try Block
"""
str1  = "select avg( try_log_count) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_log_count =  data1[0][0]

str1 = "select avg( try_log_count)  from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_log_count_catches_logged =  data1[0][0]

str1 = "select  avg( try_log_count) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_log_count_catches_non_logged =  data1[0][0]

print "[LCTB]=", "total =", avg_try_log_count , " avg_try log count =", avg_try_log_count_catches_logged , " avg try log coint non logged=", avg_try_log_count_catches_non_logged



"""
Result 9:  Logged Count Method_BT
"""
str1  = "select avg(till_try_log_count) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_log_count =  data1[0][0]

str1 = "select  avg(till_try_log_count) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_log_count_catches_logged =  data1[0][0]

str1 = "select   avg(till_try_log_count) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_log_count_catches_non_logged =  data1[0][0]

print "[LCM]=", "total =", avg_till_try_log_count , " avg_till try log count =", avg_till_try_log_count_catches_logged , " avg till try log coint non logged=", avg_till_try_log_count_catches_non_logged


"""
Result 10: Operator Count Try Block
"""
str1  = "select avg(operators_count_in_try) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_operator_count =  data1[0][0]

str1 = "select avg(operators_count_in_try) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_operator_count_catches_logged =  data1[0][0]

str1 = "select  avg(operators_count_in_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_operator_count_catches_non_logged =  data1[0][0]

print "[COTB]=", "total =", avg_operator_count , " avg operator count catches logged =", avg_operator_count_catches_logged , " avg operator count catches non logged=", avg_operator_count_catches_non_logged


"""
Result 11: Operator Count Method_BT
"""
str1  = "select avg(operators_count_till_try) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_operator_count =  data1[0][0]

str1 = "select avg(operators_count_till_try) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_operator_count_catches_logged =  data1[0][0]

str1 = "select  avg(operators_count_till_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_operator_count_catches_non_logged =  data1[0][0]

print "[COM]=", "total =", avg_till_try_operator_count , " avg till try operator count catches logged =", avg_till_try_operator_count_catches_logged , " avg till try operator count catches non logged=", avg_till_try_operator_count_catches_non_logged


"""
Result 12:  Variable Count Try Block
"""
str1  = "select avg(variables_count_try) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_variable_count =  data1[0][0]

str1 = "select avg(variables_count_try) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_variable_count_catches_logged =  data1[0][0]

str1 = "select  avg(variables_count_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_try_variable_count_catches_non_logged =  data1[0][0]

print "[VCTB]=", "total =", avg_try_variable_count , " avg variable count catches logged =", avg_try_variable_count_catches_logged , " avg variable count catches non logged=", avg_try_variable_count_catches_non_logged


"""
Result 13:  Variable Count in Method_BT
"""
str1  = "select avg(variables_count_till_try) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_variable_count =  data1[0][0]

str1 = "select avg(variables_count_till_try) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_variable_count_catches_logged =  data1[0][0]

str1 = "select  avg(variables_count_till_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_till_try_variable_count_catches_non_logged =  data1[0][0]

print "[VCM]=", "total =", avg_till_try_variable_count , " avg variable count catches logged =", avg_till_try_variable_count_catches_logged , " avg variable count catches non logged=", avg_till_try_variable_count_catches_non_logged


"""
Result 14:  Method Call Count Try Block
"""
str1  = "select avg(method_call_count_try) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_method_call_count =  data1[0][0]

str1 = "select avg(method_call_count_try) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_method_call_count_catches_logged =  data1[0][0]

str1 = "select  avg(method_call_count_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_method_call_count_catches_non_logged =  data1[0][0]

print "[MCTB]=", "total =", avg_method_call_count , " avg method count catches logged =", avg_method_call_count_catches_logged , " avg method call count catches non logged=", avg_method_call_count_catches_non_logged




"""
Result 15:  Method Call Count Method_BT
"""
str1  = "select avg(method_call_count_till_try) from "+ catch_training_table
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_method_call_till_try_count =  data1[0][0]

str1 = "select avg(method_call_count_till_try) from "+ catch_training_table+ " where  is_catch_logged=1"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_method_call_count_till_try_catches_logged =  data1[0][0]

str1 = "select  avg(method_call_count_till_try) from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str1)
data1 = select_cursor.fetchall()
avg_method_call_count_till_try_catches_non_logged =  data1[0][0]

print "[MCM]=", "total =", avg_method_call_till_try_count , " avg method count till try catches logged =", avg_method_call_count_till_try_catches_logged , " avg method call count till try catches non logged=\
              ", avg_method_call_count_till_try_catches_non_logged


"""
@Result16: % of Catch blocks with IF  Vs. logged and Non-logged catch
"""
total_if_in_try=0
if_in_try_logged_catch=0
if_in_try_non_logged_catch=0

str30 = "select count(*) from "+ catch_training_table +" where  if_in_try=1 "  
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_if_in_try= d[0]
    
str30 = "select count(*) from "+ catch_training_table +" where  if_in_try=1 and  is_catch_logged =1"  
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    if_in_try_logged_catch= d[0]
    
str31 = "select count(*) from "+ catch_training_table +" where  if_in_try=1  and is_catch_logged =0"    
select_cursor.execute(str31)
data31 = select_cursor.fetchall()   
for d in data31:
    if_in_try_non_logged_catch= d[0]   

print "[ITB]","Total if in Try Count = ", total_if_in_try, "Logged catch if count", if_in_try_logged_catch, " non logged=", if_in_try_non_logged_catch
print "ITB%=", (if_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_in_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result17: % of Method BT  with IF  Vs. logged and Non-logged catch
"""
total_if_in_till_try=0
if_in_till_try_logged_catch=0
if_in_till_try_non_logged_catch=0

str30 = "select count(*) from "+ catch_training_table +" where  if_in_till_try=1 "  
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_if_in_till_try= d[0]
    
str30 = "select count(*) from "+ catch_training_table +" where  if_in_till_try=1 and  is_catch_logged =1"  
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    if_in_till_try_logged_catch= d[0]
    
str31 = "select count(*) from "+ catch_training_table +" where  if_in_till_try=1  and is_catch_logged =0"    
select_cursor.execute(str31)
data31 = select_cursor.fetchall()   
for d in data31:
    if_in_till_try_non_logged_catch= d[0]   

print "[IM]","Total if in till Try Count = ", total_if_in_till_try, "Logged catch if count in method BT=", if_in_till_try_logged_catch, " If in method BT non logged=", if_in_till_try_non_logged_catch
print "ITB%=", (if_in_till_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_in_till_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result18: % IF count in Try  Vs. logged and Non-logged catch
"""
total_if_count_try=0
if_count_try_logged_catch=0
if_count_try_non_logged_catch=0

str30 = "select avg(if_count_in_try) from "+ catch_training_table 
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_if_count_try= d[0]
    
str30 = "select avg(if_count_in_try) from "+ catch_training_table +" where   is_catch_logged =1"  
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    if_count_in_try_logged_catch= d[0]
    
str31 = "select avg(if_count_in_try) from "+ catch_training_table +" where   is_catch_logged =0"    
#print str31
select_cursor.execute(str31)
data31 = select_cursor.fetchall()   
for d in data31:
    if_count_in_try_non_logged_catch= d[0]   

print "[ICTB]","Total AVG IF count Try = ", total_if_count_try, " avg IF  count in try logged catch=", if_count_in_try_logged_catch, "  avg If count in try non logged catch=", if_count_in_try_non_logged_catch
#print "ICTB%=", (if_count_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_count_in_try_non_logged_catch*100/non_logged_catch_count)   


"""
@Result18: % Avg IF count in Method_BT  Vs. logged and Non-logged catch
"""
total_if_count_till_try=0
if_count_till_try_logged_catch=0
if_count_till_try_non_logged_catch=0

str30 = "select avg(if_count_in_till_try) from "+ catch_training_table 
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_if_count_till_try= d[0]
    
str30 = "select avg(if_count_in_till_try) from "+ catch_training_table +" where   is_catch_logged =1"  
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    if_count_in_till_try_logged_catch= d[0]
    
str31 = "select avg(if_count_in_till_try) from "+ catch_training_table +" where  is_catch_logged =0"    
select_cursor.execute(str31)
data31 = select_cursor.fetchall()   
for d in data31:
    if_count_in_till_try_non_logged_catch= d[0]   

print "[ICM]", "Total AVG IF count Till Try = ", total_if_count_till_try, " avg IF count Till Try logged catch=", if_count_in_till_try_logged_catch, "  avg If count in Till Try non logged catch=", if_count_in_till_try_non_logged_catch
#print "ICTB%=", (if_count_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_count_in_try_non_logged_catch*100/non_logged_catch_count)   


"""
Result 19: % of catch have parameters in containing method have parameter
"""

total_catch_blocks_method_have_param_count=0
total_catch_blocks_method_have_param_logged_catch=0
total_catch_block_method_have_param_non_logged_catch=0

str30 = "select count(*) from "+ catch_training_table +" where is_method_have_param = 1"
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_catch_blocks_method_have_param_count= d[0]
    

str30 = "select count(*) from "+ catch_training_table +" where is_method_have_param = 1  and is_catch_logged=1"
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_catch_blocks_method_have_param_logged_catch= d[0]

str30 = "select count(*) from "+ catch_training_table +" where is_method_have_param = 1  and is_catch_logged=0"
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    total_catch_blocks_method_have_param_non_logged_catch= d[0]
   
print "[PM]=", "Total catch blocks method have param = ", total_catch_blocks_method_have_param_count, " count in logged catch=", total_catch_blocks_method_have_param_logged_catch,\
                 "  count in non logged catch=", total_catch_blocks_method_have_param_non_logged_catch
#print "ICTB%=", (if_count_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_count_in_try_non_logged_catch*100/non_logged_catch_count)   


"""
Result 21: % of avg. number of parameters in containing method of catch blocks
"""

avg_param_count_method_have_param=0
avg_param_count_method_have_param_logged_catch=0
avg_param_count_method_have_param_non_logged_catch=0

str30 = "select avg(method_param_count) from "+ catch_training_table +" where is_method_have_param = 1"
#print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
   avg_param_count_method_have_paramt= d[0]
    


str30 = "select avg(method_param_count) from "+ catch_training_table +" where is_method_have_param = 1 and is_catch_logged = 1"
print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    avg_param_count_method_have_param_logged_catch= d[0]


str30 = "select avg(method_param_count) from "+ catch_training_table +" where is_method_have_param = 1 and is_catch_logged = 0"
print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    avg_param_count_method_have_param_non_logged_catch= d[0]
  
print "[PCM]=", "Avg container method param count = ", avg_param_count_method_have_paramt, " avg  in logged catch=",  avg_param_count_method_have_param_logged_catch,\
                 "  avg in non logged catch=", avg_param_count_method_have_param_non_logged_catch
#print "ICTB%=", (if_count_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_count_in_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result 19: % of catch blocks having "Throw/throws"  Try Block Vs. logged and Non-logged catch
"""
total_throw_throws_try=0
throw_throws_try_logged_catch=0
throw_throws_try_non_logged_catch=0

str20 = "select count(*) from "+ catch_training_table +" where throw_throws_try=1 "   
select_cursor.execute(str20)
data20 = select_cursor.fetchall()
for d in data20:
    total_throw_throws_try= d[0]


str20 = "select count(*) from "+ catch_training_table +" where throw_throws_try=1 and  is_catch_logged =1"   
select_cursor.execute(str20)
data20 = select_cursor.fetchall()
for d in data20:
    throw_throws_try_logged_catch= d[0]
    
str21 = "select count(*) from "+ catch_training_table +" where throw_throws_try=1 and is_catch_logged =0"    
select_cursor.execute(str21)
data21 = select_cursor.fetchall()
for d in data21:
    throw_throws_try_non_logged_catch= d[0]   

print "[TTB]=", "Total Throw/ Throws =", total_throw_throws_try, " Total Throw/thorws in try logged catch",  throw_throws_try_logged_catch, " throw/throws non logged=", throw_throws_try_non_logged_catch
print "[TTB] %=", (throw_throws_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (throw_throws_try_non_logged_catch*100/non_logged_catch_count)   


"""
@Result 20: % of catch blocks having "Throw/throws"  in catch Block Vs. logged and Non-logged catch
"""
total_throw_throws_catch = 0
throw_throws_catch_logged_catch=0
throw_throws_catch_non_logged_catch=0

str22 = "select count(*) from "+ catch_training_table +" where throw_throws_catch=1 "  
select_cursor.execute(str22)
data22 = select_cursor.fetchall()
for d in data22:
    total_throw_throws_catch= d[0]

str22 = "select count(*) from "+ catch_training_table +" where throw_throws_catch=1 and  is_catch_logged =1"   
select_cursor.execute(str22)
data22 = select_cursor.fetchall()
for d in data22:
    throw_throws_catch_logged_catch= d[0]
    
str23 = "select count(*) from "+ catch_training_table +" where throw_throws_catch=1 and is_catch_logged =0"    
select_cursor.execute(str23)
data23 = select_cursor.fetchall()
for d in data23:
    throw_throws_catch_non_logged_catch= d[0]   

print "[TTC]=","Total throw/throws in Catch =", total_throw_throws_catch, "Total throw/throws catch logged catch=",  throw_throws_catch_logged_catch, " Total Throw/Throws in catch in non logged=", throw_throws_catch_non_logged_catch
print "[TTC %]=", (throw_throws_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (throw_throws_catch_non_logged_catch*100/non_logged_catch_count)   


"""
@Result 21: % of catch blocks having "Throw/throws"  in Method_BT Vs. logged and Non-logged catch
"""
total_throw_throws_till_try = 0
throw_throws_till_try_logged_catch=0
throw_throws_till_try_non_logged_catch=0

str22 = "select count(*) from "+ catch_training_table +" where throw_throws_till_try=1 "  
select_cursor.execute(str22)
data22 = select_cursor.fetchall()
for d in data22:
    total_throw_throws_till_try= d[0]

str22 = "select count(*) from "+ catch_training_table +" where throw_throws_till_try=1 and  is_catch_logged =1"   
select_cursor.execute(str22)
data22 = select_cursor.fetchall()
for d in data22:
    throw_throws_till_try_logged_catch= d[0]
    
str23 = "select count(*) from "+ catch_training_table +" where throw_throws_till_try=1 and is_catch_logged =0"    
select_cursor.execute(str23)
data23 = select_cursor.fetchall()
for d in data23:
    throw_throws_till_try_non_logged_catch= d[0]   

print "[TTM]=","Total throw/throws in Method_BT =", total_throw_throws_till_try, "Total throw/throws till try logged catch=",  throw_throws_till_try_logged_catch, " Total Throw/Throws in till try in non logged=", throw_throws_till_try_non_logged_catch
print "[TTM %]=", (throw_throws_till_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (throw_throws_till_try_non_logged_catch*100/non_logged_catch_count)   



"""======================================================================================
@Result 22: % of catch blocks having return in try block Vs. logged and Non-logged catch
=========================================================================================="""
total_return_in_try = 0 
return_in_try_logged_catch=0
reutun_in_try_non_logged_catch=0

str14 = "select count(*) from "+ catch_training_table +" where is_return_in_try=1 "    
select_cursor.execute(str14)
data14 = select_cursor.fetchall()
for d in data14:
    total_return_in_try= d[0]

str14 = "select count(*) from "+ catch_training_table +" where is_return_in_try=1 and  is_catch_logged =1"    
select_cursor.execute(str14)
data14 = select_cursor.fetchall()
for d in data14:
    return_in_try_logged_catch= d[0]
    
str15 = "select count(*) from "+ catch_training_table +" where is_return_in_try=1 and is_catch_logged =0"    
select_cursor.execute(str15)
data15 = select_cursor.fetchall()
for d in data15:
    return_in_try_non_logged_catch= d[0]   

print "[RTB]=", "Total return in try = ", total_return_in_try, "Return in try logged catch ", return_in_try_logged_catch, " Return non logged=", return_in_try_non_logged_catch
print "[RTB% ]=", (return_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (return_in_try_non_logged_catch*100/non_logged_catch_count)   


"""
@Result 23: % of catch blocks having return in Catch block Vs. logged and Non-logged catch
"""
total_return_in_catch=0
return_in_catch_logged_catch=0
reutun_in_catch_non_logged_catch=0

str16 = "select count(*) from "+ catch_training_table +" where is_return_in_catch=1 "    
select_cursor.execute(str16)
data16 = select_cursor.fetchall()
for d in data16:
    total_return_in_catch= d[0]

str16 = "select count(*) from "+ catch_training_table +" where is_return_in_catch=1 and  is_catch_logged =1"    
select_cursor.execute(str16)
data16 = select_cursor.fetchall()
for d in data16:
    return_in_catch_logged_catch= d[0]
    
str17 = "select count(*) from "+ catch_training_table +" where is_return_in_catch=1 and is_catch_logged =0"    
select_cursor.execute(str17)
data17 = select_cursor.fetchall()
for d in data17:
    return_in_catch_non_logged_catch= d[0]   

print "[RC]=", "Total return in Catch=", total_return_in_catch, " Return in catch logged catch=",  return_in_catch_logged_catch, " non logged=", return_in_catch_non_logged_catch
print "[RC %]=", (return_in_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (return_in_catch_non_logged_catch*100/non_logged_catch_count)   



"""
@Result 24: % of catch blocks having return in Method_BT  Vs. logged and Non-logged catch
"""
total_return_in_method_BT=0
return_in_method_BT_logged_catch=0
reutun_in_method_BT_non_logged_catch=0

str16 = "select count(*) from "+ catch_training_table +" where is_return_till_try=1 "    
select_cursor.execute(str16)
data16 = select_cursor.fetchall()
for d in data16:
    total_return_in_method_BT= d[0]

str16 = "select count(*) from "+ catch_training_table +" where is_return_till_try=1 and  is_catch_logged =1"    
select_cursor.execute(str16)
data16 = select_cursor.fetchall()
for d in data16:
    return_in_method_BT_logged_catch= d[0]
    
str17 = "select count(*) from "+ catch_training_table +" where is_return_till_try=1 and is_catch_logged =0"    
select_cursor.execute(str17)
data17 = select_cursor.fetchall()
for d in data17:
    return_in_method_BT_non_logged_catch= d[0]   

print "[RM]=", "Total return in method_BT=", total_return_in_method_BT, " Return in method_BT logged catch=",  return_in_method_BT_logged_catch, " non logged=", return_in_method_BT_non_logged_catch
print "[RM %]=", (return_in_method_BT_logged_catch*100/logged_catch_count), "   Non Logged %=", (return_in_method_BT_non_logged_catch*100/non_logged_catch_count)   


"""
@Result 24: % of try blocks with Assert statement  Vs. logged and Non-logged catch
"""
total_assert_in_try = 0
assert_in_try_logged_catch=0
assert_in_try_non_logged_catch=0

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_in_try=1 "  
#print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    total_assert_in_try= d[0]

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_in_try=1 and  is_catch_logged =1"  
#print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    assert_in_try_logged_catch= d[0]
    
str33 = "select count(*) from "+ catch_training_table +" where  is_assert_in_try=1  and is_catch_logged =0"    
select_cursor.execute(str33)
data33 = select_cursor.fetchall()
for d in data33:
    assert_in_try_non_logged_catch= d[0]   

print "[ATB]="," Total assert in try", total_assert_in_try, " assert in try logged catch= ", assert_in_try_logged_catch, " non logged=", assert_in_try_non_logged_catch
print "[ATB]%=", (assert_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (assert_in_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result 25: % of CATCH blocks with Assert statement  Vs. logged and Non-logged catch
"""
total_assert_in_catch = 0
assert_in_catch_logged_catch=0
assert_in_catch_non_logged_catch=0

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_in_catch=1 "  
#print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    total_assert_in_catch= d[0]

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_in_catch=1 and  is_catch_logged =1"  
#print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    assert_in_catch_logged_catch= d[0]
    
str33 = "select count(*) from "+ catch_training_table +" where  is_assert_in_catch=1  and is_catch_logged =0"    
select_cursor.execute(str33)
data33 = select_cursor.fetchall()
for d in data33:
    assert_in_catch_non_logged_catch= d[0]   

print "[AC]=","total assert in catch= ", total_assert_in_catch, "assert in logged catch=" ,assert_in_catch_logged_catch, " non logged=", assert_in_catch_non_logged_catch
print "[AC%]=", (assert_in_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (assert_in_catch_non_logged_catch*100/non_logged_catch_count)   


"""==============================================================================
@Result 26: % of method_BT with Assert statement  Vs. logged and Non-logged catch
================================================================================="""
total_assert_in_method_BT = 0
assert_in_method_BT_logged_catch=0
assert_in_method_BT_non_logged_catch=0

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_till_try=1 "  
#print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    total_assert_in_method_BT= d[0]

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_till_try=1 and  is_catch_logged =1"  
#print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    assert_in_method_BT_logged_catch= d[0]
    
str33 = "select count(*) from "+ catch_training_table +" where  is_assert_till_try=1  and is_catch_logged =0"    
select_cursor.execute(str33)
data33 = select_cursor.fetchall()
for d in data33:
    assert_in_method_BT_non_logged_catch= d[0]   

print "[AM]=","total assert in method_BT= ", total_assert_in_method_BT, "assert in method_BT logged catch=" ,assert_in_method_BT_logged_catch, " non logged=", assert_in_method_BT_non_logged_catch
print "[AM%]=", (assert_in_method_BT_logged_catch*100/logged_catch_count), "   Non Logged %=", (assert_in_method_BT_non_logged_catch*100/non_logged_catch_count)   



"""===================================================================================
@Result 27: % of Try blocks having Thread.Sleep  Block Vs. logged and Non-logged catch
======================================================================================"""

total_thread_sleep_try = 0
thread_sleep_try_logged_catch=0
thread_sleep_try_non_logged_catch=0

str24 = "select count(*) from "+ catch_training_table +" where is_thread_sleep_try=1 "  
print "str24", str24 
select_cursor.execute(str24)
data24 = select_cursor.fetchall()
for d in data24:
    total_thread_sleep_try= d[0]

str24 = "select count(*) from "+ catch_training_table +" where is_thread_sleep_try=1 and  is_catch_logged =1"  
print "str24", str24 
select_cursor.execute(str24)
data24 = select_cursor.fetchall()
for d in data24:
    thread_sleep_try_logged_catch= d[0]
    
str25 = "select count(*) from "+ catch_training_table +" where is_thread_sleep_try=1 and is_catch_logged =0"    
select_cursor.execute(str25)
data25 = select_cursor.fetchall()
for d in data25:
    thread_sleep_try_non_logged_catch= d[0]   

print "[TSTB]=", "total thread sleep try=", total_thread_sleep_try, " thread sleep try logged=",thread_sleep_try_logged_catch, " non logged=", thread_sleep_try_non_logged_catch
print "[TSTB %]=", (thread_sleep_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (thread_sleep_try_non_logged_catch*100/non_logged_catch_count)   


"""========================================================================================
@Result  28: % of Catch blocks having InterruptedException Vs. logged and Non-logged catch
==========================================================================================="""
total_interrupted_exception = 0
interrupted_exp_logged_catch=0
interrupted_exp_non_logged_catch=0

str24 = "select count(*) from "+ catch_training_table +" where is_interrupted_exception=1"  
#print "str24", str24 
select_cursor.execute(str24)
data24 = select_cursor.fetchall()
for d in data24:
    total_interrupted_exception= d[0]

str24 = "select count(*) from "+ catch_training_table +" where is_interrupted_exception = 1 and is_catch_logged = 1 "  
#print "str24", str24 
select_cursor.execute(str24)
data24 = select_cursor.fetchall()
for d in data24:
    interrupted_exp_logged_catch= d[0]
    
str27 = "select count(*) from "+ catch_training_table +" where is_interrupted_exception=1 and is_catch_logged =0"    
select_cursor.execute(str27)
data27 = select_cursor.fetchall()
for d in data27:
    interrupted_exp_non_logged_catch= d[0]   

print "[TSTB]=","total interrupted exception=",total_interrupted_exception, "  interrupted exception logged catch=",  interrupted_exp_logged_catch, " non logged=", interrupted_exp_non_logged_catch
print "[TSTB %]=", (interrupted_exp_logged_catch*100/logged_catch_count), "   Non Logged %=", (interrupted_exp_non_logged_catch*100/non_logged_catch_count)   


""" =========================================================================
@Result  29: % of Catch blocks object =ignore Vs. logged and Non-logged catch
=============================================================================="""
total_ignore_catch = 0
ignore_logged_catch=0
ignore_non_logged_catch=0

str28 = "select count(*) from "+ catch_training_table +" where  is_catch_object_ignore=1 "  
#print "str", str28 
select_cursor.execute(str28)
data28 = select_cursor.fetchall()
for d in data28:
    total_ignore_catch= d[0]

str28 = "select count(*) from "+ catch_training_table +" where  is_catch_object_ignore=1 and  is_catch_logged =1"  
#print "str", str28 
select_cursor.execute(str28)
data28 = select_cursor.fetchall()
for d in data28:
    ignore_logged_catch= d[0]
    
str29 = "select count(*) from "+ catch_training_table +" where  is_catch_object_ignore=1  and is_catch_logged =0"    
select_cursor.execute(str29)
data29 = select_cursor.fetchall()
for d in data29:
    ignore_non_logged_catch= d[0]   

print "[EOIC]=", " total_ignore_catch=", total_ignore_catch, "   ignore in logged catch= ", ignore_logged_catch, " non logged=", ignore_non_logged_catch
print "[EOIC %]=", (ignore_logged_catch*100/logged_catch_count), "   Non Logged %=", (ignore_non_logged_catch*100/non_logged_catch_count)   


"""==============================================================================================
@Result: Ratio of the non logged and non logged catch blocks 
================================================================================================="""

with open(exception_ratio_file, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Exception']+ ['Total Count','Logged catch count','Logged Ratio','Non Logged Catch Count', 'Non Logged Ratio'])
    
    all_exception = []
    str = "select distinct catch_exc  from " + catch_training_table
    select_cursor.execute(str)
    data = select_cursor.fetchall()
    for exp  in data:
        all_exception.append(exp[0])
        
    #print "all exception=", all_exception  
     
    for exp in all_exception:
        
        total = 0
        logged_catch_count = 0
        non_logged_catch_count=0
        
        str =  "select count(*) from "+catch_training_table + " where catch_exc='"+exp+"'" 
        select_cursor.execute(str)
        data = select_cursor.fetchall()        
        for temp in data:
            total =  temp[0]
         
        if total>=10:
            
            str =  "select count(*) from "+catch_training_table + " where catch_exc='"+exp+"' and is_catch_logged= 1 " 
            select_cursor.execute(str)
            data = select_cursor.fetchall()        
            for temp in data:
                logged_catch_count =  temp[0]   
            
            
            str =  "select count(*) from "+catch_training_table + " where catch_exc='"+exp+"' and is_catch_logged= 0 " 
            select_cursor.execute(str)
            data = select_cursor.fetchall()        
            for temp in data:
                non_logged_catch_count =  temp[0]    
        
        
            logged_ratio = (logged_catch_count *100)/total
            non_logged_ratio = (non_logged_catch_count*100)/total
            spamwriter.writerow([exp, total, logged_catch_count,logged_ratio, non_logged_catch_count, non_logged_ratio])


#==============BOX PLOT=====================#

"""
@Result9: % of catch blocks having "Throwable" exception in Catch block Vs. logged and Non-logged catch
"""
throwable_catch_exception_logged_catch=0
throwable_catch_exception_non_logged_catch=0
str18 = "select count(*) from "+ catch_training_table +" where catch_exc = 'Throwable' and  is_catch_logged =1"    

select_cursor.execute(str18)
data18 = select_cursor.fetchall()
for d in data18:
    throwable_catch_exception_logged_catch= d[0]
    
str19 = "select count(*) from "+ catch_training_table +" where catch_exc='Throwable' and is_catch_logged =0"    
select_cursor.execute(str19)
data19 = select_cursor.fetchall()
for d in data19:
    throwable_catch_exception_non_logged_catch= d[0]   

print "CBTH=", throwable_catch_exception_logged_catch, " non logged=", throwable_catch_exception_non_logged_catch
print "CBTH %=", (throwable_catch_exception_logged_catch*100/logged_catch_count), "   Non Logged %=", (throwable_catch_exception_non_logged_catch*100/non_logged_catch_count)   





"""
@Result17: % Box plot for IF count in try block Vs. logged and Non-logged catch
"""
if_count_try_logged_catch=[]
if_count_try_non_logged_catch=[]

str32 = "select if_count_in_try from "+ catch_training_table +" where   is_catch_logged =1"  
print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    if_count_try_logged_catch.append(d[0])
    
str33 = "select if_count_in_try from "+ catch_training_table +" where  is_catch_logged =0"    
select_cursor.execute(str33)
data33 = select_cursor.fetchall()
for d in data33:
    if_count_try_non_logged_catch.append(d[0])   
 
boxplot(if_count_try_logged_catch)
plt.title("Logged Catches Vs. tif Count")    
boxplot(if_count_try_non_logged_catch)
plt.title("Non Logged Catches Vs. tif Count")


"""
@Result 4:  Box Plot of sloc present in the try block and logged & Non-logged catch blocks
"""
str4 = "select try_loc from "+ catch_training_table+ " where is_catch_logged=1"
select_cursor.execute(str4)
data4 = select_cursor.fetchall()

try_loc_logged_catch =[]
for d in data4:
    #print d[0]
    try_loc_logged_catch.append(d[0])
    
boxplot(try_loc_logged_catch)
plt.title("Logged Catch Vs. LOC in Try Block")
figure()

str5 = "select try_loc from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str5)
data5 = select_cursor.fetchall()

try_loc_non_logged_catch =[]
for d in data5:
    #print d[0]
    try_loc_non_logged_catch.append(d[0])
    
boxplot(try_loc_non_logged_catch)
plt.title("Non Logged Catches Vs. LOC in Try Block")



"""
@Result3:  Box Plot of count log statements present in the try block and logged & Non-logged catch blocks
"""
str6 = "select try_log_count from "+ catch_training_table+ " where is_catch_logged=1"
select_cursor.execute(str6)
data6 = select_cursor.fetchall()

try_loc_logged_catch =[]
for d in data6:
    #print d[0]
    try_loc_logged_catch.append(d[0])
    
boxplot(try_loc_logged_catch)
plt.title("Logged Catch Vs. Log Count in Try Block")
figure()

str7 = "select try_log_count from "+ catch_training_table+ " where is_catch_logged=0"
select_cursor.execute(str7)
data7 = select_cursor.fetchall()

try_loc_non_logged_catch =[]
for d in data7:
    #print d[0]
    try_loc_non_logged_catch.append(d[0])
    
boxplot(try_loc_non_logged_catch)
plt.title("Non Logged Catches Vs. Log Count in Try Block")


show()