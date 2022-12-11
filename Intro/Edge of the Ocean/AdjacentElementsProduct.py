def solution(inputArray):
    largest_product = float('-inf')
    
    for i in range(1, len(inputArray)):
        product = inputArray[i] * inputArray[i-1]
        largest_product = max(largest_product, product)
        
    return largest_product