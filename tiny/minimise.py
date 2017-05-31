import glob
import os
import re

with open('../README.md', 'r') as file:
    readme = file.read()

for file_name in glob.glob("*.svg"):
    print(file_name)
    re_string = r'(?<=<td><img src="https:\/\/edent\.github\.io\/SuperTinySocialIcons\/tiny\/{}" width="125" \/><br>)([0-9]*)(?= Bytes<\/td>)'.format(file_name)
    statinfo = os.stat(file_name).st_size
    print(statinfo)
    readme = re.sub(re_string, '{}'.format(statinfo), readme)
    
with open('../README.md', 'w') as file:
    file.write(readme)