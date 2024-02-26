#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[44]:


df = pd.read_csv('all_data.csv')
df.rename(columns={'Life expectancy at birth (years)':'Life_expectancy'}, inplace=True)
print(data.head(7))
Group = df.groupby('Country')['Life_expectancy'].agg('mean')
print(Group)


# In[45]:


group = df.groupby(['Year', 'Country'])['Life_expectancy'].mean().unstack()

group.plot(kind='line', figsize=(9, 4))
plt.ylabel('Life expectancy')
plt.title('Average life expectancy by country')
plt.legend(loc='best')


# In[46]:


group = df.groupby(['Year', 'Country'])['GDP'].mean().unstack()

group.plot(kind='line', figsize=(9, 4))
plt.ylabel('GDP')
plt.title('GDP per country')
plt.legend(loc='best')


# In[50]:


sns.scatterplot(x = 'Life_expectancy', y = 'GDP', hue = 'Country', data = df)
plt.show()
plt.clf()


# In[52]:


sns.histplot(x='Life_expectancy', data=df)
plt.xlabel('Life expectancy')
plt.show()
plt.clf()


# In[ ]:




