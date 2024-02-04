# copyfile() - copies content
# copy() - copyfile() + permission mode + destination can be a directory
# copy2() - copy() + copies metadata(file creation and modification time)

import shutil

shutil.copyfile('C:\\Users\\91755\\OneDrive\\Desktop\\Test.txt' , 'copy.txt') #source, destination
shutil.copy('C:\\Users\\91755\\OneDrive\\Desktop\\Test.txt' , 'copy.txt')
shutil.copy2('C:\\Users\\91755\\OneDrive\\Desktop\\Test.txt' , 'copy.txt')