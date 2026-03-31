#system control
import os
from pathlib import Path

# Get the current working directory
current_directory = os.getcwd()
# file_path = os.path.join(current_directory, "sample.txt")
print(f"Current working directory: {current_directory}")
file_path = os.path.join(current_directory,"upload_dummy.txt")
print(f"File path: {file_path}")


file_path2 = Path.cwd()/"upload_dummy.txt"
print(f"File path using pathlib: {file_path2}")


if os.path.exists(file_path):
    print("File exists.")
else:
    print("File does not exist.")
if file_path2.exists():
    print("File exists using pathlib.") 
else:    print("File does not exist using pathlib.")   

os.mkdir("new_folder")
print("New folder created.")

folder_path = Path.cwd()/"new_folder2"
folder_path.mkdir(exist_ok=True)
print("New folder created using pathlib.")


