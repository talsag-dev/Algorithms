import numpy as np

def Maximum_Sum_Increasing_Subsequence(arr):
    msis = np.array(arr)
    
    for i in range(len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                msis[i] = max(msis[i],msis[j]+arr[i])
    print(msis)
    return max(msis)


print(Maximum_Sum_Increasing_Subsequence([1,101,2,3,100,4,5]))
        