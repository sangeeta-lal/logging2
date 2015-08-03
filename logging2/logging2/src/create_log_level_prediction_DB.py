
"""================================================================================
This file will create database for predicting log levels
Following trace levels are covered: (Trace, debug, info, warn, error, fatal)

=================================================================================="""
import os
import re

#Server
"""
file_path =

"""
#rootdir="D:\\Research\\Logging\\dataset\\tomcat-8.0.9"
rootdir="D:\\Research\\Logging\\dataset\\temp"
dbname = "logging_level"
password= "123"

#"""
java_file_count = 0
total_file_count=0
#output_file = open(output_file_path,'w')
most_recent_class = ''



def get_class(fin, file_path):
    keyword=  " class "
    for line in fin:
        if keyword in line:
            break;
    class_name = (line.split("class")[1]).split(" ")[1]
    print "class name=", class_name 
    return class_name   

def get_most_recent_fun(line, most_recent_fun):
    result = re.findall('\\b public|private\\b', line, flags=re.IGNORECASE)
    if len(result)>0:
        most_recent_fun = "Hello"
    
    return most_recent_fun        
        
   
def extract_write_log(fin, file_path):
    #output_file.write('\n----------\n')
    #output_file.write(file_path)
    #output_file.write('\n----------\n')
    most_recent_class = get_class(fin, file_path)
    most_recent_fun = ''
    add_other_line = 0
    old_line=''
    for line in fin:
        line = line.strip()
        most_recent_fun = get_most_recent_fun(line,most_recent_fun)
        print "Most recent fun=",  most_recent_fun
        #line = "log.trace(Could not set threadCpuTimeEnabled to "
        log_present = 0
        if add_other_line==0: 
            if re.search(r'\.trace\(', line):
                print line
                log_present = 1
                #output_file.write(line)
            if re.search(r'\.debug\(', line):
                print line 
                log_present = 1
                #output_file.write(line)           
            if re.search(r'\.info\(', line):
                print line
                log_present = 1
                #output_file.write(line)
            if re.search(r'\.warn\(', line):
                print line
                log_present = 1
                #output_file.write(line)           
            if re.search(r'\.error\(', line):
                print line
                log_present = 1
                #output_file.write(line)
            if re.search(r'\.fatal\(', line):
                print line
                log_present = 1
                #output_file.write(line)  
            if log_present==1 and line[-1]==';':
                #output_file.write(line)
                split_and_write_log_lines(line, output_file)
                
            if log_present==1 and line[-1]!=';':
                add_other_line=1
                old_line=line
           
        else:
            old_line = old_line +' ' +line
            if line and line[-1]==';':
               #output_file.write(old_line+"he he\n")
               split_and_write_log_lines(old_line, output_file)
               old_line = ' '
               add_other_line=0
        #output_file.write('')      

def split_and_write_log_lines(line, output_file):
    lines = line.split(");")
    for l in lines:
        if l:
            if re.search(r'\.trace\(', l):
                output_file.write(l+");\n")
            if re.search(r'\.debug\(', l):
                output_file.write(l+");\n")           
            if re.search(r'\.info\(', l):
                output_file.write(l+");\n")
            if re.search(r'\.warn\(', l):
                output_file.write(l+");\n")           
            if re.search(r'\.error\(', l):
                output_file.write(l+");\n")
            if re.search(r'\.fatal\(', l):
                output_file.write(l+");\n")
            #output_file.write(l+");\n")

        
for root, subFolders, files in os.walk(rootdir):
    for file in files:
      total_file_count= total_file_count+1
      if file.endswith('.java'):
          java_file_count = java_file_count+1
          print "count=", java_file_count, "file", file
          with open(os.path.join(root, file), 'r') as fin:
              file_path = root+"\\"+file
              print "================="
              print file_path
              print "================="
              extract_write_log(fin, file_path)
              #for line in fin:
              #    print "lines=", line
