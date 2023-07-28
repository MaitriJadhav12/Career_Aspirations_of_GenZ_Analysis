#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
import plotly.express as px #Plotly Express is a high-level data visualization library built on top of Plotly, which is used to create interactive and visually appealing plots and charts.
import plotly.graph_objects as go #Plotly graph_objects is a lower-level interface compared to Plotly Express and allows for more fine-grained control over the appearance and customization of plots and charts.


# In[5]:


data=pd.read_csv("Your Career Aspirations of GenZ.csv")
print(data.head())   #gives the starting 5 values present


# In[7]:


print(data.columns)


# In[16]:


country = data['Your Current Country.'].value_counts()
label = country.index
count = country.values
colors=['green','red']
fig = go.Figure(data=[go.Pie(labels=label, values=count)])
fig.update_layout(title_text='CURRENT COUNTRY')
fig.update_traces(hoverinfo='label+value',textinfo='percent',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[17]:


# So 98.3% of the people who submitted answers to the survey live in India


# In[18]:


question1 = data["Which of the below factors influence the most about your career aspirations ?"].value_counts()
label = question1.index
counts = question1.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Factors influencing career aspirations')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[19]:


# 33.6% of the Genz are influenced by parents
# 24.3% are influenced by the people who have changed the world for the better
# 16.6% are influenced by people from their circle but not family
# 15.7% are influenced by influencers having successful careers


# In[20]:


question2 = "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
question2 = data[question2].value_counts()
label = question2.index
counts = question2.values
colors = ['black','white']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Will you pursue a Higher Education outside India with your investment?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[21]:


# 46.8% believe in pursuing higher education outside India with their self-earned income
# 27.7% don’t want to pursue higher education outside of India
# 25.5% can only pursue higher education outside India if someone can bare that cost


# In[22]:


question3 = "How likely is that you will work for one employer for 3 years or more ?"
question3 = data[question3].value_counts()
label = question3.index
counts = question3.values
colors = ['pink','purple']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely is that you will work for one employer for 3 years or more?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[23]:


# 59.1% find it hard, but they can only if the company is good
# 33.6% don’t have any problem working for three years or more
# only 7.23% say that they will don’t work for so long by any chance


# In[24]:


question4 = "Would you work for a company whose mission is not clearly defined and publicly posted."
question4 = data[question4].value_counts()
label = question4.index
counts = question4.values
colors = ['brown','orange']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Would you work for a company whose mission is not clearly defined and publicly posted?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[60]:


question4 = "Would you work for a company whose mission is not clearly defined and publicly posted."
question4 = data[question4].value_counts()
label = question4.index
counts = question4.values

plt.bar(label, counts, width=custom_width, color=custom_colors)
# Add labels and title
plt.xlabel('LABELS')
plt.ylabel('COUNTS')
plt.title('Would you work for a company whose mission is not clearly defined and publicly posted.')
custom_width = 0.6
custom_colors = ['red', 'yellow']
# Show the plot
plt.show()


# In[26]:


question5 = "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"
question5 = data[question5].value_counts()
label = question5.index
counts = question5.values
colors = ['red','orange']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely would you work for a company whose mission is misaligned with their actions?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[27]:


# 67.2% say no
# 32.8% don’t have any problem with it


# In[28]:


question6 = "How likely would you work for a company whose mission is not bringing social impact ?"
question6 = data[question6].value_counts()
label = question6.index
counts = question6.values
colors = ['green','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='How likely would you work for a company whose mission is not bringing social impact?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[29]:


question7 = "What is the most preferred working environment for you."
question7 = data[question7].value_counts()
label = question7.index
counts = question7.values
colors = ['white','yellow']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='What is the most preferred working environment for you?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[32]:


question8 = "Which of the below Employers would you work with."
question8 = data[question8].value_counts()
label = question8.index
counts = question8.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Which of the below Employers would you work with?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[37]:


# 48.1% of Genz wants employers who push their limits by enabling a learning environment and reward them at the end
# 31.9% want employers who appreciate a learning environment
# 15.3% want an employer who enables a rewarding environment


# In[55]:


question9 = "Which type of learning environment that you are most likely to work in ?"
question9 = data[question9].value_counts()
label = question9.index
counts = question9.values
colors = ['blue','black']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Which type of learning environment that you are most likely to work in?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[56]:


question10 = "What type of Manager would you work without looking into your watch ?"
question10 = data[question10].value_counts()
label = question10.index
counts = question10.values
colors = ['gold','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='What type of Manager would you work without looking into your watch?')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[61]:


# So this is how we can analyze a career aspirations survey using Python. A Career Aspirations Survey gathers information about the goals and aspirations of people in their careers. It includes questions based on long-term goals, preferred work environment, interests, and values. I hope you liked this article on Career Aspirations Survey analysis using Python.


# In[ ]:




