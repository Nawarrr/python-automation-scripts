# Directory Organizer
This python  scripts orgainzes your directory to folders (PDF , Word , Code)


## How to use
1. download or clone the repo
2. Copy the script to the folder you want to organize
3. run the file


## How to Edit for your convenience
1. to add more file types to organize copy  this line with your prefrence
    ```python
            organize_extension(current_directory ,['extension1' ], 'Folder Name' )
    ```
    then paste it in line 12 (Marked with POST HERE comment)
    - You can  do as much as you want just copy it multiple times
    - For multiple extension in the same folder do this
    ```python
        organize_extension(current_directory ,['extension1' , 'extension2', 'etc ... ' ], 'FolderName' )
    ```
2. You can change folder names if you want by changin the folder name or adding it from lines of the first function (lines 8-11)
    ```python
        organize_extension(current_directory ,['extension1' , 'extension2', 'etc ... ' ], 'FolderName' )
    ```
3. You can add more code extension based on the languages you use in coding , line 11 
4. You can use a any path by changing the path variable from line 5