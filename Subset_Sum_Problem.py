import numpy as np
def _subset_sum_problem(values:list,sum:int)->bool:
	if len(values) == 0:
		return
	if sum <= 0:
		return

	dp = np.zeros((len(values)+1,sum+1),dtype=bool)

	for i in range(len(values)+1):
		# if sum==0
		dp[i][0] = True

	# for i in range(1,sum+1):
	# 	dp[0][i] = False
	# # this one is unnecessary cause all table is false thanks to np.zeroes but 
	# # I keep it to understand better

	for i in range(1,len(values)+1):
		for j in range(1,sum+1):
			#from index[1,1] till the end
			if j<values[i-1]:
				#if current sum smaller than current val
				dp[i][j] = dp[i-1][j]
			else:
				# j>=values[i-1]
				# current sum bigger or equal than current valid
				# we wnt to take last case or sum without this val
				dp[i][j] = (dp[i-1][j] or dp[i-1][j-values[i-1]])

	# uncomment this code to print table 
	# for i in range(len(values) + 1):
	# 	for j in range(sum + 1):
	# 		print (" ",dp[i][j], end =" ")
	# 	print()
	return dp[len(values)][sum]
					



	
def main():
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (_subset_sum_problem(set, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")
		
if __name__ == '__main__':
	main()
