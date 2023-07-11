# We have a list containing integers, negatives and float
# We want to calculate the factorial of integers
# We need to separate the integers from the list using the decorator

def decorat_func(func):
    def make_new_list(n):
        if n >= 0 and isinstance(n , int):
            new_number_list.append(n)
            factorial_new_number_list.append(func(n))
    return make_new_list
                
@decorat_func
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
number_List = [1, 3.5 , 8 , -4.5 , 3 , 5 , 2 , -10 , -16 , 5 , 0.9 , 0 , -6 , 9 , 3.4 , 25.01 , 11.5]
new_number_list = []
factorial_new_number_list = []
for n in number_List:
    factorial(n)
print(f"New Number List : {new_number_list}")
print(f"Factorial New Number List : {factorial_new_number_list}")