# Q3. Demonstrate the difference between mutable and immutable data types.
#     Create a list and a tuple.
#     Try to modify an element in both the list and the tuple.
#     Observe the results and explain the difference.

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_list[2] = 10
print("Modified list:", my_list)  
try:
    my_tuple[2] = 10
except TypeError as e:
    print("Error:", e)
print("Original tuple:", my_tuple)
