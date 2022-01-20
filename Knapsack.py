def Knapsack_0_1(W,weights,values):
    # Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
    # In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
    # Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
    # You cannot break an item, either pick the complete item or don’t pick it
    # we cannot pick and item infinite times only one time
	n = len(values)
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	# Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif weights[i-1] <= w:
				K[i][w] = max(val[i-1]
						+ K[i-1][w-weights[i-1]],
							K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	return K[n][W]


# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(Knapsack_0_1(W, wt, val))
