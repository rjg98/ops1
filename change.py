#!/usr/bin/env python
# coding: utf-8

# In[40]:


k=open("/prog/MlOp.py",'r')
a=k.readlines()
k.close()
count=open("/data/data/COUNT.txt",'r')
c=count.readlines()
count.close()



# In[41]:


if(c[0]=='1'):
    with open ("/prog/MlOp.py",'w') as k:
            for l in a:
                if l.strip("\n")!="l(16,count,3)":
                    k.write(l)
                if l.strip("\n")=="l(16,count,3)":
                    k.write(l.replace('l(16,count,3)','l(16,count,3)\nl(32,count,3)'))
elif(c[0]=='2'):
    with open ("/prog/MlOp.py",'w') as k:
            for l in a:
                if l.strip("\n")!="l(32,count,3)":
                    k.write(l)
                if l.strip("\n")=="l(32,count,3)":
                    k.write(l.replace('l(32,count,3)','l(64,count,3)\nl(64,count,3)'))
        


# In[42]:

print("model updated")


# In[ ]:





# In[ ]:




