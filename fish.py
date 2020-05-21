def solution(A, B):
    
    down_fish = [0] * len(A)
    down_nmbr = 0
    up_f = 0
    
    for i in range(-1, -1*(len(A)+1), -1):
        
        if B[i] is 0: 
            down_fish[down_nmbr] = A[i]
            down_nmbr += 1
        else: 
            
            if down_nmbr is 0: 
                up_f += 1
            else: 
                
                while A[i] > down_fish[down_nmbr-1]:
                    down_nmbr -= 1
                    if down_nmbr is 0:
                        break
                if down_nmbr is 0:
                    up_f += 1
    
    return down_nmbr+up_f
