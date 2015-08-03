import os
import re

#"""
rootdir = 'D:\\Research\\Logging\\dataset\\tomcat-8.0.9'
output_file_path = "D:\\Research\\Logging\\result\\tomcat-log.txt"

#rootdir = 'D:\\Research\\Logging\\dataset\\openoffice-4.1.0'
#output_file_path = "D:\\Research\\Logging\\result\\openoffice-log.txt"

#rootdir = 'D:\\Research\\Logging\\dataset\\jackrabbit-2.8.0'
#output_file_path = "D:\\Research\\Logging\\result\\jackrabbit-log.txt"

#rootdir = 'D:\\Research\\Logging\\dataset\\geronimo-3.0.1'
#output_file_path = "D:\\Research\\Logging\\result\\geronimo-log.txt"

#rootdir = 'D:\\Research\\Logging\\dataset\\cloudstack-4.3.0'
#output_file_path = "D:\\Research\\Logging\\result\\cloudstack-log.txt"
"""
##Server##
#rootdir = 'E:\\Sangeeta\\Research\\Logging\\dataset\\tomcat-8.0.9'
#output_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\tomcat-log.txt"

#rootdir = 'E:\\Sangeeta\\Research\\Logging\\dataset\\openoffice-4.1.0'
#output_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\openoffice-log.txt"

#rootdir = 'E:\\Sangeeta\\Research\\Logging\\dataset\\jackrabbit-2.8.0'
#output_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\jackrabbit-log.txt"

#rootdir = 'E:\\Sangeeta\\Research\\Logging\\dataset\\geronimo-3.0.1'
#output_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\geronimo-log.txt"

#rootdir = 'E:\\Sangeeta\\Research\\Logging\\dataset\\cloudstack-4.3.0'
#output_file_path = "E:\\Sangeeta\\Research\\Logging\\result\\cloudstack-log.txt"
#"""

java_file_count = 0
total_file_count=0
output_file = open(output_file_path,'w')

def extract_write_log(fin, file_path):
    output_file.write('\n----------\n')
    output_file.write(file_path)
    output_file.write('\n----------\n')
    add_other_line = 0
    old_line=''
    for line in fin:
        line = line.strip()
        
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

print "root dir", rootdir
print "java file count=", java_file_count, "\n"
print "total file count=", total_file_count, "\n"

output_file.close()                     
"""
  if 'data.txt' in files:
      with open(os.path.join(root, 'data.txt'), 'r') as fin:
           for lines in fin:
               dosomething()
"""