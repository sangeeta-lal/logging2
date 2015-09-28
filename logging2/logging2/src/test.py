#!/usr/bin/python

#
# Example boxplot code
#

from pylab import *
import utill 
from nltk.stem.porter import PorterStemmer

name ="MyNameIs sANGeEETs ands Iam NotATerroristes"
name = utill.camel_case_convert(name)
name=  utill.stem_it(name)
print "name= ", name



temp   = list()
temp.append("hello")
temp.append(" life")

temp2 = list()
temp2.append(" I am ")
temp2.append("fine")

temp3 =  temp + temp2
print" temp3=", temp3


print "abc"
# fake up some data
spread= rand(50) * 100
center = ones(25) * 50
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100
data =concatenate((spread, center, flier_high, flier_low), 0)

# basic plot
#data=[1,2,3,4,5,6,7,8,9,10,1,2,3,2,3,4,3,4,5,3,4,5,2,3,4,5,2,3,45]
print "data=",data
boxplot(data)


# notched plot
figure()
boxplot(data,1)

# change outlier point symbols
figure()
boxplot(data,0,'gD')

# don't show outlier points
figure()
boxplot(data,0,'')

# horizontal boxes
figure()
boxplot(data,0,'rs',0)

# change whisker length
figure()
boxplot(data,0,'rs',0,0.75)

# fake up some more data
spread= rand(50) * 100
center = ones(25) * 40
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100
d2 = concatenate( (spread, center, flier_high, flier_low), 0 )
data.shape = (-1, 1)
d2.shape = (-1, 1)
#data = concatenate( (data, d2), 1 )
# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [data, d2, d2[::2,0]]
# multiple box plots on one figure
figure()
boxplot(data)

#show()

import re

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s1= re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    s2 = s1.split("_")
    final= " "
    for s in s2:
        final = final+" "+s
    final = final.strip()
    return final 
name= "HelooSan"
    
name = convert(name)
print "name=", name



import re




def clean(val):
   # val ="hello + remove a*b a<>b abc(10) int a[20] int b=10^10 int fun(){print hello c/d /*smd*/ //dfdn @override<?:?>};"
    val = re.sub(r"[\+\*%-/&|^=!]", " ", val)
    val = re.sub(r"[<>\{\}\(\)\[\]]", " ", val)
    val = re.sub(r"[@#$_\\\'\":;\.,\?0-9]", " ", val)
    val = re.sub(r" +"," ", val)
    return val

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s1= re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    s2 = s1.split("_")
    
    final= " "
    for s in s2:
        final = final+" "+s
    final = final.strip()
    return final    
    
def stem_it(val):
    #print "val=", val
    temp = " ".join(PorterStemmer().stem_word(word) for word in val.split(" "))
    #print "temp=", temp
    return temp

name='UserSangeeta'
s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
s1= re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
s2 = s1.split("_")
print "s2=", s2

import matplotlib.pyplot as plt
from numpy.random import normal
gaussian_numbers = [10,20,30,10,20,40, 90,100, 50]#normal(size=10)
x=[1,2,3]
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
#plt.show()

print"gaussian_numbers",gaussian_numbers

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from numpy.ma import masked_array
import numpy as np
from pandas import Series
from pandas.tseries.index import date_range
#from dataframe import DataFrame

#data = pd.read_clipboard() # just copied your example
#data = [[1,2,3],[2,3,4],[7,8,9],[11,12,0]]

#data = DataFrame({"fun":[1,2,3]},
 #                {"fun2":[3,1,2]},
 #                {"func3":[4,3,1]})
"""
rng = date_range('1/1/2000 00:00:00', '1/1/2000 00:8:00', freq='min')
data = Series(np.random.randn(3*3),index=rng)
print "data", data
# define masked arrays to mask all but the given column
c1 = masked_array(data, mask=(np.ones_like(data)*(data.values[0]!=data.values[0][0]))) 
c2 = masked_array(data, mask=(np.ones_like(data)*(data[0]!=data[0][1])))
c3 = masked_array(data, mask=(np.ones_like(data)*(data[0]!=data[0][2])))

fig,ax = plt.subplots()
ax.matshow(c1,cmap=cm.Reds) # You can change the colormap here
ax.matshow(c2,cmap=cm.Greens)
ax.matshow(c3,cmap=cm.Blues)
#plt.xticks(range(3), data)





#plt.yticks(range(4), data)
#plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm

#px = [[1,2,3],[3,4,5],[5,6,7]]

#px2 = px.reshape((-1,3))
#df = pd.DataFrame({'R':px2[:,0],'G':px2[:,1],'B':px2[:,2]})
# data loading
df = pd.read_csv('Book1.csv', index_col=0)
print (df)
# plotting
fig,ax = plt.subplots()
ax.matshow(df.mask(df.isin(df.att1)!=1), cmap=cm.Reds) # You can change the colormap here
ax.matshow(df.mask(df.isin(df.att2)!=1), cmap=cm.Greens)
ax.matshow(df.mask(df.isin(df.att3)!=1), cmap=cm.Blues)
plt.xticks(range(3), df.columns)
plt.yticks(range(12), df.index)
plt.show()