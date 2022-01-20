# Policemen catch thieves
# Difficulty Level : Medium

# Given an array of size n that has the following specifications: 

# Each element in the array contains either a policeman or a thief.
# Each policeman can catch only one thief.
# A policeman cannot catch a thief who is more than K units away from the policeman.
# We need to find the maximum number of thieves that can be caught.
# Examples: 
 

# Input : arr[] = {'P', 'T', 'T', 'P', 'T'},
#             k = 1.
# Output : 2.
# Here maximum 2 thieves can be caught, first
# policeman catches first thief and second police-
# man can catch either second or third thief.

# this one is Greedy approach

from asyncio import TimerHandle
from calendar import THURSDAY
from itertools import pairwise
from re import X
from shutil import which
from time import thread_time


def Catch_thieves(arr:list,k:int)->int:
    police_index = []
    thieves_index = []
    
    for i in range(len(arr)):
        if arr[i]=='T':
            thieves_index.append(i)
        else:
            police_index.append(i)
            
    res,t,p =0,0,0
    while t<len(thieves_index) and p<len(police_index):
        if abs(thieves_index[t]-police_index[p])<=k:
            res+=1
            t+=1
            p+=1
            
        elif thieves_index[t]<police_index[p]:
            t+=1
        else:
            p+=1
            
    return res

if __name__=='__main__':
    arr1 = ['P', 'T', 'T', 'P', 'T']
    k = 2
    n = len(arr1)
    print(("Maximum thieves caught: {}".
         format(Catch_thieves(arr1, k))))

    arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
    k = 2
    n = len(arr2)
    print(("Maximum thieves caught: {}".
          format(Catch_thieves(arr2, k))))

    arr3 = ['P', 'T', 'P', 'T', 'T', 'P']
    k = 3
    n = len(arr3)
    print(("Maximum thieves caught: {}".
          format(Catch_thieves(arr3, k))))
    
# lets try and proof the greedy choice :
# A={(T1,P1),(T2,P2)....,(Tk,PK)} is our optimal solution thus we got 
# k pairs where each pair |Tk-Pk|<=k (by taking the minumim index each time from
# our police_index stack and thives_index stack we get the maximum pairs)
# lets assume by contradiction that we have |Ti-Pk|<=k in which i is minimal than 
# i = min(i,k) thus our algorithm will choose this i and continue to the next
# elemnt in our stack thus we can switch our solution with A-(Tk,Pk) and
# continue with A union (Ti,Pk) so we get another solution but we didnt 
# enlarge our set thus A is our optimal solutuion