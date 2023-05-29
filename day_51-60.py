## 51  seek() and tell() functions
'''
the seek() and tell() functions are used to work with file objects and their positions within a file
seek() - allows you to move the current position within a file to a specific point.
tell() - returns the current position within the file, in bytes. 
'''

# with open("file_io.txt","r") as file:
#     file.seek(3)    # Move to the 3th byte in the file
#     text = file.read(4)     # Read the next 4 byte
#     print(text)
#     print("current position",file.tell())   #return the current position

# with open("file_io.txt","a") as file:
#     file.write("this is from seek() and tell() function")    # Move to the 3th byte in the file
#     file.truncate(26)   #if you want to truncate the file to a specific size, it only print upto 26 byte and only write 'this i' because previous string char also come in 26 byte

# with open("file_io.txt","r") as file:
#     print(file.read())

