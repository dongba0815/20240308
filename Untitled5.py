#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("100")
print(100)
print(50+50)
print("50+50")


# In[2]:


print('%d / %d = %d' %(5, 10, 5/10))


# In[8]:


print("%04d" % 876)
print("%5s" % "CookBook")
print("%1.1f" % 123.45)


# In[9]:


print("{2:d} {0:d} {1:d}".format(111,222,333))


# In[18]:


print(int('1011',2))
print(int('1A',16))


# In[31]:


int('1002',2)
int('1008',8)
int('AAFG',16)

print('모두 오류가 나옵니다.')
print('1번 2진수는 0 ~ 1')
print('2번 8진수는 0 ~ 7')
print('1번 16진수는 A ~ F')
print('까지 허용하기 때문입니다')


# In[27]:


num = 12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)

print("10진수==>", num)
print("16진수==>", hex_num)
print("8진수==>", oct_num)
print("2진수==>", bin_num)


# In[ ]:




