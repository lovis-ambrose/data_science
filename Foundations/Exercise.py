# first write data to a file
import os
try:
    file_path = "~/Documents/Hands-On/6 Months Hero/Data Scientist/Yes/input.txt"
    expanded_path = os.path.expanduser(file_path)
    with open(expanded_path, "w") as f:
        f.write(str([
            [6,8],
            [7,6],
            [2,8],
            [9,5],
            [9,6]
        ]))
    print("Input file written successfully")
except:
    print("OOPS... an error occured")
    
# read the file
countNum = 0
with open(expanded_path,"r") as f:
    for row in f:
        if 9 in f:
            countNum+=1
        print(countNum)
