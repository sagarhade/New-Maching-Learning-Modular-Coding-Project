import os,sys
from pathlib import Path
import logging

while True:
    Project_name = input("Enter Your Project Name: ")
    if Project_name !="":
        break
 
#src/__init__.py    
list_of_files = [
    f"{Project_name}/__init__.py",
    f"{Project_name}/components/__init__.py",
    f"{Project_name}/config/__init__.py",
    f"{Project_name}/constants/__init__.py",
    f"{Project_name}/entity/__init__.py",
    f"{Project_name}/exceptaion/__init__.py",
    f"{Project_name}/logger/__init__.py",
    f"{Project_name}/pipeline/__init__.py",
    f"{Project_name}/utils/__init__.py",
    f"config/config.yml",
    "schema.yml",
    "app.py",
    "main.py",
    "logs.py",
    "excepation.py",
    "setup.py"
] 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        logging.info("file is already present as:{filepath}")
                   