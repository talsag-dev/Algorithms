import numpy as np

def Longest_Increasing_Subsequence(arr):
	lis = np.full(shape=len(arr),fill_value=1)

	for i in range(len(arr)):
		for j in range(i):
			if arr[i]>arr[j]:
				lis[i] = max(lis[j]+1,lis[i])
			
	return max(lis)



print(Longest_Increasing_Subsequence([10,22,9,33,21,50,41,60,80]))