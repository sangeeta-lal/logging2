
import MySQLdb
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

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
count=0

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()

with open('Book1.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([' ']+ ['debug1','error1','warn1','info1','trace1','fatal1'])
    
#====================Graph5==============================#
#==================heatMap================================#
    total_log_lines=0
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
        count=count+1
            
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
        if (info_count + error_count+trace_count +debug_count +warn_count +fatal_count) >=5:
            spamwriter.writerow([method_name+((str)(count)),debug_count,error_count,warn_count,info_count,trace_count,fatal_count])        
            
df = pd.read_csv('Book1.csv', index_col=0)
print "df=", (df)
# plotting
# ===Working but not used in the paper=== rather next graph is used====#
fig,ax = plt.subplots()
ax.matshow(df.mask(df.isin(df.info1)!=1), cmap=cm.Reds, aspect='auto') # You can change the colormap here
ax.matshow(df.mask(df.isin(df.trace1)!=1), cmap=cm.Reds,aspect='auto')
ax.matshow(df.mask(df.isin(df.warn1)!=1), cmap=cm.Reds, aspect='auto')
ax.matshow(df.mask(df.isin(df.fatal1)!=1), cmap=cm.Reds, aspect='auto')
ax.matshow(df.mask(df.isin(df.debug1)!=1), cmap=cm.Reds,aspect='auto')
ax.matshow(df.mask(df.isin(df.error1)!=1), cmap=cm.Reds,aspect='auto')
plt.xticks(range(6), df.columns)
plt.yticks(range(70), df.index)
plt.show()   

#=================================Following graph is used in the paper================#
import pylab as plt
import numpy as np

fn = "Book2.txt"
with open(fn, "r") as f:
    labels = f.readline().rstrip("\n").split(',')[1:]
data = np.loadtxt("Book2.txt", skiprows=1, delimiter=',', converters={0:lambda x: 0})
print "data=",data
print "data hmm=", type(data)
plot_data = np.ma.masked_equal(data[:,1:], 0)
#plt.subplots_adjust(left=0.1, bottom=0.15, right=0.99, top=0.95)

plt.imshow(plot_data, cmap=plt.cm.get_cmap("Reds"), interpolation="nearest", aspect = "auto")
plt.xticks(range(len(labels)), labels, rotation=90, va="top", ha="center", fontsize=18)
plt.yticks(fontsize=18)
cbar = plt.colorbar()


plt.show()