import numpy as np
def Longest_Repeated_Subsequence(str):
    
    dp = np.zeros((len(str),len(str)),dtype=np.int64)
    

    for i in range(len(str)):
        for j in range(len(str)):
            if i==j:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
            elif i!=j:
                if str[i]==str[j]:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
    return dp[-1][-1]

print(Longest_Repeated_Subsequence('aabebcdd'))