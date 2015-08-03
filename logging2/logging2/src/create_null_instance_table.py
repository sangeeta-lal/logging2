
#======================= Create New Tbale ======================#
#============Deatiled Catch Analysis============================#

import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import csv
import re

"""
#This file is used to creats tables where if condition either checks "null or instance of"
"""
project = "tomcat_"
#project="cloudstack_"

"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging_level"
file_path = "E:\\Sangeeta\\Research\\logging\\result"
"""
port=3306
user="root"
password="123"
database="logging_level"
file_path = "D:\\Research\\logging\\result"
#"""
#unique_if_table = project+"unique_if_feature"
unique_if_table = project+"if_train"
null_instance_table = project+"if_only_null_instance"

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()
temp_cursor =db1.cursor()

## Insert InstanceOf
instanceOf_str = "select expr, level from "+unique_if_table+" where expr!=\'\' and expr like \'%instanceof%\'"
select_cursor.execute(instanceOf_str)
temp_data = select_cursor.fetchall()
id = 0
for temp in temp_data:
    expr = temp[0]
    level = temp[1]
    if not level:
         id = id+1
         insert_str = "insert into "+ null_instance_table+" values(\'"+expr+"\',\'"+level+"\',\'instanceof\',"+(str)(id)+")"
         temp_cursor.execute(insert_str)
         
    else:
         level_array =level.strip().split(" ")
         for l in level_array:
             id =id+1
             insert_str = "insert into "+ null_instance_table+" values(\'"+expr+"\',\'"+l+"\',\'instanceof\',"+(str)(id)+")"
             temp_cursor.execute(insert_str)

##Insert Null
instanceOf_str = "select expr, level from "+unique_if_table+" where expr!=\'\' "
select_cursor.execute(instanceOf_str)
temp_data = select_cursor.fetchall()

for temp in temp_data:
    expr = temp[0]
    level = temp[1]
    if  re.search(r'=\s*null', expr):
        if not level:
            id = id+1
            insert_str = "insert into "+ null_instance_table+" values(\'"+expr+"\',\'"+level+"\',\'null\',"+(str)(id)+")"
            temp_cursor.execute(insert_str)
         
        else:
             level_array =level.strip().split(" ")
             for l in level_array:
                 id =id+1
                 insert_str = "insert into "+ null_instance_table+" values(\'"+expr+"\',\'"+l+"\',\'null\',"+(str)(id)+")"
                 temp_cursor.execute(insert_str)
                          
db1.commit()      