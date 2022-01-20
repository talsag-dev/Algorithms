import numpy as np
def Coing_Change(N:int,m:list)->int:
    # typical knapsack problem counting the number of ways
    # i can change a sum(N) with the coins valued in N
    if len(m) == 0:
        # we can also check type and stuff like neg numbers inside array but 
        # this is not the subject of this code
        return 
    if N<=0:
        return
    
    dp = np.zeros((N+1,len(m)),dtype=np.int64)
    
    for i in range(len(m)):
        dp[0][i] = 1 # base case
        
    for i in range(1,N+1):
        for j in range(len(m)):
            
            #count the ways with m[j]
            x = dp[i-m[j]][j] if i-m[j]>=0 else 0
            
            #count the ways without m[j]
            y = dp[i][j-1] if j>=1 else 0
            
            
            dp[i][j] = x+y
            
    return dp[N][len(m)-1]


def main():
    N = 5
    m = [1,2,3]
    print(f'Number of ways to change {N} with the coins:{m} is:',Coing_Change(N,m))
        
    
if __name__=='__main__':
    main()
       
