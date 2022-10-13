# Other types of data structures (beyond numbers and strings)

# Lists - an ordered set of values; enclosed in square brackets. Can be different types.
list = ["gene", 5.16e-08, 0.000138511, "a string of words"]
list[1]
#5.16e-08
list[-1]
#'a string of words'

print(list[2])
#0.000138511

# Can change the value of objects in a list using indexing (lists are immutable)
list[0] = "Gene_name"
print(list[0])
#Gene_name

# Note: can't use indexing to change values in strings - strings are immutable
# i.e. motif = "GATCG"
# motif[0] = "A" GIVES AN ERROR

# Can slice lists using index (will create a new list)
list[-3:]
#[5.16e-08, 0.000138511, 'a string of words']

# A full copy of the original list
list[:]
#['Gene_name', 5.16e-08, 0.000138511, 'a string of words']

# Assignment to slices can change the list
list[1:3]
#[5.16e-08, 0.000138511]
list[1:3] = [6.09e-07] # Replaces second and third item in list with the specified value
list
#['Gene_name', 6.09e-07, 'a string of words']
# Clear the whole list
list[:] = []
list
#[]

# Common List Operations
# Concatenation
gene_expression = ["Lif", 6.09e-07, 7.33e-08]
gene_expression + [5.16e-08, 0.000138511]
#['Lif', 6.09e-07, 7.33e-08, 5.16e-08, 0.000138511] # This is a NEW list; must assign to new object to make permanent

# Length
len(gene_expression)
#3


# Delete elements with del() function (destructively)
del(gene_expression[1])
gene_expression
# ['Lif', 7.33e-08] # Everything after position 2 (index 1) moves up one position



# Lists as objects - can also apply methods to them using the . operator
# Commonly used list-related methods

# Adjust by extending with a separate list
gene_expression.extend([5.16e-08, 0.000138511])
gene_expression
#['Lif', 7.33e-08, 5.16e-08, 0.000138511]

# Count number of times an element appears in a list
gene_expression.count("Lif")
#1
print(gene_expression.count("Lif"), gene_expression.count("gene"))
#(1, 0)
# To check if an element is in a list, do a count on the list - result = 0 means it isn't present

# Reverse all elements in a list; doesn't require assigning - reverses list in place
gene_expression.reverse()
gene_expression
#[0.000138511, 5.16e-08, 7.33e-08, 'Lif']

# Lists as Stacks 
# Using methods append and pop, can use a list as a stack where the last element added is the first element retrieved
stack = ["a", "b", "c", "d"]
stack.append("e")
stack
#['a', 'b', 'c', 'd', 'e']

# Difference between append and extend: append takes only one element, while extend takes a list as an argument
# If you try to append a list, that list becomes a single element
list2 = ["x", "y", "z"]
stack.append(list2)
stack
#['a', 'b', 'c', 'd', 'e', ['x', 'y', 'z']]

# Remove/retrieve an item from the top of the stack by using pop() method
elem = stack.pop() # returns the last element added to the list
elem
#['x', 'y', 'z']

elem2 = stack.pop(1) # returns the value based on the index (starting from 0)
elem2
'b'

# Sorting lists
# Using sorted() function
mylist = [3, 31, 123, 1, 5]
sorted(mylist)  # Does NOT change the indexing of elements in the list, but sorts them for display only
#[1, 3, 5, 31, 123]

# Using sort() method
mylist.sort() # apply a method to the list; changes the indexing in the list
mylist
# [1, 3, 5, 31, 123]

# Using sorted() with alphabet elements
mylist2 = ["c", "g", "T", "a", "A"]
print(sorted(mylist2))
#['A', 'T', 'a', 'c', 'g']




