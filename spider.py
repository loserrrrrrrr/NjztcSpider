#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor,as_completed
print (requests.get("http://njzy.njztc.com/find_taskWorkList.jspx"))


# In[3]:


response=requests.get("http://njzy.njztc.com/find_taskWorkList.jspx")
print(response.status_code)
print(response.content.decode("utf-8"))


# In[29]:


def getData(url):
    content=response.content.decode("utf-8")
    soup=BeautifulSoup(content,"html.parser")
    list =soup.find("div").findAll("li")
    pageDatas=[]
    for i in list :
        lis=i.findAll("li")
        if(len(lis)==0):
            continue
        if(len(lis)<7):
                continue
        detailUrl=''
        res=getDetail(baseUrl+detainUrl)
        pageDatas.append(res)
    return pageDatas


# In[31]:


url="http://njzy.njztc.com/find_taskWorkList.jspx"
getData(url)


# In[ ]:




