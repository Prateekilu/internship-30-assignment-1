#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# a python program to find the factorial of a number


# In[2]:


a = int(input("Enter a number: ")) 
f = 1 
for i in range(1,a+1): 
    f = f * i 
 
print(f'The factorial of the number is {f}') 


# In[ ]:


# a python program to find whether a number is prime or composite


# In[3]:


n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is not prime but composite number")
            break
    else:
        print(n,"number is prime but not composite number")
else :
    print("Please enter positive number only ")


# In[ ]:


# a python program to check whether a given string is palindrome or not


# In[4]:


my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[ ]:


# a Python program to get the third side of right-angled triangle from two given sides


# In[9]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[ ]:


# a python program to print the frequency of each of the characters present in a given string


# In[11]:


test_str = "GeeksforGeeks"
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(all_freq))


# In[ ]:




