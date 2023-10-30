# Consider the problem of searching for an element 'v' in an array 'A.' 
# Write a recursive code that returns the index of the element 'v' if it belongs to the array or NULL otherwise. 
# Using Big-O notation, calculate the complexity of your algorithm. s

## Search V in A with complexity O(n)
def search(A, v): 
    if len(A) == 0:
        return None
    for index, element in enumerate(A):
        if element == v:
            return index
    return None

## Example when V is in A
print(search([1, 2, 3, 4, 5], 1))

## Example when V is not in A
print(search([1, 2, 3, 4, 5], 6))

## Example when A is empty
print(search([], 1))