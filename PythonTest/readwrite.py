file = open('test.txt')
#print(file.read()) # To Read All Content  From the file

#print(file.read(5))  # To read Number of Char by passing parameter

#print(file.readline()) # Read File Data line by lIne

# Different Between Readline and Readlines method is Readlines stored in the list, iterate one by one, where Readline
#print the value lne by line not in list

# Print file line by line using readline method

#line = file.readline()

#while line !="":
#    print(line)
#    line = file.readline()

# Read Record Line by Line when Multiple Strings are in One File.

# Readlines Method stored Data in list
for line in file.readlines():
    print(line)

file.close()

