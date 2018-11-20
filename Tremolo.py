# -*- coding: utf-8 -*-
#program: Tremolo.py
#author: Maulik Rajpara
#course: CS 827
#date: 2018/11/19 
#assignment #3
#Description : This program read .pcm audio file and genrate .pcm file of audio with Tremolo 
#              effect.
#--------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

# read audio file from given locaiton
data = pd.read_csv("c.dat", header=None, delimiter=r"\s+")

#storing data into varibles
x = data[0]
y = data[1]
xlist = []

ylist = []
# populate the lists with the contents of the columns read
for i in range(0,int(len(x))):
   xlist.append(float(x.iloc[i]))
   ylist.append(float(y.iloc[i]))    

f = open("out.dat", "w")  #creating output file


# add header required for pcm file

f.write("; Sample Rate "+str(11025)+"\n")  #add sample rate as per audio file 
f.write("; Channels 1"+"\n")

fc=5   # this variable Controls the speed of the oscillation; use higher frequencies for faster oscillation.
temp=0
new=[0]
alpha=0.5  # Sets the depth of tremolo. 

# applying tremolo formula to every sample and storing them in output file
for i in range(1,len(ylist)):
 temp=(1+alpha*(np.sin(2*np.pi*i*(float(fc)/11025))))
 new.append(temp*ylist[i])
 f.write(str(xlist[i])+"   "+str((new[i]))+"\n")   
    

f.close()  # file closing.
