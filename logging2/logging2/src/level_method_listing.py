

"""
This file is used to create method 
"""

import MySQLdb

#"""
port=3307
user="sangeetal"
password="sangeetal"
database="apsec2014"
table = "cloudstack_level_feature"
rootdir="E:\\Sangeeta\\Research\\Logging\\result\\cloudstack_method_"
 
#table = "tomcat_level_feature"
#rootdir="E:\\Sangeeta\\Research\\Logging\\result\\tomcat_method_"


"""
rootdir="D:\\Research\\Logging\\result\\tomcat_method_"
port=3306
user="root"
password="123"
database="logging_level"
table = "cloudstack_level_feature"
rootdir="D:\\Research\\Logging\\result\\cloudstack_method_"
 
#table = "tomcat_level_feature"
#rootdir="D:\\Research\\Logging\\result\\tomcat_method_"

#"""

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()
info_file = open(rootdir+"info.txt",'w')
warn_file = open(rootdir+"warn.txt",'w')
error_file = open(rootdir+"error.txt",'w')
debug_file = open(rootdir+"debug.txt",'w')
fatal_file = open(rootdir+"fatal.txt",'w')
trace_file = open(rootdir+"trace.txt",'w')

select_str = "select method, method_content, level from " +table+ " where level!=\"\""
select_cursor.execute(select_str)
data = select_cursor.fetchall()
for d in data:
    method_name = d[0].strip()
    method_content =d[1].strip()
    method_size = len(' '.join(method_content.split()))  
    #method_body_sizes.append(method_size)
    
    info_flag=0
    error_flag=0
    trace_flag=0
    debug_flag=0
    warn_flag=0
    fatal_flag=0
    level= d[2].strip() 
    print "level", level
    level=' '.join(level.split())
    level_array=level.split(" ")
    
    for l in level_array:
        if l == "info":
            info_flag=1
            info_file.write(method_name+"()\n")
            info_file.write(method_content+" \n\n==================================\n")
        elif l=="error":
            error_flag=1
            error_file.write(method_content+" \n\n====================================\n")
        elif l=="trace":
            trace_flag=1
            trace_file.write(method_name+"()\n")
            trace_file.write(method_content+" \n\n==================================\n")
        elif l=="debug":
            debug_flag=1
            debug_file.write(method_name+"()\n")
            debug_file.write(method_content+" \n\n==================================\n")
        elif l=="warn":
            warn_flag=1
            warn_file.write(method_name+"()\n")
            warn_file.write(method_content+" \n\n==================================\n")
        elif l=="fatal":
            fatal_flag=1
            fatal_file.write(method_name+"()\n")
            fatal_file.write(method_content+" \n\n==================================\n")
    
 
info_file.close()
warn_file.close()
error_file.close()
debug_file.close()
fatal_file.close()
trace_file.close()  