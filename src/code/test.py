import os

path = os.getcwd()
print(path)
files = os.listdir(path=path[:-4] + 'text')
print(files)
