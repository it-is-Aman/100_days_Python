## 41 - If ... Else in One Line
# result = value_if_true if condition else value_if_false

# a=7
# b=3
# print("Nice") if a>b else print("not cool") if a==b else ""     #have to write else "" in end

# oldVal = 2
# cond=6
# newVal = 7 if cond > 5 else 9   #newVal will be 7 'cause cond > 5
# print(newVal)


## 42 - Enumerate function 
# allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time

# lstName = ["wsd","cool","nice","boy"]
# for index,name in enumerate(lstName):
#     print(index, name)  #Loop over a tuple and print the index and value of each element

# lstName = ["wsd","cool","nice","boy"]
# for index,name in enumerate(lstName, start=10): #index will start from 10
#     print(index, name)  



## 43 - Virtual Environment

'''A virtual environment is a tool used to isolate specific Python environments on a single machine,
 allowing you to work on multiple projects with different dependencies and packages without conflicts
 '''
'''
python --version    #check python version
python -m venv myenv    # Create a virtual environment
source myenv/bin/activate   # Activate the virtual environment (Linux/macOS)
myenv\Scripts\activate.bat  # Activate the virtual environment (Windows)
myenv\Scripts\activate.ps1   #in powershell
deactivate  # Deactivate the virtual environment
pip freeze > requirements.txt   # Output the list of installed packages and their versions to a file
pip install -r requirements.txt   # Install the packages listed in the requirements.txt file

'''


## 44 - Importing in Python

# import math     #module imported and function can be accessed by dot notation 
# value=math.pow(7,2)
# print(value)

# from math import sqrt   #import specific functions from a module using the from keyword
# value=sqrt(49)
# print(value)

# from math import *  #import all functions and variables from a module using the * wildcard. However, this is generally not recommended
# value=sqrt(49)
# print(value)

# from math import sqrt,pow as p  #only pow will be acessed by p but not sqrt 
# value=p(9,2)
# print(value)

# print(dir(math))    #dir() that you can use to view the names of all the functions and variables defined in a module.

# import MyFile   #I have imported module from MyFile.py which was created by me
# MyFile.welMsg()
# print(MyFile.secret)


## 45 if "__name__ == "__main__" in Python
'''
The if __name__ == "__main__" idiom is a common pattern used in Python scripts to determine whether
the script is being run directly or being imported as a module into another script.
In Python, the __name__ variable is a built-in variable that is automatically set to the name of
the current module. When a Python script is run directly, the __name__ variable is set to the
string __main__ When the script is imported as a module into another script, the __name__ variable
is set to the name of the module

This can be useful if you have code that you want to reuse in multiple scripts, but you only want it to run when the script is run directly and not when it's imported as a module.
'''

# import MyFile       #print "MyFile" because script is imported as a module into another script 
# MyFile.welMsg()     #message print only onces because if __name__ == "__main__" idiom used


## 46 os Module in Python

# import os

# if(not os.path.exists("randomDir")):    #if directory not present then make
#     print("directory has been created")
#     os.mkdir("randomDir")   #make the directory with name "randomDir"

# # for num in range(1,11,1):
# #     os.mkdir(f"randomDir/random {num}")   #make the directory in bulk via loop 

# # for num in range(1,11,1):
# #     os.rename(f"randomDir/random {num}", f"randomDir/random_new {num}")     #rename the directory os.rename(old_name,new_name)

# dirContent=os.listdir("randomDir")      #get a list of the files in a directory "randomDir"
# print(dirContent)

# ## file=os.open("revise.py",os.O_RDONLY)   # Open the file in read-only mode
# ## content=os.read(file,10)      # Read the contents of the file with length
# ## print(content)
# ## os.close(file)      # Close the file
# #
# ## file=os.open("checking_oswrite.txt",os.O_WRONLY)   # Open the file in write-only mode
# ## os.write(file,b"#Changed the context though day_41-50.py")      # write to the file
# ## print("successfully written on checking_oswrite.txt")
# ## os.close(file)      # Close the file


## 47 Again Encoding and Decoding exercise
'''
String.ascii_letters 	It returns a random string that contains both uppercase and lowercase characters.
String_ascii_uppercase 	It is a random string method that only returns a string in uppercase characters.
String.ascii_lowercase 	It is a random string method that returns a string only in lowercase characters.
String.digits 	It is a random string method that returns a string with numeric characters.
String.punctuation 	It is a random string method that returns a string with punctuation characters.

    random.choice(string.ascii_letters)     #must have both string,random module and generate random string
'''

# import random,string
# str=input("Enter your string: ")
# con=int(input("1- Encoding, 2- Decoding: "))
# ranString=""        #empty string
# cond=True if con==1 else False
# if cond==True:
#     if(len(str)>=3):
#         for i in range(1,4,1):      #loop generate random char and store in ranString only 3 characters
#             ranString+=random.choice(string.ascii_lowercase)
#         str=ranString + str[1:] + str[0] + ranString        
#         str=str[::-1]       #this will reverse the string
#         print("Encoded message: ",str)
#     else:
#         str=str[::-1]
#         print("Encoded message: ",str)
# if cond==False:
#     if(len(str)>=3):
#         str=str[::-1]       #reverse the string  
#         str=str[3:-3]       #remove that ranString characters
#         str=str[-1]+str[:-1]        #move last char into front
#         print("Decoded message: ",str)
#     else:
#         str=str[::-1]
#         print("Decoded message: ",str)











