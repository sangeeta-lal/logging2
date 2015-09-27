

import MySQLdb
from pylab import *
import matplotlib.pyplot as plt
import csv

"""
@Author: Sangeeta
@Uses:  This file is used to create tables in the paper
@Data: It will use TABLE :" TRAINING2_IF "  for creating the tables
"""
project = "tomcat_"
#project="cloudstack_"

"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level2"
file_path = "E:\\Sangeeta\\Research\\logging\\result"
"""
port=3306
user="root"
password="1234"
database="logging_level2"
file_path = "F:\\Research\\logging\\result"
#"""

"""
@Table
"""
if_training_table =  project+"if_training2"

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()


"""===============================================================
@Results 1: 
Total Count of IF blocks , logged if block and non-logged if blocks
===================================================================="""

total_if_count=0
logged_if_count = 0

total_if_str = "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'"
             
select_cursor.execute(total_if_str)
total_if_count = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    total_if_count = temp[0]
    
if_with_log_str = "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and  is_if_logged = 1 and \
                if_expr not like '%isTraceEnabled()' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'"
               
select_cursor.execute(if_with_log_str)
if_with_log = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    if_with_log = temp[0]    

print "Total If Count=", total_if_count
print "IF with logs=", if_with_log   

"""=======================================================================
@Note: Result 2: Loc of method_BI in logged Vs. non-logged If block
=========================================================================="""
str =  "select  avg(loc_till_if) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_if_loc_logged =  data[0][0]

str =  "select  avg(loc_till_if) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_if_loc_non_logged =  data[0][0]    

print " Avg Loc [SM]=", " avg loc =",  avg_if_loc_logged, "  avg if loc non logged=", avg_if_loc_non_logged
    
#print "Total catch=", total_catch_count, " logged catch count=", logged_catch_count, " Non logged Catch Count=", non_logged_catch_count     


"""=========================================================================================
@Note: Result 3: Logged method_BI in logged if block vs. non logged if block
============================================================================================"""
str =  "select  count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1  and is_till_if_logged = 1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
count_till_if_logged =  data[0][0]

str =  "select  count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_till_if_logged = 1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
count_till_if_non_logged =  data[0][0]    

print " Logged method [LM]=", " logged method Bi logged if=", count_till_if_logged, "  logged method Bi non logged if=", count_till_if_non_logged


"""=========================================================================================
@Note: Result 4: Logged count method_BI in logged if block vs. non logged if block
============================================================================================"""
str =  "select  avg(till_if_log_count)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_log_count_till_if_logged =  data[0][0]

str =  "select  avg(till_if_log_count)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_log_count_till_if_non_logged =  data[0][0]    

print " Logged method [LCM]=", "Avg log count method Bi logged if=", avg_log_count_till_if_logged, "  avg log count method BI non logged if=", avg_log_count_till_if_non_logged


"""===========================================================================================
@Note: Result 5: Count of operators in method bit in logged Vs Non logged if
=============================================================================================="""

str =  "select  avg(operators_count_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_operators_count_till_if_logged =  data[0][0]

str =  "select  avg(operators_count_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_operators_count_till_if_non_logged =  data[0][0]    

print " Logged method [COM]=", "avg operator count method Bi logged if=", avg_operators_count_till_if_logged, "  avg operator count method BI non logged if=", avg_operators_count_till_if_non_logged



"""===========================================================================================
@Note: Result 6: Count of variables in method BI in logged Vs Non logged if
=============================================================================================="""

str =  "select  avg(variables_count_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_variable_count_till_if_logged =  data[0][0]

str =  "select  avg(variables_count_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_variable_count_till_if_non_logged =  data[0][0]    

print " Logged method [VCM]=", "avg variable count method Bi logged if=", avg_variable_count_till_if_logged, "  avg variable count method BI non logged if=", avg_variable_count_till_if_non_logged



"""===========================================================================================
@Note: Result 7: Method call count in logged Vs Non logged if
=============================================================================================="""

str =  "select  avg(method_call_count_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_method_call_count_till_if_logged =  data[0][0]

str =  "select  avg(method_call_count_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_method_call_count_till_if_non_logged =  data[0][0]    

print " Logged method [MNM]=", "avg method call count method Bi logged if=", avg_method_call_count_till_if_logged, "  avg method call count method BI non logged if=", avg_method_call_count_till_if_non_logged


"""===========================================================================================
@Note: Result 8: if in method_BI logged Vs Non logged if
=============================================================================================="""

str =  "select  count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and if_in_till_if = 1 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
if_in_till_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and if_in_till_if = 1 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
if_in_till_if_non_logged =  data[0][0]    

