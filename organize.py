import os
import shutil

from_dir = "C:/Users/sudha/OneDrive/Documents/Python WHJ/Downloaded images/image_files"
to_dir = "C:/Users/sudha/Downloads"
listOfFiles = os.listdir(from_dir)
# print(listOfFiles)

for filename in listOfFiles:
    name, extension = os.path.splitext(filename)
    if extension == '':
        continue
    if extension in['.pdf']:
        path1 = from_dir + '/' + filename 
        path2 = to_dir + '/' +"pdf_files"
        path3 = to_dir + '/' + "pdf_files" + '/' + filename

        if os.path.exists(path2):
            print("moving" + filename)
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("moving" + filename)
            shutil.move(path1, path3)