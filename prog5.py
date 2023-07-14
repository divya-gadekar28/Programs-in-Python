#Write a Python function to multiply all the numbers in a list.
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
list=[8,2,3,-1,7]
print("Given list :",list)
print("Multiplication of all the elements :",multiply(list))
