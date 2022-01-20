import numpy as np
def Find_maximum_length_Snake_sequence(mat):
    dp = np.zeros((len(mat),len(mat[0])),dtype = np.int64)
    dp[0][0] = 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j==0 and i==0: continue
            if i==0:
                if mat[i][j-1]-1 == mat[i][j] or mat[i][j-1]+1 == mat[i][j]:
                    dp[i][j] = dp[i][j-1]+1
                else:
                    dp[i][j] = 1
                continue
                    
                
            if j==0:
                if mat[i-1][j]-1 == mat[i][j] or mat[i-1][j]+1 == mat[i][j]:
                    dp[i][j]=dp[i-1][j]+1
                else:
                    dp[i][j]=1
                continue
                    
            dp[i][j]= max(dp[i-1][j],dp[i][j-1])
            
            if mat[i-1][j]+1 == mat[i][j] or mat[i-1][j]-1==mat[i][j]:
                dp[i][j]  = max(dp[i-1][j]+1,dp[i][j])
                
            if mat[i][j-1]+1 == mat[i][j] or mat[i][j-1]-1==mat[i][j]:
                dp[i][j] = max(dp[i][j-1] +1,dp[i][j])
                
            
    
    length = dp[-1][-1]
    return length

mat = [[1,2,3],[6,5,4],[7,8,9],[12,11,10]]

print('longest snake sequence is: ',Find_maximum_length_Snake_sequence(mat))
                    