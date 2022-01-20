def Unbounded_knapsack(Capacity,n,weight,val):
    # Given a knapsack weight W and a set of n items with certain value and weight,
    # we need to calculate the maximum amount that could make up this quantity exactly.
    # This is different from classical Knapsack problem,
    # here we are allowed to use unlimited number of instances of an item.
    dp=[]
    for i in range(Capacity+1):
        dp.append(0)
    for i in range(0,Capacity+1):
        for j in range(0,n):
            if weight[j] <= i:
                dp[i] = max(dp[i] , dp[i-weight[j]]+val[j])
    return dp[Capacity]
''' No. of items '''
n = 4
''' Weights of all items '''
weight = [5,10,8,15]
''' Values of all items '''
val = [40,30,50,25]
''' Capacity of Knapsack '''
Capacity = 120
print("The maximum value possible is ",Unbounded_knapsack(Capacity,n,weight,val))