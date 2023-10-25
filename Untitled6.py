#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


# code 8 assignment
data_list = [('apple', 5), ('banana', 2), ('orange', 8), ('grapes', 3), ('pineapple', 1)]

def convert_to_dictionary(data_list):
    result_dict = {}
    for item in data_list:
        key, value = item
        result_dict[key] = value
    return result_dict


# In[7]:


#using function for conversion
convert_dict = convert_to_dictionary(data_list)

print("Original Data Type : ", data_list)
print("Converted Data Type : ", convert_dict)

