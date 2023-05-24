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