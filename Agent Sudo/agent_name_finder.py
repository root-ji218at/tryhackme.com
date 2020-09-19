import os

code_name = input("Please Input the code-name --->  ")

os.system("curl -A "+code_name+" -L 10.10.15.49")
