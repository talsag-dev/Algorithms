import numpy as np

def Lognest__polindromiec_Subseq(str ):
    # we want to find the longest polindromiec subseq in a string 
    # for example if we have S=BARCAR we have RAR which is length 3
    
    if str is None or len(str) == 0:
        return
    
    Mat = np.zeros((len(str),len(str)),dtype=np.int64)


    for gap in range(len(str)):
        i=0
        for j in range(gap,len(str)):
            if i==j:
                Mat[i][j] = 1
                continue
            if str[i]==str[j]:
                Mat[i][j] = Mat[i-1][j-1]+1
            else:
                Mat[i][j]=max(Mat[i][j-1],Mat[i+1][j])
            i+=1
              
    
    print(f'Longest Polindromiec Subsequnce length is:{Mat[0][len(str)-1]}')
    return Mat
    
def Print_Longest_polindromiec_Subseq(str):
    Mat = Lognest__polindromiec_Subseq(str)
    
    
Lognest__polindromiec_Subseq('B')
            
            
                
            