import numpy as np

def largest_divisible_pairs_subset(arr:list)->int:
    if arr == None or len(arr)==0:
        return
    
    arr.sort() ##sort in descending order
    dp = np.zeros(len(arr))
    dp[len(arr) - 1] = 1
 
    # Fill values for smaller elements
    for i in range(len(arr) - 2, -1, -1):
         
        # Find all multiples of a[i]
        # and consider the multiple
        # that has largest subset    
        # beginning with it.
        mxm = 0
        for j in range(i + 1, len(arr)):
            if arr[j] % arr[i] == 0 or arr[i] % arr[j] == 0:
                mxm = max(mxm, dp[j])
        dp[i] = 1 + mxm
         
    # Return maximum value from dp[]
    return max(dp)

def main():
    arr = [18,1,3,6,13,17]
    arr2 = [1,10,5,3,15]
    
    print(f'length of longest sequence is:{largest_divisible_pairs_subset(arr)}\n')
    print(f'length of longest sequence is:{largest_divisible_pairs_subset(arr2)}')

if __name__=='__main__':
    main()
        
            
    
    
