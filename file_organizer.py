import os
import shutil

try:
    path = input('Enter the path of the folder you want to organize: ')
    files = os.listdir(path) # List all files in the specified directory

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:].lower()  # Remove the dot from the extension

        if os.path.exists(f"{path}/{extension}"): # If the path for the extension already exists, move the file there
            shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
        else:
            os.makedirs(f"{path}/{extension}") # If it don't exist, create the directory and move the file there
            shutil.move(f'{path}/{file}', f'{path}/{extension}/{file}')
    print('Your files have been organized!')
    
except FileNotFoundError:
    print("The specified path does not exist. Please check the path and try again.")