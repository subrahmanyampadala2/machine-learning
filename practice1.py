#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Linear regression
#dummy variables
#onehotencoder
#train test split


# In[2]:


import os 
import pandas as pd


# In[3]:


os.chdir(r'C:\Users\SUBRAHMANYAM\OneDrive\Desktop\fresh project')


# In[4]:


os.listdir()


# In[5]:


df=pd.read_excel('Book1.xlsx')


# In[6]:


df.head()


# In[7]:


#creating dummies using pandas


# In[8]:


df1=pd.get_dummies(df['area'])


# In[9]:


df1.head()


# In[10]:


df2=pd.concat([df,df1],axis='columns')


# In[11]:


df2.head()


# In[12]:


df3=df2.drop(['area','z'],axis='columns')


# In[13]:


df3.head()


# In[14]:


from sklearn.linear_model import LinearRegression


# In[15]:


model=LinearRegression()


# In[16]:


x=df3.drop(['price'],axis='columns')


# In[17]:


y=df3['price']


# In[18]:


x


# In[19]:


y


# In[20]:


model.fit(x,y)


# In[21]:


model.coef_


# In[22]:


model.intercept_


# In[23]:


model.predict([[1500,1,0]])


# In[24]:


model.score(x,y)


# In[25]:


#using label encoder and onehotencoder


# In[26]:


df5=df.copy()


# In[27]:


df5.head()


# In[28]:


from sklearn.preprocessing import LabelEncoder


# In[29]:


le=LabelEncoder()


# In[30]:


df5['area']=le.fit_transform(df5['area'])


# In[31]:


df5.head()


# In[32]:


X=df5[['area','size']].values
X


# In[33]:


y=df['price']
y


# In[34]:


from sklearn.preprocessing import OneHotEncoder


# In[35]:


ohe=OneHotEncoder()


# In[36]:


x=ohe.fit_transform(df5[['area']]).toarray()


# In[37]:


x


# In[39]:


xx=['x','y','z']


# In[40]:


xx


# In[41]:


df6=pd.DataFrame(x,columns=xx)


# In[42]:


df6['size']=df5['size']


# In[43]:


x=df6
x=x.drop(['x'],axis='columns')
x


# In[44]:


y


# In[45]:


from sklearn.linear_model import LinearRegression


# In[46]:


le=LinearRegression()


# In[47]:


le.fit(x,y)


# In[48]:


le.predict([[0,0,500]])


# In[49]:


le.score(x,y)


# In[54]:


#train test split


# In[55]:


from sklearn.model_selection import train_test_split


# In[76]:


X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=0.1)


# In[77]:


le.fit(X_train,y_train)


# In[78]:


le.predict([[0,0,500]])


# In[79]:


le.score(X_train,y_train)


# In[ ]:





# In[ ]:




