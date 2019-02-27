#!/usr/bin/env python
# coding: utf-8

# In[143]:


#tip data analysis 


# In[144]:


import pandas as pd
import matplotlib.pyplot as plt


# In[145]:


tipdata = pd.read_csv("tips.csv")


# In[146]:


tipdata.columns


# In[147]:


tipdata


# In[148]:


tipdata.info()


# In[149]:


tipdata.describe()


# In[150]:


male = tipdata[tipdata.sex=='Male']
maletip = male.tip
maletip


# In[151]:


male.describe()


# In[152]:


malecount=int(male.describe().tip.iloc[0])
malecount


# In[153]:


female = tipdata[tipdata.sex=='Female']
femaletip = female.tip
femaletip


# In[154]:


female.describe()


# In[155]:


femalecount=int(female.describe().tip.iloc[0])
femalecount


# In[156]:


plt.plot(range(malecount),male.tip,"p")
plt.plot(range(femalecount),female.tip,'p')
plt.grid(True)


# In[157]:


print(max(maletip))
print(max(femaletip)) 


# In[158]:


tipsun=tipdata[tipdata['day']=="Sun"]
tipthus=tipdata[tipdata['day']=="Thur"]
tipfri=tipdata[tipdata['day']=="Fri"]
tipsat=tipdata[tipdata['day']=="Sat"]


# In[159]:


tipdata["day"].describe()


# In[160]:


#count of no of customer
tipsunc=tipsun.tip.count()
tipthusc=tipthus.tip.count()
tipfric=tipfri.tip.count()
tipsatc=tipsat.tip.count()


# In[161]:


#pplot of number of customer
plt.plot([tipthusc,tipfric,tipsatc,tipsunc])
plt.xticks([0.0,1.0,2.0,3.0],["Thursday",'Friday',"Saturday","Sunday"])
plt.grid(True)
plt.show()


# In[162]:


#mean tip per day
avgthustip=round((tipthus['tip']).mean(),2)
avgfritip=round((tipfri['tip']).mean(),2)
avgsattip=round((tipsat['tip']).mean(),2)
avgsuntip=round((tipsun['tip']).mean(),2)


# In[163]:


#plot mean tip per day
plt.plot([avgthustip,avgfritip,avgsattip,avgsuntip])
plt.xticks([0.0,1.0,2.0,3.0],["Thursday",'Friday',"Saturday","Sunday"])
plt.grid(True)
plt.show()


# In[164]:


#time and tip relation
tipdata["time"].describe()


# In[165]:


timeD= tipdata[tipdata['time']=="Dinner"]
timeL = tipdata[tipdata['time']=="Lunch"]
timeL


# In[166]:


#tip in dinner
maxtimeD=timeD.tip.max()
mintimeD=timeD.tip.min()
#tip in lunch
maxtimeL=timeL.tip.max()
mintimeL=timeL.tip.min()


# In[167]:


#average tip in dinner
avgtimeD=timeD.tip.mean()
#average tip in lunch
avgtimeL = timeL.tip.mean()


# In[168]:


plt.plot([maxtimeD,mintimeD,maxtimeL,mintimeL])
plt.xticks([0.0,1.0,2.0,3.0],["Dinner.max","Dinner.min","Lunch.max","Lunch.min"])
plt.grid(True)
plt.show()


# In[169]:


smokertip=tipdata[tipdata['smoker']=="Yes"]
nosmokertip=tipdata[tipdata['smoker']=='No']


# In[170]:


smokertip.tip.mean()


# In[171]:


nosmokertip.tip.mean()


# In[ ]:




