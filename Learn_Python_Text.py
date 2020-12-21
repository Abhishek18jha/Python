#Read the complete list text file
handle = open("text.txt")
data = handle.read()
print(data)
handle.close()
print("-------------------------------")
#Read the complete single first line of the file
handle = open("text.txt")
data = handle.readline()
print(data)
handle.close()
print("-------------------------------")
#Read the complete all by line by line of the file
handle = open("text.txt")
data = handle.readlines()
print(data)
handle.close()
print("-------------------------------")
# Read the file piece by piece
handle = open("text.txt","r")
for line in handle:
    print(line)
handle.close()
#
handle = open("text.txt","r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break
# Writing File in python
handle = open("output.txt","w")
handle.write("This is a best")
handle.close()

