#!/usr/bin/env python
# coding: utf-8

# #Question 1
#     
# 

# In[4]:



   
port1_dict= {21:'FTP', 22:'SSH', 23:'telnet', 80:'http'} 
port2_dict = dict([(value, key) for key, value in port1_dict.items()]) 
print("Original dictionary is : ") 
print(port1_dict)  
print() 
print ("Dictionary after swapping is :  ")  
print("keys:values") 
for i in port2_dict: 
   print(i, " :  ", port2_dict[i]) 


# #Question 2
# 

# In[15]:



list1 = [(1, 2), (3,4), (5, 6)] 
print("The original list : " + str(list1) )

res =[sum(x) for x in list1]
  
# printing result 
print("The summation of all tuple elements are : " +str(res) )


# #Question 3

# In[28]:



tup = [(1, 2,3), (1,2),("a","hit","less")] 

 
result = [] 

for t in tup: 
    for x in t: 
        result.append(x) 


print(result) 


# In[ ]:





# In[ ]:




