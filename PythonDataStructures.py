#!/usr/bin/env python
# coding: utf-8

# # Reversing a Python String
# * With Accessing Characters from a string, we can also reverse them. 
# * We can Reverse a string by writing [::-1] and the string will be reversed.
# 
# This code reverses the string str2 and prints the result. Let's break it down step by step:
# 
# 
# str2[::-1]: In Python, when you use slicing with a negative step (-1 in this case), it reverses the sequence (string, list, etc.). So, str2[::-1] creates a new string that is a reversed version of str2.
# 
# Let's see how the reversal works:
# 
# The syntax for slicing in Python is start:stop:step.
# If start is not specified, it defaults to the beginning of the sequence.
# If stop is not specified, it defaults to the end of the sequence.
# If step is not specified, it defaults to 1.
# In our case, start and stop are not specified, which means the whole string will be considered. The step is -1, which means it will iterate over the string in reverse order, effectively reversing the string.
# 
# Here's how the slicing works kefile
# Copy code
# str2 = "growdataskills"
# str2[::-1]
# No start and stop specified, so it considers the entire string: "growdataskills"
# 
# step is -1, so it iterates in reverse order: "slliskatsadworg"
# 
# print(str2[::-1]): This line prints the result of the slicing operation, which is the reversed string "slliskatsadworg".
# 
# So, when you run this
# utput will be:
# 
# Copy code
# slliskatsadworg
# 

# In[1]:


str2 = "growdataskills"
print(str2[::-1])


# In[2]:


# Can not reassign 
t= "GrowDataSkills"
type(t)


# In[3]:


t[0] = "M"


# In[4]:


original_string = "Hello"
new_string = original_string + " World!"  # Concatenation creates a new string. 


# In[5]:


new_string


# In[6]:


original_string


# # in and not in
# 
# The in and not in operators in Python are used to check whether a particular element exists within a sequence (like a string, list, tuple, etc.). They return a Boolean value (True or False) based on whether the element is present in the sequence or not.

# In[7]:


my_string = " growdataskills"


# In[8]:


"grow" in my_string


# In[9]:


"world" in my_string


# In[10]:


"z" in my_string


# In[11]:


"Hellos" not in my_string


# # Python Tuple
# In Python, a tuple is an ordered and immutable collection of elements. It is similar to a list, but unlike lists, tuples cannot be changed after they are created. Tuples are represented using parentheses ( ) and can contain elements of different data types, such as numbers, strings, or even other tuples.

# In[15]:


#creating a tuple with an elements
emp_name = ("Dinesh" , "Nikhil" , "Kalyan" , "Kumar" , "Rohit")


# In[16]:


emp_name


# In[17]:


emp_name[0]


# In[19]:


emp_name[1:4]


# In[20]:


type(emp_name)


# In[21]:


mixed_Tuple = (1, "Fiziya" , 8.6, "# 21 Hubli" , True) 


# In[22]:


mixed_Tuple


# In[24]:


mixed_Tuple[-1]


# In[27]:


mixed_Tuple[1:4]  #Slicing


# In[30]:


mixed_Tuple[1] = "Kausar" # Tuple is immutable it cannot be changed 


# In[31]:


len(mixed_Tuple)


# In[37]:


tup1 = (1,2,3)
tup2 = (4,5,6)
tup1+tup2
tup1+tup2*


# In[40]:


tup1=(10,20,30,40,50)


# In[43]:


min(tup1)


# In[44]:


max(tup1)


# In[45]:


#tuple unpacking


# In[46]:


cordinates=(1,2,3) 


# In[47]:


a,b,c= cordinates


# In[48]:


a


# In[49]:


b


# In[50]:


c


# In[51]:


cordinates


# # Python Lists
# In Python, a list is an ordered and mutable collection of elements. Lists are one of the most versatile and widely used data structures in Python. They can hold elements of different data types, such as numbers, strings, or even other lists. Lists are represented using square brackets [ ].
# 

# In[52]:


# Creating a list with elements
numbers_list = [1, 2, 3, 4, 5]

numbers_list


# In[53]:


type(numbers_list)


# In[54]:


# Lists can also have elements of different data types
mixed_list = [1, 'hello', 3.14, True]

mixed_list


# In[55]:


type(mixed_list)


# # Accessing elements of a list:
# You can access elements of a list using indexing. The index starts from 0 for the first element, 1 for the second, and so on.

# In[57]:


l1= [1, 'hello', 3.14, True]


# In[58]:


l1[1]


# In[59]:


l1[-1]


# In[60]:


l1[1:3]


# # Modifying elements of a list:
# Lists are mutable, which means you can change their elements after they are created.

# In[61]:


l1= [1, 'hello', 3.14, True]
l1[0] = 'pear'

l1


# # Removing elements from a list:
# You can remove elements from a list using methods like remove() or pop().

# In[62]:


l1= [1, 'hello', 3.14, True]
l1.pop()

l1


# In[63]:


l1= [1, 'hello', 3.14, True]
l1.remove('hello')

l1


# # Adding elements to a list:
# You can add elements to the end of a list using the append() method.

# In[7]:


l1= [1, "Fiziya" , "Data Analyst" , 35000]
l1.append("Working Professional")

l1


# # Other List Operations

# In[10]:


l1 = ["apple", "banana" , "orange"]
l2=["Mango" , "guava"]

l1+l2


# In[12]:


l1.reverse()
l1


# l1.sort()

# In[13]:


l1.insert(2, "Berry")
l1


# # When we should use lists and when tuples in Python:
# 
# * Use Lists When:
# 
# You need a collection of items that can be changed or modified over time.
# You want to add or remove elements from the collection dynamically.
# The order of elements matters, and you need to maintain the original order.
# You need to use built-in list methods for sorting, appending, or extending the collection.
# You plan to perform various operations on the elements like searching, filtering, or counting.
# 
# Example Case:
# Suppose you are building a to-do list application. Users can add, remove, and modify their tasks. In this case, using a list to store the tasks makes sense because you can easily add new tasks, mark them as completed, or remove them as the user interacts with the application.
# 
# * Use Tuples When:
# 
# You want to create a collection of items that should remain constant and immutable throughout the program's execution.
# You need to use the collection as a key in a dictionary because dictionary keys must be immutable.
# You want to guarantee that the order of elements will not change accidentally.
# You want to use a collection as a set of coordinates or a point in space.
# 
# 
# Example Case:
# Suppose you are working on a geometric shapes application, and you want to represent different points in 2D space. In this case, using tuples for the coordinates is suitable because the coordinates of points should not change, and they should be used as keys in a dictionary.

# # Python Dictionary
# 
# Dictionary is a collection of key-value pairs. They are unordered, mutable, and extremely useful for organizing and retrieving data quickly based on specific keys.

# In[20]:


emp_details = {
    "name" : "John Doe",
    "age" : 30, 
    "Occupation" :" Software Engineer", 
    "Email" : "john@exmple.com",
    "is_employed": True
}


# In[21]:


emp_details


# In[22]:


del emp_details["age"]
emp_details


# In[23]:


exapmle = {
    1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60
}


# In[24]:


exapmle


# In[26]:


10 in exapmle


# In[27]:


# Creating a dictionary of students and their scores
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Emma": 88
}


# In[28]:


student_scores


# In[29]:


type(student_scores)


# In[30]:


student_scores.keys()


# In[31]:


student_scores.values()


# In[32]:


# Accessing a student's score

student_scores["Bob"]


# In[33]:


# Adding a new student and their score

student_scores["Fiziya"] = 99


# In[34]:


student_scores


# In[35]:


# Modifying a student's score

student_scores["Charlie"] = 81


# In[36]:


student_scores


# In[37]:


# Removing a student and their score

del student_scores["Emma"]


# In[38]:


student_scores


# In[45]:


# Checking if a student exists in the dictionary
student_scores
if "Bob" in student_scores:
    else
        print("Bob's score does not exist in the dictionary.")


# In[ ]:





# # Python Set
# 
# It is an unordered collection of unique elements. It is denoted by curly braces {} and can contain elements of different data types, such as integers, strings, or even other sets. 
# 
# * The key feature of a set is that it does not allow duplicate values, so each element in a set must be unique. 
# * Sets are mutable, meaning you can add or remove elements after creating them.

# In[46]:


my_set = {1, 2, 3, 4}


# In[47]:


my_set


# In[48]:


# adding duplicates

my_set= {1, 3, 2, 3, 2, 4}


# # Adding elements to a set:
# You can add elements to a set using the add() method.

# In[50]:


fruits = {'apple', 'banana', 'orange'}


# In[51]:


fruits.add('grape')


# In[52]:


fruits


# In[53]:


fruits.add('apple')


# In[54]:


fruits


# In[55]:


fruits.update(['lichi','guava'])


# In[56]:


fruits


# # Removing elements from a set:
# You can remove elements from a set using the remove() method. If the element is not present in the set, it will raise a KeyError. Alternatively, you can use the discard() method, which does not raise an error if the element is not found.

# In[57]:


fruits = {'apple', 'banana', 'orange'}


# In[58]:


fruits.remove('banana')


# In[59]:


fruits


# In[60]:


# Trying to remove a non-existing element

fruits.remove('grape')


# In[61]:


fruits.discard('grape')


# In[62]:


fruits


# # Set Functions:

# In[63]:


set1 = {1, 2, 3}
set2 = {3, 4, 5}


# In[64]:


# Union: Elements present in either set

union_set = set1.union(set2)


union_set


# In[65]:


# Intersection: Elements present in both sets

intersection_set = set1.intersection(set2)


intersection_set 


# In[66]:


# Difference: Elements present in set1 but not in set2

difference_set = set1.difference(set2)


difference_set


# In[ ]:




