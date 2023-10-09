import os
import xml.etree.ElementTree as ET
import re

table_length = 6
counter = 0

svg_list = sorted(os.listdir('images/svg/'))
ref_list = sorted(os.listdir('images/reference/'))
ref_files = {}

for ref_file in ref_list:
	if ref_file.endswith('.md'):
		continue
	name, filetype = ref_file.split('.')
	ref_files[name] = { 'filetype': filetype }

total_bytes = 0

table = "<table>\n"
check_table = "-|-\n"
missing_table = "| ** No Reference Image Found **\n"
for svg_file in svg_list:
	svg = svg_file.split('.')[0]
	name = ET.parse(f'images/svg/{svg_file}').getroot().attrib["aria-label"]
	bytes = os.stat(f'images/svg/{svg_file}').st_size
	total_bytes += bytes

	if svg in ref_files:
		ref_file = f"{svg}.{ref_files[svg]['filetype']}"
		check_table += f'<img src="/images/svg/{svg_file}" width="256" /> | <img src="/images/reference/{ref_file}" width="256">\n'
		ref_files.pop(svg)
	else:
		missing_table += f'<img src="/images/svg/{svg_file}" width="256" /> | **?** \n'
		print(f'No reference file found for: {name} [{svg}]')

	if counter == 0 :
		table += "<tr>\n"
		
	table += f'<td>{name}<br>'
	table += f'<img src="/images/svg/{svg_file}" width="100" title="{name}"><br>'
	table += f'{bytes} bytes</td>\n'
	
	counter +=1

	if counter == 6 :
		table += "</tr>\n\n"
		counter = 0
		
if counter != 0 :
		table += "</tr>\n\n"
		
table += "</table>"

summary_text = f"There are currently {len(svg_list)} icons and the average size is _under_ {round(total_bytes / len(svg_list))} bytes!"

with open('README.md','r+') as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)<table>.*?</table>", table, file)
    file = re.sub("There are currently \d* icons and the average size is _under_ \d* bytes\!", summary_text, file) 

    f.seek(0)  
    f.write(file)  
    f.truncate()

print(f"README.md updated with {len(svg_list)} icons.")

with open('CHECK.md','r+') as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)-\|-\|-.*", check_table, file)
    file += missing_table

    file += "**Unused reference files**\n"
    for key in ref_files:
        ref_file = f"{key}.{ref_files[key]['filetype']}"
        file += f'{ref_file} | <img src="/images/svg/{ref_file}" width="256" />\n'

    f.seek(0)  
    f.write(file)  
    f.truncate()
	
print(f"CHECK.md updated.")