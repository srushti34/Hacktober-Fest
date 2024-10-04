import os
file_name = "data.txt"
if os.path.exists(file_name):
 os.remove(file_name)
 print(f"{file_name} removed successfully.")
else:
 print(f"{file_name} does not exist.")
os.remove(file_name)