

import MySQLdb
from pylab import *
import matplotlib.pyplot as plt
import csv

"""
@Author: Sangeeta
@Uses:  This file is sed to create tables in the paper
@Data: It will use "training2  catch"  for creating the tables for APSEC-2015 paper
"""
#project = "tomcat_"
project="cloudstack_"

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
database="logging_level"
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
@Result2:  Box Plot of sloc present in the try block and logged & Non-logged catch blocks
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


"""
@Result4: % of catch blocks having try logged Vs logged/nonlogged catch blcks
"""
logged_try_logged_catch=0
logged_try_non_logged_catch=0
str8 = "select count(*) from "+ catch_training_table +" where is_try_logged=1 and  is_catch_logged =1"    
select_cursor.execute(str8)
data8 = select_cursor.fetchall()
for d in data8:
    logged_try_logged_catch= d[0]
    
str9 = "select count(*) from "+ catch_training_table +" where is_try_logged=1 and is_catch_logged =0"    
select_cursor.execute(str9)
data9 = select_cursor.fetchall()
for d in data9:
    logged_try_non_logged_catch= d[0]   

print "ltlc=", logged_try_logged_catch, " ltnlc=", logged_try_non_logged_catch
print "ltlc %=", (logged_try_logged_catch*100/logged_catch_count), "   ltnlc %=", (logged_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result5: % of catch blocks having previous catch block Vs. logged and Non-logged catch
"""
previous_catch_logged_catch=0
previous_catch_non_logged_catch=0
str10 = "select count(*) from "+ catch_training_table +" where have_previous_catches=1 and  is_catch_logged =1"    

select_cursor.execute(str10)
data10 = select_cursor.fetchall()
for d in data10:
    previous_catch_logged_catch= d[0]
    
str11 = "select count(*) from "+ catch_training_table +" where have_previous_catches=1 and is_catch_logged =0"    
select_cursor.execute(str11)
data11 = select_cursor.fetchall()
for d in data11:
    previous_catch_non_logged_catch= d[0]   

print "CBPCB=", previous_catch_logged_catch, " non logged=", previous_catch_non_logged_catch
print "CBPCB %=", (previous_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (previous_catch_non_logged_catch*100/non_logged_catch_count)   


"""
@Result6: % of catch blocks having previous catch and previous catches are logged Vs. logged and Non-logged catch
"""
logged_previous_catch_logged_catch=0
logged_previous_catch_non_logged_catch=0
str12 = "select count(*) from "+ catch_training_table +" where have_previous_catches=1 and previous_catches_logged=1 and  is_catch_logged =1"    

select_cursor.execute(str12)
data12 = select_cursor.fetchall()
for d in data12:
    logged_previous_catch_logged_catch= d[0]
    
str13 = "select count(*) from "+ catch_training_table +" where have_previous_catches=1 and previous_catches_logged=1 and is_catch_logged =0"    
select_cursor.execute(str13)
data13 = select_cursor.fetchall()
for d in data13:
    logged_previous_catch_non_logged_catch= d[0]   

print "CBPLCB=", logged_previous_catch_logged_catch, " non logged=", logged_previous_catch_non_logged_catch
print "CBPCB %=", (logged_previous_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (logged_previous_catch_non_logged_catch*100/non_logged_catch_count)   

"""
@Result7: % of catch blocks having return in try block Vs. logged and Non-logged catch
"""
return_in_try_logged_catch=0
reutun_in_try_non_logged_catch=0
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

print "TBR=", return_in_try_logged_catch, " non logged=", return_in_try_non_logged_catch
print "TBR %=", (return_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (return_in_try_non_logged_catch*100/non_logged_catch_count)   


"""
@Result8: % of catch blocks having return in Catch block Vs. logged and Non-logged catch
"""
return_in_catch_logged_catch=0
reutun_in_catch_non_logged_catch=0
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

print "CBR=", return_in_catch_logged_catch, " non logged=", return_in_catch_non_logged_catch
print "CBR %=", (return_in_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (return_in_catch_non_logged_catch*100/non_logged_catch_count)   


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
@Result10: % of catch blocks having "Throw/throws"  Try Block Vs. logged and Non-logged catch
"""
throw_throws_try_logged_catch=0
throw_throws_try_non_logged_catch=0

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

print "TTT=", throw_throws_try_logged_catch, " non logged=", throw_throws_try_non_logged_catch
print "TTT %=", (throw_throws_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (throw_throws_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result11: % of catch blocks having "Throw/throws"  in catch Block Vs. logged and Non-logged catch
"""
throw_throws_catch_logged_catch=0
throw_throws_catch_non_logged_catch=0

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

print "CTT=", throw_throws_catch_logged_catch, " non logged=", throw_throws_catch_non_logged_catch
print "CTT %=", (throw_throws_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (throw_throws_catch_non_logged_catch*100/non_logged_catch_count)   




"""
@Result12: % of Try blocks having Thread.Sleep  Block Vs. logged and Non-logged catch
"""
thread_sleep_try_logged_catch=0
thread_sleep_try_non_logged_catch=0

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

print "TTS=", thread_sleep_try_logged_catch, " non logged=", thread_sleep_try_non_logged_catch
print "TTS %=", (thread_sleep_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (thread_sleep_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result13: % of Catch blocks having InterruptedException Vs. logged and Non-logged catch
"""
interrupted_exp_logged_catch=0
interrupted_exp_non_logged_catch=0

str26 = "select count(*) from "+ catch_training_table +" where is_interrupted_exception=1 and  is_catch_logged =1"  
print "str26", str26 
select_cursor.execute(str26)
data26 = select_cursor.fetchall()
for d in data26:
    interrupted_exp_logged_catch= d[0]
    
str27 = "select count(*) from "+ catch_training_table +" where is_interrupted_exception=1 and is_catch_logged =0"    
select_cursor.execute(str27)
data27 = select_cursor.fetchall()
for d in data27:
    interrupted_exp_non_logged_catch= d[0]   

print "TTS=", interrupted_exp_logged_catch, " non logged=", interrupted_exp_non_logged_catch
print "TTS %=", (interrupted_exp_logged_catch*100/logged_catch_count), "   Non Logged %=", (interrupted_exp_non_logged_catch*100/non_logged_catch_count)   


"""
@Result14: % of Try Block = Thread.Sleep ++ Catch blocks =InterruptedException Vs. logged and Non-logged catch
"""
TTS_IE_logged_catch=0
TTS_IE_non_logged_catch=0

str28 = "select count(*) from "+ catch_training_table +" where  is_thread_sleep_try=1 and is_interrupted_exception=1 and  is_catch_logged =1"  
print "str", str28 
select_cursor.execute(str28)
data28 = select_cursor.fetchall()
for d in data28:
    TTS_IE_logged_catch= d[0]
    
str29 = "select count(*) from "+ catch_training_table +" where  is_thread_sleep_try=1 and is_interrupted_exception=1 and is_catch_logged =0"    
select_cursor.execute(str29)
data29 = select_cursor.fetchall()
for d in data29:
    TTS_IE_non_logged_catch= d[0]   

print "TTS + IE=",TTS_IE_logged_catch, " non logged=", TTS_IE_non_logged_catch
print "TTS + IE%=", (TTS_IE_logged_catch*100/logged_catch_count), "   Non Logged %=", (TTS_IE_non_logged_catch*100/non_logged_catch_count)   


"""
@Result15: % of Catch blocks object =ignore Vs. logged and Non-logged catch
"""
ignore_logged_catch=0
ignore_non_logged_catch=0

str28 = "select count(*) from "+ catch_training_table +" where  is_catch_object_ignore=1 and  is_catch_logged =1"  
print "str", str28 
select_cursor.execute(str28)
data28 = select_cursor.fetchall()
for d in data28:
    ignore_logged_catch= d[0]
    
str29 = "select count(*) from "+ catch_training_table +" where  is_catch_object_ignore=1  and is_catch_logged =0"    
select_cursor.execute(str29)
data29 = select_cursor.fetchall()
for d in data29:
    ignore_non_logged_catch= d[0]   

print "COI=",ignore_logged_catch, " non logged=", ignore_non_logged_catch
print "COI%=", (ignore_logged_catch*100/logged_catch_count), "   Non Logged %=", (ignore_non_logged_catch*100/non_logged_catch_count)   


"""
@Result16: % of Catch blocks with IF  Vs. logged and Non-logged catch
"""
if_in_try_logged_catch=0
if_in_try_non_logged_catch=0

str30 = "select count(*) from "+ catch_training_table +" where  if_in_try=1 and  is_catch_logged =1"  
print "str", str30
select_cursor.execute(str30)
data30 = select_cursor.fetchall()
for d in data30:
    if_in_try_logged_catch= d[0]
    
str31 = "select count(*) from "+ catch_training_table +" where  if_in_try=1  and is_catch_logged =0"    
select_cursor.execute(str31)
data31 = select_cursor.fetchall()
for d in data31:
    if_in_try_non_logged_catch= d[0]   

print "TIF=",if_in_try_logged_catch, " non logged=", if_in_try_non_logged_catch
print "TIF%=", (if_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (if_in_try_non_logged_catch*100/non_logged_catch_count)   



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
@Result18: % of try blocks wuth Assert statement  Vs. logged and Non-logged catch
"""
assert_in_try_logged_catch=0
assert_in_try_non_logged_catch=0

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_in_try=1 and  is_catch_logged =1"  
print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    assert_in_try_logged_catch= d[0]
    
str33 = "select count(*) from "+ catch_training_table +" where  is_assert_in_try=1  and is_catch_logged =0"    
select_cursor.execute(str33)
data33 = select_cursor.fetchall()
for d in data33:
    assert_in_try_non_logged_catch= d[0]   

print "TBS=",assert_in_try_logged_catch, " non logged=", assert_in_try_non_logged_catch
print "TBS%=", (assert_in_try_logged_catch*100/logged_catch_count), "   Non Logged %=", (assert_in_try_non_logged_catch*100/non_logged_catch_count)   



"""
@Result19: % of CATCH blocks wuth Assert statement  Vs. logged and Non-logged catch
"""
assert_in_catch_logged_catch=0
assert_in_catch_non_logged_catch=0

str32 = "select count(*) from "+ catch_training_table +" where  is_assert_in_catch=1 and  is_catch_logged =1"  
print "str", str32
select_cursor.execute(str32)
data32 = select_cursor.fetchall()
for d in data32:
    assert_in_catch_logged_catch= d[0]
    
str33 = "select count(*) from "+ catch_training_table +" where  is_assert_in_catch=1  and is_catch_logged =0"    
select_cursor.execute(str33)
data33 = select_cursor.fetchall()
for d in data33:
    assert_in_catch_non_logged_catch= d[0]   

print "CBS=",assert_in_catch_logged_catch, " non logged=", assert_in_catch_non_logged_catch
print "CBS%=", (assert_in_catch_logged_catch*100/logged_catch_count), "   Non Logged %=", (assert_in_catch_non_logged_catch*100/non_logged_catch_count)   


"""
@Result: Ratio of the non logged and non logged catch blocks 
"""

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

show()