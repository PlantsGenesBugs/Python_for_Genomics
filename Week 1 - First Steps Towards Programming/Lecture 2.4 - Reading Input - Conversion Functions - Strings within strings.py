# Reading input

# Get input from user by asking them to provide it - use the input() function in Python 3 (raw_input() in Python 2)

dna = input("Enter DNA sequence:")
#Enter DNA sequence:

# Type sequence - it assigns that value as a string to the dna object

# Similarly you can ask the user to provide a number
my_number = input("Please enter a number:")
#Please enter a number:
# NOTE: this number is saved as a STRING not a number, so type(my_number) <class 'str'>
# To convert to number do...

actual_number=int(my_number) #converts to integer <class 'int'>


# Conversion Functions
# int() converts to integer
# float() converts to floating point number
# complex() creates a complex number
# str() converts to a string
# chr() converts integer to character


# Strings within strings
# From previous calculations we determined that the GC content of a particular sequence was 53.06122448979592
gc_perc = 53.06122448979592

# Express this in a sentence:
print("The DNA sequence's GC content is",gc_perc,"%") # Use commas to separate strings and variables
#The DNA sequence's GC content is 53.06122448979592 %

# Change the way that print() displays the number
# Use the % operator as a placeholder. % is used with a letter to indicate what type of value it is to be replaced with: %s - string, %d - number, %f - float
# In this case we want to print the number above with 3 decimal places. Because there are 2 places before the decimal, the total number of places will be 5.
# Replace ",gc_perc," with %5.3f which specifies a float, 5 values in total, and 3 values after the decimal point. Add %% to print "%" after the number (otherwise it would indicate another placeholder %). Add the variable gc_perc after a % to indicate this is the variable to use. (You can use more than one %f, %s or %d, as long as you supply the variables that have to replace them in your string.)

print("The DNA sequence's GC content is %5.3f %%" % gc_perc)
#The DNA sequence's GC content is 53.061 %

print("%d" % 10.6)
# 10

print("%3d" % 10.6)
#  10 adds extra space in front of 10 (zero - total space = 3 letters)

print("%e" % 0.0000000004)
# 4.000000e-10
print("%3.1e" % 0.0000000004)
# 4.0e-10

print("%s" % dna)
#ATGTGGTACTAGATA






