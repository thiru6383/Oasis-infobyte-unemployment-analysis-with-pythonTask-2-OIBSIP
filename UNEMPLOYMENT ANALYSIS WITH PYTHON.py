#!/usr/bin/env python
# coding: utf-8

# # UNEMPLOYMENT ANALYSIS WITH PYTHON:
# (Task-2)

# # Unemployment in India

# In[1]:


#importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly .express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#uploding the data
data_set1=pd.read_csv(r"C:\Users\HP\OneDrive\Documents\oasis infobytes\Unemployment in India.csv")


# In[3]:


data_set1.head()


# In[4]:


data_set1.tail()


# In[5]:


data_set1.shape


# In[6]:


data_set1.describe()


# In[7]:


data_set1.info()


# In[ ]:





# In[ ]:





# # Data cleaning and Modifiying

# In[8]:


data_set1.isnull().sum() #finding the missing value


# In[9]:


data_set1.isnull().sum().sum() #Total missing values


# In[10]:


data_set=data_set1.fillna(method='pad' ) #filling the null values with the previous value
data_set


# In[11]:


data_set.isnull().sum()


# In[12]:


print(data_set.columns.tolist())


# In[ ]:





# In[ ]:





# # Data Analysis Part

# In[13]:


plt.figure(figsize=(20,10))  #Unemployment rate in india
sns.lineplot(data=data_set,x=' Date',y=' Estimated Unemployment Rate (%)',color='blue')
plt.title("Unemployment rate in india")


# In[14]:


sns.barplot(data=data_set,x=' Estimated Unemployment Rate (%)',y='Region',color='blue')


# In[15]:


sns.barplot(data=data_set,x='Area',y=' Estimated Unemployment Rate (%)',color='yellow')


# In[16]:


plt.figure(figsize=(25,30))
data_set.columns=['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'Area']
plt.title("Unemployment in India Rural and Urban Area")
sns.histplot(x=' Estimated Unemployment Rate (%)',hue='Region',data=data_set1)
plt.show()


# In[17]:


plt.figure(figsize=(30,25))
data_set.columns=['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'Area']
plt.title("Unemployment in India Rural and Urban Area")
sns.histplot(x='Region',hue='Area',data=data_set1)
plt.show()


# In[18]:


sns.heatmap(data_set.corr(),annot=True)


# In[ ]:





# In[ ]:





# In[19]:


################################################################################################################################################################################################################


# In[ ]:





# In[ ]:





# # Unemployment Rate upto 1/11/2020(November)

# In[20]:


data_set2=pd.read_csv(r"C:\Users\HP\OneDrive\Documents\oasis infobytes\Unemployment_Rate_upto_11_2020.csv")


# In[21]:


data_set2.head()


# In[22]:


data_set2.tail()


# In[23]:


print(data_set2.columns.tolist())


# In[24]:


data_set2.isnull().sum()


# In[ ]:





# In[ ]:





# # Data Analysis Part

# In[25]:


#Unemployment rate in india
plt.figure(figsize=(20,10)) 
sns.lineplot(data=data_set2,x=' Date',y=' Estimated Unemployment Rate (%)',color='red')


# In[26]:


#Unemployment rate in india

sns.barplot(data=data_set1,x=' Estimated Unemployment Rate (%)',y='Region',color='orange')


# In[27]:


sns.barplot(data=data_set2,x=' Estimated Unemployment Rate (%)',y='Region.1',color='gray')


# In[28]:


plt.figure(figsize=(20,10)) 
data_set2.columns=['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'Region.1', 'longitude', 'latitude']
plt.title("Unemployment in India Rural and Urban Area")
sns.histplot(x=' Estimated Unemployment Rate (%)',hue='Region.1',data=data_set2)
plt.show()


# In[29]:


plt.figure(figsize=(20,10)) 
data_set2.columns=['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'Region.1', 'longitude', 'latitude']
plt.title("Unemployment in India Rural and Urban Area")
sns.histplot(x=' Estimated Unemployment Rate (%)',hue='Region',data=data_set2)
plt.show()


# In[30]:


sns.heatmap(data_set2.corr(),annot=True)


# In[31]:


unemployment=data_set2[['Region', ' Date', ' Frequency', ' Estimated Unemployment Rate (%)', ' Estimated Employed', ' Estimated Labour Participation Rate (%)', 'Region.1', 'longitude', 'latitude']]
figure=px.sunburst(unemployment,path=['Region',' Estimated Unemployment Rate (%)'],
                  
                  width=1000,height=1000,color_continuous_scale="RdV1Gn"
                 )
figure.show()


# In[32]:


#Thanking You...


#                                                                                                  - Thiruvalluvan G

# In[ ]:




