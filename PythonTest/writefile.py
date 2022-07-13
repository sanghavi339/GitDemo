# Read The file and Stored the all the line in list and reverse the list and than
#write that list back to the file.

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    #reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

