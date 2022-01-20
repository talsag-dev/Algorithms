from unittest import result
import numpy as np


def gold_mine_problem(mat:list(list()))->int:
    if len(mat)==0:
        return
    if len(mat[0])==0:
        return
    
    Gold_sum = np.zeros((len(mat),len(mat[0])),dtype=np.int64)
    cols = len(mat[0])
    rows = len(mat)
    for col in range(cols-1,-1,-1):
        for row in range(rows):
            ## iterate through columns
            
            ##right move
            if col==cols-1:
                right = 0
            else:
                right = Gold_sum[row][col+1]
                
            ##right up move  
            if col==cols-1 or row==0:
                right_up = 0
            else:
                right_up = Gold_sum[row-1][col+1]
            ##right down move
            if col==cols-1 or row==rows-1:
                right_down = 0
            else:
                right_down = Gold_sum[row+1][col+1]
                
            Gold_sum[row][col] = mat[row][col] + max(right,right_up,right_down)
            
    result = Gold_sum[0][0]
    for i in range(1,rows):
        if Gold_sum[i][0]>result:
            result = Gold_sum[i][0]
    
    return result


def main():
    mat = [[1,3,3,5,4],[2,1,4,7,2],[0,6,4,3,6]]
    
    print(f'The maximum gold we can get is : {gold_mine_problem(mat)}')
    
    
if __name__ == '__main__':
    main()
            
                
            
    