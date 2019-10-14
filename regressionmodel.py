#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[3]:


df['gender_val'] = df['gender'].apply(gen_to_num)
df.tail()


# In[ ]:


import statsmodels.formula.api as sm
result = sm.ols(formula= 'grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()


# In[6]:


import statsmodels.formula.api as sm
result = sm.ols(formula= 'grade ~ exercise + hours', data=df).fit()
result.summary()


# In[ ]:




