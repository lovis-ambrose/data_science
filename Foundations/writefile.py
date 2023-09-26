# program to write a file
import os
try:
    file_path = "~/Documents/Hands-On/6 Months Hero/Data Scientist/Yes/myfile.txt"
    # Expand the tilde (~) to the user's home directory
    expanded_path = os.path.expanduser(file_path)
    file = open(expanded_path, "w")
    file.write("\n I love python \n Its the best programming language. \n I use it for data science")
    file.close()
except:
    print("OOPS.. error occurred")
finally:
    print("Thank you!")
    
# end writing file
    
    
    
# reading the file
file = open(expanded_path, "r")
print(file.read())
file.close()


# alternatively
# reading using with key word ie for the case of large files where u may forget to close
with open(expanded_path, "r") as f:
    print(f.read())
    
    
    
# to sho that the file is closed automatically
print(f.closed)