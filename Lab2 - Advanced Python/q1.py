# Q1.  Create and access tuples.
#     Create a tuple of colors.
#     Access elements using indexing.
#     Try to modify an element in the tuple (to demonstrate immutability).
#     Find the number of occurrences of a specific element in the tuple.

colors = ("red", "blue", "green", "yellow", "blue")
print("First color:", colors[0])    
print("Last color:", colors[-1])
blue_count = colors.count("blue")
print("Number of times 'blue' appears:", blue_count)
