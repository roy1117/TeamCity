import time
import os

print('Hello world')
# directory = "build\1_Text_File_Open"
# parent_dir = os.path.dirname(os.path.realpath(__file__))
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# os.chdir(path)
with open('readMe.txt', 'w') as f:
    f.write('readme')
print('finish..!!!!')