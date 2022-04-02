def solution(n, lost, reserve):
    
    
    len_r = len(reserve)
    len_l = len(lost)
    answer = n - len_l
    arr = list()
    arr1 = list()
    
    for l in lost:
        if l in reserve:
            print("L:",l)
            arr1.append(l)
            len_r -= 1
            len_l -= 1
            reserve.remove(l)
            # lost.remove(l)
            answer +=1
    for j in range(len(arr1)):
        lost.remove(arr1[j])

        # for r in reserve:
        #     if r == l:
        #         len_r -= 1
        #         len_l -= 1
        #         reserve.remove(r)
        #         lost.remove(l)
        #         answer +=1
                
    
    for i in lost:
        arr.append(i-1)
        arr.append(i+1)
        
        if arr[0] in reserve:
            reserve.remove(arr[0])
            answer +=1
            
        elif arr[1] in reserve:
            reserve.remove(arr[1])
            answer +=1
                
           # if i-1 in reserve:
        #     answer +=1
        #     reserve.remove(i-1)
        # elif i+1 in reserve:
        #     answer +=1
        #     reserve.remove(i+1)         
        

            
    return (answer)
  
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [1,2,3], [2,3,4]))