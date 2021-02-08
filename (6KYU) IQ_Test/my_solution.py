def iq_test(numbers):
    numbers = numbers.split(" ")
    ctr_even = 0
    ctr_odd = 0
    ans = 0
    
    for i in range (len(numbers)):
        numbers[i] = int(numbers[i])
        if numbers[i] % 2 != 0:
            ctr_odd +=1
        else:
            ctr_even +=1
            
    for j in range (len(numbers)):  
        if ctr_even == 1 and numbers[j] % 2 == 0:
            ans = j+1
        if ctr_odd == 1 and numbers[j] % 2 != 0:
            ans = j+1     
    return ans
