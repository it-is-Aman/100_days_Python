def welMsg():
    print("This is from different module")

secret="You are AWESOME"

print(__name__)     #When Python script is run directly, the __name__ variable is set to the string __main__
                    #When the script is imported as a module into another script, the __name__ variable is set to the name of the module which is "MyFile"
if __name__=="__main__":    #if i did't use this then, whenever i import this module 'MyFile' welMsg() will execute
    welMsg()
