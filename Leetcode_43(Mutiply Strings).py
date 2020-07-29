def multiply(self, num1: str, num2: str) -> str:
    v1, v2, count = 0, 0, 0
    num_dict = {str(i): i for i in range(10)}
    
    #convert each number in the string to the right position in the number format
    for i in num1:
        v1 += num_dict[i] * pow(10, len(num1)-1-count)
        count += 1
        
    # reset count for second number conversion
    count = 0
    
    # same thing 
    for i in num2:
        v2 += num_dict[i] * pow(10, len(num2)-1-count)
        count += 1
        
    return str(v1*v2)