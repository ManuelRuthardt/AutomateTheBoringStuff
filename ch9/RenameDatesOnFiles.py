# Create 20 files with random american style dates in the beginning (MM-DD-YYYY)
# Regex for eu style ([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))
# Regex for US style (0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-([12]\d{3})

# Create a regex that can identify the text pattern of American-style dates.

# Call os.listdir() to find all the files in the working directory.

# Loop over each filename, using the regex to check whether it has a date.

# If it has a date, rename the file with shutil.move().    (YYYYMMDD )

import os
#import send2trash
import re
import shutil

# os.makedirs('D:\\coding\\AutomateTheBoringStuff\\ch9\\files')
# print(os.path.relpath('D:\\coding\\AutomateTheBoringStuff\\ch9\\files'))

# lets create the files with US file date system
# for date_files in range(20):
#    rn_files = open('08-%s-2019_logfiles.txt' % (date_files + 1), 'w')

regx = r'(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-([12]\d{3})'


# for filename in os.listdir():
#    shutil.copyfile('D:\\coding\\AutomateTheBoringStuff\\ch9\\' +
#                    filename, 'D:\\coding\\AutomateTheBoringStuff\\ch9\\save\\' + filename)
#    print("copied: " + filename + "to: save")

for filename in os.listdir():
    if re.search(regx, filename):
        print(filename)
        os.rename('D:\\coding\\AutomateTheBoringStuff\\ch9\\' + filename, )
