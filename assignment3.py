# Jarrett Strow
# Assignment 3

def arraysum(thelist): # calculates the total sum of all elements of an array
    sum = 0
    for element in thelist:
        sum = sum + element
    return sum

def arrayprod(thelist): # calculates the total product of all elements of an array
    product = 1
    for element in thelist:
        product = product * element
    return product

# User inputted values
size = int(input("Enter the size of the array: "))
list = []

for i in range(0, size):
    num = int(input("Enter an integer for the %d element of the array: " % i))

    list.append(num)

print("The total sum of your inputted array is: " + str(arraysum(list)) + ", and the product of your entire array is: " + str(arrayprod(list)))


