# Reading data from files instead of typing it in

# Open the file; do something to the file; close the file

# Opening files
open(filename, mode)
f = open('myfile', 'r')         # Open myfile in reading mode (default; can be omitted)
f = open('myfile', 'w')         # Open myfile in writing mode (truncates content first)
f = open('myfile', 'a')         # Open myfile in append mode (append new code to the end of the file)

# The result of the open() function is an object

# To avoid error message if the file doesn't exist:
try:                            # You can try a function and if it doesn't work, the system won't crash
  f=open("myfile")
except IOError:
  print("That file does not exist")

  
# Reading from a file
# Create a file (can be .txt) that contains the following. Make sure it is in the working directory.
"This is the first line of the file."
"This is the second line of the file."

# Open the file
try:                            
  f=open("myfile.txt")            # Read mode
except IOError:
  print("That file does not exist")

# You can read each line by looping over the file object.
for line in f:
    print(line)

# Can also read using the read method of the file object. This reads the entire file (not line-wise; see below).
f.read()

# Doesn't show anything because we've just read the whole file and are at the end of the file. The read method returns the content of the file object f from the current position in the file to the end of the file.
# To change your position within the file object, use f.seek(offset, from_what). The position is computed by adding offset to a ref point; the ref point is selected by the from_what arg, which in text files is only allowed to be 0 signifying the beginning of the file

f.seek(0)
f.read()
# 'This is the first line of the file.\nThis is the second line of the file.'

# To read line by line, use readline() method
f.seek(0)
f.readline()
#'This is the first line of the file.\n'


# Writing into a File
# Use write() method of file object
# Must first open file object in write mode
f=open("myfile.txt", "a")                 # Note a for append, otherwise will over-write
string = "This is a third added line."
f.write(string)

# To read it back, will have to open in read mode
f=open("myfile.txt", "r") 
for line in f:                            # OR f.read()
  print(line)
 
# To close a file, use the close() method with the file object
f.close()






    

