
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
"""
#This file is used to craete graph for characterization study of logging levels
1. Function Count Vs. Logging level count
2.  
"""

port=3306
user="root"
password="123"
database="logging_level"
table = "tomcat_level_feature"
#To save files on specified locations
file_path="D:\\Research\\Logging\\result\\graph\\"

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()
"""
#Graph 1
select_str = "select count(*) from " +table+ " where level=\"\""
print"select str=", select_str
select_cursor.execute(select_str)
function_without_log = select_cursor.fetchall()[0][0]
print "fucntion_with_0_log=", function_without_log

#Graph 1
#==================# 
log_1=0
log_2=0
log_3=0
log_4=0
log_more=0
log_count=list()
select_str = "select level from " +table+ " where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()
for d in data:
    level= d[0].strip() 
    level=' '.join(level.split())
    length = len(level.split(" "))
    log_count.append(length)
    if length==1:
        log_1=log_1+1
    elif length==2:
        log_2=log_2+1 
    elif length==3:
        log_3=log_3+1
    elif length==4:
        log_4=log_4+1
    else:
        log_more=log_more+1  

print "log_1=", log_1
print "log_2=", log_2
print "log_3=", log_3
print "log_4=", log_4
print "log_more=", log_more

print "len=", length, level, log_count


#plt.title('Distribution of Log')
plt.ylabel('Function Count')
plt.xlabel('No. of Log Statements')
#plt.grid(True)
x=[1,2,3,4,5]
plt.xticks([1, 2, 3, 4,5], ['1', '2', '3', '4','>=5'])
log_count=[486,189,70,49,70]
plt.bar(x,log_count,width=0.3, align='center', color='green')
plt.plot(x, log_count, color='purple', lw=0.5, marker='s')
plt.savefig(file_path+"funcount-vs-log.eps")
plt.show()


#Graph 2
#================#
#Select all the tuple
select_str = "select method_content, level, method from " +table
select_cursor.execute(select_str)
data = select_cursor.fetchall()

method_body_loc=list()
method_body_noc=list()#Number of characters
log_count=list()
for d in data:
    method_content =d[0].strip()
    method_name = d[2].strip()
   # method_size = len(' '.join(method_content.split()))  #level=' '.join(level.split())
   # method_body_noc.append(method_size)
   
    method_loc = 0
    temp_method_content = method_content.split("\n")  #level=' '.join(level.split())
    #print "content", method_content
    for t in temp_method_content:
        if t:
            method_loc = method_loc+1
            
    method_body_loc.append(method_loc)
    
    level= d[1].strip() 
    print "level", level
    if not level:
        length=0
    else:    
        level=' '.join(level.split())
        length = len(level.split(" "))# No of log statements
    log_count.append(length)
    
    print "Method Name=", method_name,"LOC=", method_loc," log statement count=",length

#Plot Scatter Plot    
#========#      

plt.xlabel('Function Size(LOC)')
plt.ylabel('No. of Log Statements')
plt.scatter(method_body_loc, log_count,color='green')
plt.xlim([0,400])
plt.ylim([-1,25])
plt.savefig(file_path+"fun-scatter.eps")
plt.show()

#====================Graph 3===============#
#Removing outliers from the above figure
plt.xlabel('Function Size(LOC)')
plt.ylabel('No. of Log Statements')
plt.scatter(method_body_loc, log_count,color='red')
plt.xlim([0,250])
plt.ylim([-1,20])
plt.savefig(file_path+"fun-scatter-without-outliers.eps")

plt.show()
"""

#=====================Graph 4================#
##To make box plot of log level and LOC
debug_method_loc=list()
error_method_loc=list()
info_method_loc=list()
warn_method_loc=list()
trace_method_loc=list()
fatal_method_loc=list()

select_str = "select method_content, level from " +table+" where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()

for d in data:
    method_content = d[0].strip()
    method_loc = 0
    
    temp_method_content = method_content.split("\n")  #level=' '.join(level.split())
    #print "content", method_content
    for t in temp_method_content:
        if t:
            method_loc = method_loc+1
    
    info_flag=0
    error_flag=0
    trace_flag=0
    debug_flag=0
    warn_flag=0
    fatal_flag=0
    level= d[1].strip() 
    print "level", level
    level=' '.join(level.split())
    level_array=level.split(" ")
    for l in level_array:
        if l == "info":
            info_method_loc.append(method_loc)
        elif l=="error":
            error_method_loc.append(method_loc)
        elif l=="trace":
            trace_method_loc.append(method_loc)
        elif l=="debug":
            debug_method_loc.append(method_loc)
        elif l=="warn":
            warn_method_loc.append(method_loc)
        elif l=="fatal":
            fatal_method_loc.append(method_loc)

boxes=[]

boxes.append(debug_method_loc)
boxes.append(error_method_loc)
boxes.append(warn_method_loc)
boxes.append(info_method_loc)
boxes.append(trace_method_loc)
boxes.append(fatal_method_loc)
plt.figure()
plt.hold = True
plt.boxplot(boxes,vert=0)
labels=[" "," Debug"," Error"," Wran"," Info"," Trace"," Fatal"]
plt.yticks(range(len(labels)), labels, rotation=90, va="top", ha="center", fontsize=14)
plt.xlabel('Function Size(LOC)',fontsize=14)
plt.xlim([0,150])
plt.savefig(file_path+"level-vs-loc.eps")
plt.show()
#===========Graph 5=================#
select_str = "select method_content, level from " +table+" where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()
method_body_sizes=list()
unique_log_count=list()

select_str = "select method_content, level from " +table+ " where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()
for d in data:
    method_content =d[0].strip()
    method_size = len(' '.join(method_content.split()))  #level=' '.join(level.split())
    method_body_sizes.append(method_size)
    
    info_flag=0
    error_flag=0
    trace_flag=0
    debug_flag=0
    warn_flag=0
    fatal_flag=0
    level= d[1].strip() 
    print "level", level
    level=' '.join(level.split())
    level_array=level.split(" ")
    for l in level_array:
        if l == "info":
            info_flag=1
        elif l=="error":
            error_flag=1
        elif l=="trace":
            trace_flag=1
        elif l=="debug":
            debug_flag=1
        elif l=="warn":
            warn_flag=1
        elif l=="fatal":
            fatal_flag=1
    
    unique_level=info_flag+error_flag+trace_flag+debug_flag+warn_flag+fatal_flag
    
    print "unique level", unique_level
    unique_log_count.append(unique_level)

plt.xlabel('Function Size(NOC)')
plt.ylabel('No. of Different Log Levels Used')
plt.scatter(method_body_sizes, unique_log_count,color='red')
plt.show()

#====================Graph6==============================#
#==================heatMap================================#

info_count=0
trace_count=0
warn_count=0
fatal_count=0
debug_count=0
error_count=0
select_str = "select method, level from " +table+" where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()
for d in data:
    method_name = d[0]
    
    info_count=0
    trace_count=0
    warn_count=0
    fatal_count=0
    debug_count=0
    error_count=0
    
    level= d[1].strip() 
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
    

#=================Table 1=================#
#This identifies how many log statment are their and what %percentage they are of total log statements
total_log_lines = 0
info_count=0
trace_count=0
warn_count=0
fatal_count=0
debug_count=0
error_count=0

select_str = "select level from " +table+" where level!=\"\""
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
    
print "Total_log_statements=",total_log_lines
print"info=",info_count
print"trace=",trace_count
print "warn=",warn_count
print "fatal=",fatal_count
print "debug=",debug_count
print "error=",error_count


#"""