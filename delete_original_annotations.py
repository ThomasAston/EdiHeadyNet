import os
import fnmatch

HEADER_LENGTH = 4
FOOTER_LENGTH = 6

rootdir ='C:/Users/s1710722/OneDrive - University of Edinburgh/PhD/1. Working/1. Computational/EdiHeadyNet/devkit/europe_uefa-champions-league/2015-2016'
# print(rootdir)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print(os.path.join(subdir, file))
        if fnmatch.fnmatch(file, 'Labels-v2.json'):
            file_dir = os.path.join(subdir, file)
            with open(file_dir, 'r') as f:
                lines = f.readlines()

            with open(file_dir, 'w') as f:
                for line in lines[0:HEADER_LENGTH]:
                    f.write(line)
                for line in lines[-FOOTER_LENGTH:]:
                    f.write(line)