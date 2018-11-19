# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib.pyplot as plt


data = pd.read_csv("c.dat", header=None, delimiter=r"\s+")


x = data[0]
y = data[1]
xlist = []

ylist = []
# populate the lists with the contents of the columns read
for i in range(0,int(len(x))):
   xlist.append(float(x.iloc[i]))
   ylist.append(float(y.iloc[i]))    

f = open("out.dat", "w")


# add header required for pcm file
# NOTE: we've slowed down the sample rate
#       because at 44100 it plays back fast.
#       I don't know why it does this!
f.write("; Sample Rate "+str(11025)+"\n")
f.write("; Channels 1"+"\n")

fc=5
temp=0
new=[0]
alpha=0.5
for i in range(1,len(ylist)):
 temp=(1+alpha*(np.sin(2*np.pi*i*(float(fc)/11025))))
 new.append(temp*ylist[i])
 f.write(str(xlist[i])+"   "+str((new[i]))+"\n")  
    

f.close() 
