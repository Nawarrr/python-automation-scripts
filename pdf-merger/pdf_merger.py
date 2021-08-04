from pathlib import Path

from PyPDF2 import PdfFileMerger


current_path = Path.cwd()
def pdf_pathes():
    """
    returns list of paths of file taken from input --> list 
    """
    file_names_input =input("Enter file names separated with spaces")
    file_names_list = file_names_input.split()
    files_paths = []

    for name in file_names_list:
        files_paths.append(str(current_path / name))
        
    return files_paths

def merger(file_paths):
    """
    args : paths of pdfs to be merged --> list
    returns None 
    """
    merger = PdfFileMerger()
    for path in file_paths :
        merger.append(path)
    merger.write(str(current_path  / 'merged.pdf'))
    
    return merger.close()



def main():
    pdf_paths = pdf_pathes()
    merger(pdf_paths)
    print("Done Merging")
    return


main()