# Input the text as a single string
input_text = input()  # Example: "shock;979;23"

# Write your solution below and make sure to encode the word correctly
def max_non_adjacent_sum(arr):
    if not arr:
        return 0
    
    include = 0  # Max sum including current element
    exclude = 0  # Max sum excluding current element
    
    for num in arr:
        new_include = exclude + num  # Current element + best sum without adjacent
        exclude = max(include, exclude)  # Best sum without current element
        include = new_include  # Update include for next iteration
    
    return max(include, exclude)  # Maximum sum possible

# Example usage
arr = input_text
arr = eval(arr)  # Convert input string to list
result = max_non_adjacent_sum(arr)
print(result)
