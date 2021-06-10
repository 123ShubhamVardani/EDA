#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sbn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv(r"E:\python\dataset\analysis\titanic.csv")
#df


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


plt.hist(df.Age,edgecolor='k')
plt.title("peoples in titanic")
plt.xlabel("Age")
plt.ylabel("No. of people")
plt.show()


# In[7]:


df.isnull()


# In[8]:


sbn.heatmap(df.isnull(),yticklabels=False)


# In[9]:


sbn.set_style('whitegrid')
sbn.countplot(x="Survived",data=df)


# In[10]:


sbn.set_style('whitegrid')
sbn.countplot(x="Survived",hue='gender',data=df,palette="tab10")


# In[11]:


sbn.set_style('whitegrid')
sbn.countplot(x="Survived",hue='Pclass',data=df,palette="rainbow")


# In[12]:


df[(df.SibSp==0) & (df.Parch==0) & (df.gender=='male') & df.Survived==1].shape


# In[ ]:




