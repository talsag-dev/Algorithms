import numpy as np

def Tilin_Problem(n):
    if n==0:
        return
    
    counts = np.zeros((n+1),dtype=np.int64)
    
    
    counts[0] = counts[1] = 1
    
    for i in range(2,n+1):
        counts[i] = counts[i-1]+counts[i-2]
        
    return counts[n]

def main():
    n=4
    
    print(Tilin_Problem(n))

if __name__ == '__main__':
    main()
    

    