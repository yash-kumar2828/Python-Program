
import os

# Specify the path to the directory
directory_path = '/'

# List all files and subdirectories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)