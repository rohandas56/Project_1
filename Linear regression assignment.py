#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[2]:


data = pd.read_csv('Delivery_time.csv')


# In[3]:


data


# In[4]:


data=data[['Sorting Time','Delivery Time']]


# In[5]:


data


# # EDA(Exploratory Data Analysis

# In[6]:


print(data.head())


# In[7]:


print(data.info()) 


# In[8]:


print(data.describe())


# # Data Visualization

# In[9]:


z=np.arange(len(data))


# In[10]:


sns.scatterplot(data,x='Sorting Time',y='Delivery Time')


# In[11]:


sns.pairplot(data)
plt.show()


# ## Correlation Analysis 

# In[12]:


correlation = data.corr()
sns.heatmap(correlation, annot=True)
plt.title('Correlation Heatmap')
plt.show()


# # Feature Engineering

# In[13]:


x = data[['Sorting Time']]  
y = data[['Delivery Time']] 


# In[14]:


x


# In[15]:


y


# #Splitting the dataset into train and test sets

# In[16]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# In[17]:


x_train


# In[18]:


y_train


# In[19]:


x_test


# In[20]:


y_test


# # Model Building

# In[21]:


model = LinearRegression()
model.fit(x_train, y_train)


# # Model Testing

# In[22]:


y_pred_train = model.predict(x_train)
y_pred_test = model.predict(x_test)


# In[23]:


y_pred_train


# In[24]:


y_pred_test


# # Model Prediction

# In[26]:


new_sorting_time = [[4], [5],[7],[10]]
predicted_delivery_time = model.predict(new_sorting_time)
print('Predicted Delivery Time:', predicted_delivery_time)

