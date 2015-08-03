
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