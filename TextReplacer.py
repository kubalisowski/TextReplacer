import os
import re

filepath = []
find = input('FIND: ')
replace = input('REPLACE: ')


for path, dir, file in os.walk('./files'):
    if len(file) != 0:
        filepath.append(path + '/' + file[0])


for file in filepath:
    with open(file) as f:
        fread = f.read()
        if re.search(find, fread):
            reg = re.compile(find, re.IGNORECASE)
            fread = reg.sub(replace, fread)
            f.close()
    with open(file, 'w') as w:
        w.write(fread)
        w.close()

print('DONE')

