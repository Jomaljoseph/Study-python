#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''this is python file'''
msg="module_programming"
def sum_list(l):
    sum=0
    for i in l:
        sum=sum+i
    print(sum)
def printing():
    print("hellooooo")
if __name__=='__main__':    # below calling only will work if it is main file
    sum_list([1,2,3,4])     # it will not work if it is imported to other file
    printing()


# In[ ]:




