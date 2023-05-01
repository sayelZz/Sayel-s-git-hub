#!/usr/bin/env python
# coding: utf-8

# In[7]:


elements = [1,2,3,4,5]


# In[8]:


for i in elements:
    print(i)


# In[9]:


hungry = True
if hungry :
    print('Feed me')
else:
    print("I'm not hungry")


# In[10]:


loc = 'Bank'
if loc == 'Auto shop':
    print('cars are cool')
else:
    print ('I do not know much')


# In[10]:


loc = 'game'
if loc == 'Auto shop':
    print('cars are cool')
elif loc == 'bank':
    print('money is cool$$')
elif loc == 'store':
    print('welcome to the store!')
else:
    print('I do not know much')
   


# In[18]:


name = 'Ronal'
if name == 'Milan':
    print('come to the school!')
elif name == 'Ruben':
    print('Have your food and come to class')
elif name == 'Kastup':
    print ('dont make meme')
else:
    print('you are not needed now!')
    


# In[19]:


#for loops


# In[22]:


my_iterable = [1,2,3,]
for happy in my_iterable:
    print(happy)


# In[3]:


mylist = [1,2,3,4,5,6,7,8,9]
for num in mylist:
    print('Thursday')


# In[4]:


mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)


# In[8]:


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num%2 == 0:
        print(num)
else:
    print(f'odd number :{num}')
    
    


# In[9]:


mystring = 'hello world'
for letter in mystring:
    print(letter)


# In[11]:


for letter in 'Medhavi':
    print('wassup')


# In[14]:


mylist =[(1,2),(3,4),(5,6),(7,8),(9,10)]
for b,a in mylist:
    print(a)
    #print(b)


# In[15]:


mylist=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for fv1,fv2,fv3 in mylist:
    print(fv2)
    print(fv3)
    print(fv1)


# In[20]:


d={'k1':1,'k2':2,'k3':3}
for key,value in d:
    print(value)


# In[ ]:




