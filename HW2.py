# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:28:05 2018

@author: Alexander
"""
#%%
"""
Задача 1
"""

def summ35(n):
    s = 0
    for i in range(n):
        if (i%3==0) or (i%5==0):
            s = s + i
    return(s)

#%%
"""
Задача 2
"""

def fibo(n):
    if n < 2:
        return n
    return fibo(n-2) + fibo(n-1)
# 173402521172797813159685037284371942044301

#%%
"""
Задача 3
"""

import pandas
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()
def anagrams(s):
    n=len(s)
    if n == 1:
        return s
    sb=[]
    for i in range(n):
        sb.append(s[i])
        rval=anagrams(s[0:i]+s[i+1:n])
        if isinstance(rval,str):
            sb[i]=sb[i]+rval
        if isinstance(rval,list):
            c=sb[i]
            sb[i]=[c + rval[x] for x in range(len(rval))]
    if(n==2):
        return sb
    else:
        c=[sb[x][h] for x in range(len(sb)) for h in range(len(sb[x]))]
        return c
    
    
    
    
    
    
    
    
#%%

"""
Задача 4
"""










    
    
    
    
#%%

"""
Задача 5
"""
name = "words-list-russian.txt"
ds = (pandas.read_table(name, header = None))[0].tolist()
import pandas
import random
n=5
#making a list contains only 5-letters words
ds5 = [i for i in ds if len(i) == 5]
#def datasort(n):
#    n = len(a[i])
#    for i in range(n):
#        
def complet(letters, user):
    lst = [0]
    for correct, guess in zip(letters, user):
        if guess in letters:
            lst[0] += 1
    return tuple(lst)
words = random.choice(ds5)
letters = set(words)
playing = True
print("Хочешь развлечься,шалун?;-)")
guesses = 0
while playing:
    print(words)
    user = input("Начинай веселье!\n")
    if user == "Не хочу":
        break
    lettercount = complet(letters, user)
    guesses += 1
    print("Всего %s букв!Давай еще!" % lettercount)
    
    if lettercount[0] == 5:
        playing = False
        print("Красауа, отгадал с %s попыток!"
                % (guesses))




































