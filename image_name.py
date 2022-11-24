import os
import uuid

path = 'C:/Users/Cansu/Desktop/example_image'

files= os.listdir(path)
print(files)

for file in files:
    filename = str(uuid.uuid4())
    old_file = os.path.join(path, file)
    new_file = os.path.join(path, filename+'.jpg')
    os.rename(old_file, new_file)
    

print(files)