print " If in method BI [IM]=", " IF method BI logged if=", if_in_till_if_logged, "  IF  method BI non logged if=", if_in_till_if_non_logged


"""===========================================================================================
@Note: Result 9: Avg if count in method_BI logged Vs Non logged if
=============================================================================================="""

str =  "select  avg(if_count_in_till_if)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_if_count_till_if_logged =  data[0][0]

str =  "select  avg(if_count_in_till_if) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
avg_if_count_till_if_non_logged =  data[0][0]    

print "avg if count method BI [IM]=", " avg if count method BI logged if=", avg_if_count_till_if_logged, "  avg if count method BI non logged if=", avg_if_count_till_if_non_logged



"""===========================================================================================
@Note: Result 10: method_have_parameter logged Vs Non logged if
=============================================================================================="""

str =  "select  count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_method_have_param = 1 "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
method_have_param_count_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0  and is_method_have_param = 1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
method_have_param_count_if_non_logged =  data[0][0]    

print "method have param [PM]=", " method have param logged if=", method_have_param_count_if_logged, "  method have param non logged if=", method_have_param_count_if_non_logged



"""===========================================================================================
@Note: Result 11: null logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_null_condition_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
null_condition_count_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_null_condition_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
null_condition_count_if_non_logged =  data[0][0]    

print "null condition [NC]=", " null condition count logged if=", null_condition_count_if_logged, "  null condition count non logged if=", null_condition_count_if_non_logged



"""===========================================================================================
@Note: Result 12: instanceOf logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_instance_of_condition_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
instance_of_condition_count_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_instance_of_condition_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
instance_of_condition_count_if_non_logged =  data[0][0]    

print "instanceOf condition [IOC]=", " instanceOf condition count logged if=", instance_of_condition_count_if_logged, "  instanceOF condition count non logged if=", instance_of_condition_count_if_non_logged




"""===========================================================================================
@Note: Result 13: throw/throws if logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and throw_throws_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
throw_count_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and throw_throws_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
throw_count_if_non_logged =  data[0][0]    

print "throw count [TTI]=", " throw count logged if=", throw_count_if_logged, "  throw count non logged if=", throw_count_if_non_logged




"""===========================================================================================
@Note: Result 14: throw/throws in method_BI logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and throw_throws_till_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
throw_count_till_if_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and throw_throws_till_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
throw_count_till_if_if_non_logged =  data[0][0]    

print "throw count [TTM]=", " throw count till if logged if=", throw_count_till_if_if_logged, "  throw count till if non logged if=", throw_count_till_if_if_non_logged




"""===========================================================================================
@Note: Result 15: return in if block logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_return_in_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
return_count_till_if_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_return_in_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
return_count_till_if_if_non_logged =  data[0][0]    

print " return in if [RC]=", " return count in if if logged if=", return_count_till_if_if_logged, "  return count in if if non logged if=", return_count_till_if_if_non_logged


"""===========================================================================================
@Note: Result 16: RETURN  in method_BI logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_return_in_till_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
return_count_till_if_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_return_in_till_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
return_count_till_if_if_non_logged =  data[0][0]    

print "return count [RM]=", " return count till if logged if=", return_count_till_if_if_logged, "  return count till if non logged if=", return_count_till_if_if_non_logged



"""===========================================================================================
@Note: Result 17: assert in if logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_assert_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
assert_count_in_if_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_assert_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
assert_count_in_if_if_non_logged =  data[0][0]    

print "assert count [AI]=", " assert count in if logged if=", assert_count_in_if_if_logged, "  assert count in if non logged if=", assert_count_in_if_if_non_logged




"""===========================================================================================
@Note: Result 18: assert in till if logged Vs Non logged if
=============================================================================================="""

str =  "select count(*)  from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 1 and is_assert_till_if=1"
  
select_cursor.execute(str)
data = select_cursor.fetchall()
assert_count_in_till_if_if_logged =  data[0][0]

str =  "select  count(*) from "+ if_training_table+" where if_expr!=\'\' and if_expr not like '%isTraceEnabled()%' and \
               if_expr not like '%isDebugEnabled()' and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'\
               and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and is_if_logged = 0 and is_assert_till_if=1  "
  
select_cursor.execute(str)
data = select_cursor.fetchall()
assert_count_in_till_if_if_non_logged =  data[0][0]    

print "assert count [AM]=", " assert count in till if logged if=", assert_count_in_till_if_if_logged, "  assert count in till if non logged if=", assert_count_in_till_if_if_non_logged

