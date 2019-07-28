def add_numbers(num1,num2):
    total = 0
    for number in range(num1,num2 + 1):
        
        total = total + number
    return total
    
   
answer = add_numbers(333,777)
print(answer)
