import os
from unittest import result

rootdir = r'/Users/kyle/Documents/GitHub'

substring = "Gemfile"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        project_name = os.path.basename(subdir)
        result_str = ''
        if substring == file:
            if "HOD" not in project_name.upper():
                break
            print(project_name)
            f = os.path.join(subdir, file)
            if os.path.exists(f):
                afile = open(f, "r")
                for line in afile:
                    # checking string is present in line or not
                    if line.startswith('ruby'):
                        result_str += line
                        # print(line)
                    if line.startswith("gem 'rails'"):
                        result_str += line
                        # print(line)
            print(result_str)
            print()
            break
print("done!")
