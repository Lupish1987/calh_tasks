#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import xml.etree.ElementTree as ET


def task1_solution():
    file = open("task1_solution.txt","w")
    response = requests.get("https://coding-academy.pl/all_customers")
    tree = ET.fromstring(response.content)
    
    #element = tree.getchildren()
    for subelement in list(tree):
        file.write(f"{subelement.text}\n")
        
    file.close()
    pass


if __name__ == '__main__':
    task1_solution()


# In[ ]:





# In[ ]:





# In[ ]:




