
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import csv
import re

"""
#This file is used to creats tables for characterization study of logging levels
1. 
2.  
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
password="123"
database="logging_level"
file_path = "D:\\Research\\logging\\result"
#"""

log_table= project+"level_feature"
train_catch_table=project+"catch_train"
#unique_catch_table = project+"unique_catch_feature"

#unique_if_table = project+"unique_if_feature"
unique_if_table = project+"if_train"
null_instance_table = project+"if_only_null_instance"

exception_file = file_path+"\\" +project+"level_ratio.csv"
unique_exception_file = file_path+"\\"+project+"unique_expt.csv" #Not required

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()
temp_cursor =db1.cursor()

#=================Table 1=================#
#This identifies how many log statment are their and what %percentage they are of total log statements
total_log_lines = 0
info_count=0
trace_count=0
warn_count=0
fatal_count=0
debug_count=0
error_count=0

select_str = "select level from " +log_table+" where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()

for d in data:
    level= d[0].strip() 
    level=' '.join(level.split())
    level_array=level.split(" ")
    for l in level_array:
        total_log_lines = total_log_lines+1
        if l == "info":
            info_count=info_count+1
        elif l=="error":
            error_count=error_count+1
        elif l=="trace":
            trace_count=trace_count+1
        elif l=="debug":
            debug_count=debug_count+1
        elif l=="warn":
            warn_count=warn_count+1
        elif l=="fatal":
            fatal_count=fatal_count+1
 
print "-----------------------\n" 
print "Project=", project    
print "-------------------------\n"
print "Total_log_statements=",total_log_lines
print"info=",info_count
print"trace=",trace_count
print "warn=",warn_count
print "fatal=",fatal_count
print "debug=",debug_count
print "error=",error_count
#"""

#===============Table 2==========================================#
#=============To show correlation catch exceptions and ===#
print"===== Table 2===================\n"


expt_count_str = "select   distinct exp FROM  "+train_catch_table+ " where exp!=\'\'"
select_cursor.execute(expt_count_str)
data1 = select_cursor.fetchall()
excep_count = len(data1)

print "Distinct Exception Count=", excep_count, "\n"

#expt_level_str = "select  level, count(*) from " + train_catch_table +" where exp!=\'\' group by level "
#select_cursor.execute(expt_level_str)
#data2 = select_cursor.fetchall()
#for d in data2:
#    print "level=", d[0], "  count=", d[1]


with open(exception_file, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Exception']+ ['Total','None','None Ratio','Trace', 'Trace Ratio','Debug', 'Debug Ratio',
                                        'Info','Info Ratio','Warn','Warn Ratio','Error','Error Ratio','Fatal','Fatal Ratio'])


    expt_count_str = "select   distinct exp FROM  "+train_catch_table+ " where exp!=\'\'"
    select_cursor.execute(expt_count_str)
    data1 = select_cursor.fetchall()
    for d in data1:
        #print "exception", d[0]
        exception = d[0]
        temp_str = "select exp,count(*) from "+ train_catch_table+" where exp ='"+exception+"'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        exception_count = 0
        total = 0
        for temp in temp_data:
            exception_count  = temp[1]
        total = exception_count    
           
        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level=\'\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        none = 0
        for temp in temp_data:
            none=temp[1]
        none_ratio = 0
        if  none:
            none_ratio = (none*100)/exception_count
    
        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level like \'%trace%\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        trace = 0
        for temp in temp_data:
            trace=temp[1]
    
        trace_ratio = 0
        if  trace:
            trace_ratio = (trace*100)/exception_count
            
        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level like \'%debug%\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        debug  = 0
        for temp in temp_data:
            debug=temp[1]
        debug_ratio = 0
        if  debug:
            debug_ratio = (debug*100)/exception_count

        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level like \'%info%\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        info =  0
        for temp in temp_data:
            info=temp[1]
        
        info_ratio = 0
        if  info:
            info_ratio = (info*100)/exception_count
        
        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level like \'%warn%\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        warn =  0
        for temp in temp_data:
            warn=temp[1]
        warn_ratio = 0
        if  warn:
            warn_ratio = (warn*100)/exception_count
       
        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level like \'%error%\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        error  = 0
        for temp in temp_data:
            error=temp[1]
       
        error_ratio = 0
        if  error:
            error_ratio = (error*100)/exception_count    
    
    
        temp_str = "select level, count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level like \'%fatal%\'"
        temp_cursor.execute(temp_str)
        temp_data = temp_cursor.fetchall()
        fatal  = 0
        for temp in temp_data:
            fatal=temp[1]
        fatal_ratio = 0
        if  fatal:
            fatal_ratio = (fatal*100)/exception_count
        

        spamwriter.writerow([exception, total, none,none_ratio, trace, trace_ratio,debug,debug_ratio, info,info_ratio,
                             warn,warn_ratio, error, error_ratio,fatal, fatal_ratio])
        
        #print exception,            none,trace, debug, info, warn, error, fatal 


#=======================Table 3==============================#
print "=========Result 3====="
all_catch_str = "select count(*) from "+ train_catch_table +" where exp!=''"
select_cursor.execute(all_catch_str)
all_catch_count=0
catch_with_log= 0

temp_data = select_cursor.fetchall()
for temp in temp_data:
    all_catch_count = temp_data[0][0] 

catch_with_log = "select count(*) from "+ train_catch_table +" where level!='' and exp!=''"
select_cursor.execute(catch_with_log)
temp_data = select_cursor.fetchall()
for temp in temp_data:
    catch_with_log = temp_data[0][0] 


print "Total Catch =", all_catch_count
print "Catch with Log =", catch_with_log,  "  Ratio=", (((catch_with_log)*100)/all_catch_count)

#=================Result 4===============================================================#
print "====== Result 4===="
with open(unique_exception_file, 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Exception']+ ['All Count','With Log Count'])
    
    expt_count_str = "select   distinct exp FROM  "+train_catch_table+ " where exp!=\'\'"
    select_cursor.execute(expt_count_str)
    data1 = select_cursor.fetchall()
    for d in data1:
        #print "exception", d[0]
        exception = d[0]
    
    
        all_expt_str = "select count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"'"
        temp_cursor.execute(all_expt_str)
        temp_data = temp_cursor.fetchall()
        all_expt_count = 0
        for temp in temp_data:
            all_expt_count=temp[0]
    
        with_log_str = "select count(*), exp  from  "+train_catch_table+" where exp='"+d[0]+"' and level!=\'\'"
        temp_cursor.execute(with_log_str)
        temp_data = temp_cursor.fetchall()
        with_log_count = 0
        for temp in temp_data:
            with_log_count=temp[0]
        
        spamwriter.writerow([exception, all_expt_count, with_log_count])
        
        
#=========================== Result ====================#
##===========================IF Results=================#     
print "---------------------IF Results-------------------"
total_if_str = "select  count(*) from "+ unique_if_table+" where expr!=\'\' and expr not like '%isTraceEnabled()%' and \
               expr not like '%isDebugEnabled()' and expr not like '%isInfoEnabled()' and expr not like '%isWarnEnabled()'\
               and expr not like '%isErrorEnabled()'  and expr not like '%isFatalEnabled()'"
#print "total if str=", total_if_str               
select_cursor.execute(total_if_str)
total_if_count = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    total_if_count = temp[0]
    
if_with_log_str = "select  count(*) from "+ unique_if_table+" where expr!=\'\' and level!=\'\' and \
                expr not like '%isTraceEnabled()' and \
               expr not like '%isDebugEnabled()' and expr not like '%isInfoEnabled()' and expr not like '%isWarnEnabled()'\
               and expr not like '%isErrorEnabled()'  and expr not like '%isFatalEnabled()'"
print "if with log str", if_with_log_str
select_cursor.execute(if_with_log_str)
if_with_log = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    if_with_log = temp[0]    

print "Total If Count=", total_if_count
print "IF with logs=", if_with_log   

all_instanceOf_if_str = "select  count(*) from "+ unique_if_table+" where expr!=\'\' and expr like \'%instanceof%\' "
select_cursor.execute(all_instanceOf_if_str)
all_instanceOf_if_count = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    all_instanceOf_if_count = temp[0]  
    
all_instanceOf_with_log_if_str = "select  count(*) from "+ unique_if_table+" where expr!=\'\' and expr like \'%instanceof%\' \
                                and level!='' "
select_cursor.execute(all_instanceOf_with_log_if_str)
all_instanceOf_with_log_if_count = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    all_instanceOf_with_log_if_count = temp[0]      

print "If with instanceOf=", all_instanceOf_if_count
print "If with instanceOf with log=", all_instanceOf_with_log_if_count

all_if_str = "select expr from "+unique_if_table+" where expr!=''"
select_cursor.execute(all_if_str)
all_null_if_count = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    expr = temp[0]
    if re.search(r'=\s*null', expr):
        #print "null=",expr
        all_null_if_count = all_null_if_count+1
 
all_if_with_log_str = "select expr from "+unique_if_table+" where expr!='' and level!=''"
select_cursor.execute(all_if_with_log_str)
all_null_if_with_log_count = 0
temp_data =select_cursor.fetchall()
for temp in temp_data:
    expr = temp[0]
    if re.search(r'=\s*null', expr):
        #print "null=",expr
        all_null_if_with_log_count = all_null_if_with_log_count+1

print "all_null_if_count=",all_null_if_count
print "all_null_if_with_log_count=", all_null_if_with_log_count
     


select_str = "select  type, level,  count(*) from "+ null_instance_table+ " where type= 'instanceof' group by level  "
print "select str=", select_str
select_cursor.execute(select_str)
temp_data =select_cursor.fetchall()
for temp in temp_data:
    type = temp[0]
    level = temp[1]
    count = temp[2]
    print "type=", type,"level=", level, " count=", count     

print "\n-----"
select_str = "select  type, level,  count(*) from "+ null_instance_table+ " where type= 'null' group by level  "
select_cursor.execute(select_str)
temp_data =select_cursor.fetchall()
for temp in temp_data:
    type = temp[0]
    level = temp[1]
    count = temp[2]
    print "type=", type,"level=", level, " count=", count 
print"\n========================="          

