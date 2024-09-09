import os
import xml.etree.ElementTree as ET
import re

table_columns = 6
img_domain = "https://edent.github.io/SuperTinyIcons/"

svg_list = sorted(os.listdir('images/svg/'))
ref_list = sorted(os.listdir('images/reference/'))
svg_data = {}
total_bytes = 0

for svg_file in svg_list:
	if not svg_file.endswith('.svg'):
		continue
	svg = svg_file.split('.')[0]
	svg_data[svg] = { 'svg_file' : svg_file }
	svg_data[svg]['name'] = ET.parse(f'images/svg/{svg_file}').getroot().attrib["aria-label"]
	bytes = os.stat(f'images/svg/{svg_file}').st_size
	svg_data[svg]['bytes'] = bytes
	total_bytes += bytes

for ref_file in ref_list:
	if ref_file.endswith('.url'):
		continue
	ref_name = ref_file.split('.')[0]
	if ref_name in svg_data:
		svg_data[ref_name]['ref_file'] = ref_file

for ref_url in ref_list:
	if ref_url.endswith('.url'):
		ref_name = ref_url.split('.')[0]
		if ref_name in svg_data:
			svg_data[ref_name]['source'] = open("images/reference/" + ref_url, "r").readline()

readme_table = "<table>\n"
check_table = '<table><tr><th>SVG Icon</th><th>Circle Icon</th><th>Reference</th><th>Source</th></tr>\n'
reference_table = "-|-|-\n"
missing_table = "&nbsp; | ** No Reference Image Found ** | &nbsp;\n"

counter = 0
for svg in svg_data:
	svg_file = svg_data[svg]['svg_file']
	name = svg_data[svg]['name']
	bytes = svg_data[svg]['bytes']

	check_table += f'<tr><td><img src="{img_domain}images/svg/{svg_file}" width="100" /></td><td><img src="{img_domain}images/svg/{svg_file}" width="100" style="border-radius: 50%;"></td>'

	if 'ref_file' in svg_data[svg]:
		ref_file = svg_data[svg]['ref_file']
		reference_table += f'<img src="{img_domain}images/svg/{svg_file}" width="256" /> | <img src="{img_domain}images/reference/{ref_file}" width="256"> | '
		check_table += f'<td><img src="{img_domain}images/reference/{ref_file}" width="100"></td>'

		if 'source' in svg_data[svg]:
			source = svg_data[svg]['source']
			reference_table += source
			check_table += f'<td><a href="{source}">{source}</a></td>'

		reference_table += '\n'
	else:
		missing_table += f'<img src="{img_domain}images/svg/{svg_file}" width="256" /> | {name} <br/>*[{svg}]* | \n'

	check_table += '</tr>\n'


	if counter == 0 :
		readme_table += "<tr>\n"
		
	readme_table += f'<td>{name}<br>'
	readme_table += f'<img src="{img_domain}images/svg/{svg_file}" width="100" title="{name}"><br>'
	readme_table += f'{bytes} bytes</td>\n'
	
	counter +=1

	if counter == table_columns:
		readme_table += "</tr>\n\n"
		counter = 0
		
if counter != 0 :
		readme_table += "</tr>\n\n"
		
readme_table += "</table>"
check_table += "</table>"


readme_summary_text = f"There are currently {len(svg_list)} icons and the average size is _under_ {round(total_bytes / len(svg_list))} bytes!"

with open('README.md','r+') as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)<table>.*?</table>", readme_table, file)
    file = re.sub("There are currently \d* icons and the average size is _under_ \d* bytes\!", readme_summary_text, file) 

    f.seek(0)  
    f.write(file)  
    f.truncate()

print(f"README.md updated with {len(svg_list)} icons.")

with open('REFERENCE.md','r+') as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)-\|-\|-.*", reference_table, file)
    file += missing_table

    f.seek(0)  
    f.write(file)  
    f.truncate()
	
print(f"REFERENCE.md updated.")

with open('CHECK.html','r+') as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)<table>.*?</table>", check_table, file)

    f.seek(0)  
    f.write(file)  
    f.truncate()

print(f"CHECK.html updated.")
