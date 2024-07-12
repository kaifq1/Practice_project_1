#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[20]:


dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())


# In[21]:


def handleRate(value):
	value=str(value).split('/')
	value=value[0];
	return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[22]:


dataframe.info()


# In[34]:


N = 10
top_n_restaurants = dataframe.nlargest(N, 'votes')
plt.figure(figsize=(10, 6))
sns.barplot(x='votes', y='name', data=top_n_restaurants, palette='viridis')
plt.xlabel("Votes", c="blue", size=15)
plt.ylabel("Restaurant Name", c="blue", size=15)
plt.title(f"Top {N} Restaurants by Votes")
plt.show()


# In[23]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# In[31]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")


# In[24]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)


# In[25]:


max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print("Restaurant with the maximum votes:")
print(restaurant_with_max_votes)


# In[26]:


sns.countplot(x=dataframe['online_order'])


# In[32]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='votes', y='rate', data=dataframe, hue='online_order', palette='deep')
plt.xlabel("Votes", c="blue", size=15)
plt.ylabel("Rate", c="blue", size=15)
plt.title("Votes vs. Ratings")
plt.show()


# In[27]:


plt.hist(dataframe['rate'],bins=7)
plt.title("Ratings Distribution")
plt.show()


# In[33]:


avg_rating_by_type = dataframe.groupby('listed_in(type)')['rate'].mean().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_by_type.values, y=avg_rating_by_type.index, palette='coolwarm')
plt.xlabel("Average Rating", c="blue", size=15)
plt.ylabel("Type of Restaurant", c="blue", size=15)
plt.title("Average Rating by Restaurant Type")
plt.show()


# In[28]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# In[29]:


plt.figure(figsize = (10,10))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe)


# In[30]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()


# In[35]:


plt.figure(figsize=(10, 8))
corr_matrix = dataframe.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Matrix")
plt.show()


# Dining restaurants mainly accept orders in person, while cafes primarily handle orders online. This indicates that customers prefer to place orders face-to-face at restaurants, but opt for online ordering at cafes.
# 
