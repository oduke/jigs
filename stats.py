import os
import shutil

basedir = "data/"

def compress(str, dict):
    for c in str:
        if c not in dict:
            dict[c] = 0;
        else:
            dict[c] += 1;
    return dict;

table = {}
maxLen = 0

for id in os.listdir(basedir):
    with open(os.path.join(basedir,id), 'r') as file:
        contents = file.read()
        maxLen = maxLen if (maxLen > len(contents)) else len(contents)
        table = compress(contents,table)

print("Max number of characters: %d"%maxLen)
print("Table:")
for entry in table:
    print(entry)
