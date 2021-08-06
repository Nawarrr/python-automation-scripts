import shutil , os
from pathlib import Path
from glob import glob

path = Path.cwd()

def organize_directory(current_directory):
    organize_extension(current_directory , ['pdf'] )
    organize_extension(current_directory ,['docx'], 'Word' )
    organize_extension(current_directory ,['jpeg' , 'png' , 'PNG' , 'jpg'], 'images' )
    organize_extension(current_directory ,['py' , 'js' , 'html' , 'css'  ], 'Codes' )
    #POST HERE (check docs)
    return "Organized"



def organize_extension(current_directory ,
                       extensions , name= None):
    folder_name = name if name else extensions[0].upper()
    print(folder_name)
    folder_path = str(current_directory /folder_name )
    print(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for extension in extensions:
        for item in glob(str(current_directory / f'*.{extension.lower()}')):
            shutil.move(current_directory / item , folder_path)

    return True



def main():

    organize_directory(path)

main()