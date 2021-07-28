#!/usr/bin/env python
# coding: utf-8

# # Pattern Programming
# Registration ID : SIRSS2140
# 
# RAJ SANKAR GS
# Q1.
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
# In[1]:


n=5
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(n,end=" ")
    print()        

Q2.
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
# In[2]:


n=5
for i in range(n,0,-1):
    for j in range(0,i+1):
        print(j,end=" ")
    print() 

Q3.
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
# In[3]:


n=5
for i in range(n):
    for j in range(i+1):
        print(i+(i+1),end=" ")
    print()

Q4.
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
# In[4]:


n=5
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()

Q5.
1
3 2
6 5 4
10 9 8 7
# In[5]:


start = 1
stop = 2
currentNumber = stop
for row in range(2,6):
    for col in range(start,stop):
        currentNumber -= 1
        print(currentNumber, end=" ")
    print()
    start = stop
    stop += row
    currentNumber = stop

Q6.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
# In[6]:


def pascal(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j),end=" ")
        print()
def function(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
pascal(7)

Q7.
1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5
5 5 5 5 5
# In[7]:


n=5  
for i in range(1,n+ 1):  
    for j in range(1, n+ 1):   
        if j <= i:  
            print(i, end=' ')  
        else:  
            print(j, end=' ')  
    print()

Q8.
1
2 4
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64
# In[8]:


n=9  
for i in range(1,n):  
    for j in range(1, i+ 1):
        print(i*j, end=" ")  
    print()

Q9.

* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
# In[9]:


n=6
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print() 

Q10.

      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
# In[10]:


n=7
for i in range(1,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

Q11.

*
* *
* * *
* * * *
* * * * *
* * * * * *

* * * * * *
* * * * *
* * * *
* * *
* *
*
# In[11]:


n=6
for i in range(0, n):
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")
print("                   ")
for i in range(n,0,-1):
    for j in range(0, i):
        print("* ", end="")
    print("\r")

Q12.

* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
# In[12]:


n=5
for i in range(n):
    for j in range(0,n-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,n-1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

Q13.

        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *
# In[13]:


n=5
k = 2 * n - 2
for i in range(0, n-1):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")
k = -1
for i in range(n-1,-1,-1):
    for j in range(k,-1,-1):
        print(end=" ")
    k = k + 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

Q14.

* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
# In[14]:


n=4
k = n - 2
for i in range(n,-1 ,-1):
    for j in range(k , 0 , -1):
          print(end=" ")
    k = k + 1    
    for j in range(0, i+1):
        print("* " , end="")
    print("\r")
k = 2 * n  - 2
for i in range(0 , n+1):
    for j in range(0 , k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")

Q15.

****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*
# ### Divide into two parts

# In[15]:


# part1
for i in range(8,0,-1):
    for j in range(0, i):
        print("*", end="")
    for j in range(8-i):
        print("_",end="")
    print()


# In[16]:


# part2
for i in range(8,0,-1):
    for j in range(8-i):
        print("_",end="")
    for j in range(i,0,-1):
        print("*",end="")
    print()


# In[17]:


# combine the for loops
for i in range(8,0,-1):
    for j in range(0, i):
        print("*", end="")
    for j in range(8-i):
        print("_",end="")
    for j in range(8-i):
        print("_",end="")
    for j in range(i,0,-1):
        print("*",end="")    
    print()
    


# In[ ]:





# In[ ]:




