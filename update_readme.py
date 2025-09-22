import os
import xml.etree.ElementTree as ET
import re

table_columns = 6
img_domain = "https://edent.github.io/SuperTinyIcons/"
svg_dir = "images/svg/"
ref_dir = "images/reference/"

svg_list = sorted(os.listdir( svg_dir ))
ref_list = sorted(os.listdir( ref_dir ))
svg_data = {}
total_bytes = 0

#	Loop through all the SVGs
for svg_file in svg_list:
	#	Ignore anything which isn't an .svg
	if not svg_file.endswith('.svg'):
		continue
	#	Replace Windows line endings (CRLF) with Unix (LF)
	with open( svg_dir + svg_file, 'rb' ) as open_file:
		content = open_file.read()
		content = content.replace(  b'\r\n', b'\n')
		#	Remove trailing newline
		content = content.strip()
	with open( svg_dir + svg_file, 'wb' ) as open_file:
		open_file.write(content)
	#	Get the filename of the service. E.g. service.svg
	svg = svg_file.split('.')[0]
	svg_data[svg] = { 'svg_file' : svg_file }
	#	Get the name of the service from the ARIA label
	svg_data[svg]['name'] = ET.parse(f'{svg_dir}{svg_file}').getroot().attrib["aria-label"]
	#	Get the file size
	bytes = os.stat(f'{svg_dir}{svg_file}').st_size
	svg_data[svg]['bytes'] = bytes
	total_bytes += bytes

#	Get all reference images
for ref_file in ref_list:
	if ref_file.endswith('.url'):
		continue
	ref_name = ref_file.split('.')[0]
	if ref_name in svg_data:
		svg_data[ref_name]['ref_file'] = ref_file

#	Get all the reference URls
for ref_url in ref_list:
	if ref_url.endswith('.url'):
		ref_name = ref_url.split('.')[0]
		if ref_name in svg_data:
			svg_data[ref_name]['source'] = open(ref_dir + ref_url, "r").readline().rstrip()

#	Set up the tables
readme_table = "<table>\n"
check_table = '<table><tr><th>Name</th><th>SVG Icon</th><th>Circle Icon</th><th>Reference</th><th>Source</th></tr>\n'
reference_table = "-|-|-|-\n"
missing_table = "<h2>No Reference Image Found</h2>\n\n"
missing_table += "Name | Icon | Filename\n-|-|-\n"

counter = 0
#	Loop through all the SVG data
for svg in svg_data:
	svg_file = svg_data[svg]['svg_file']
	name     = svg_data[svg]['name']
	bytes    = svg_data[svg]['bytes']

	#	Add it to the check table
	check_table += f'<tr><td>{name}</td><td><img src="{img_domain}{svg_dir}{svg_file}" width="100" /></td><td><img src="{img_domain}{svg_dir}{svg_file}" width="100" style="border-radius: 50%;"></td>'

	#	If a reference image exists, add it to the reference table and check table
	if 'ref_file' in svg_data[svg]:
		ref_file = svg_data[svg]['ref_file']
		reference_table += f'{name} | <img src="{img_domain}{svg_dir}{svg_file}" width="256" /> | <img src="{img_domain}{ref_dir}{ref_file}" width="256"> | '
		check_table += f'<td><img src="{img_domain}{ref_dir}{ref_file}" width="100"></td>'

		if 'source' in svg_data[svg]:
			source = svg_data[svg]['source']
			reference_table += source
			check_table += f'<td><a href="{source}">{source}</a></td>'

		reference_table += '\n'
	else:
		#	No reference image. Add it to the missing table
		missing_table += f'{name} | <img src="{img_domain}{svg_dir}{svg_file}" width="256" /> | {svg}.svg \n'

	check_table += '</tr>\n'


	if counter == 0 :
		readme_table += "<tr>\n"
		
	readme_table += f'<td>{name}<br>'
	readme_table += f'<img src="{img_domain}{svg_dir}{svg_file}" width="100" title="{name}"><br>'
	readme_table += f'{bytes} bytes</td>\n'
	
	counter +=1

	if counter == table_columns:
		readme_table += "</tr>\n\n"
		counter = 0
		
if counter != 0 :
		readme_table += "</tr>\n\n"
		
readme_table += "</table>"
check_table += "</table>"

#	Calculate the number of icons and average size
readme_summary_text = f"There are currently {len(svg_list)} icons and the average size is _under_ {round(total_bytes / len(svg_list))} bytes!"

#	Replace the table in README with the new one
with open('README.md','r+', encoding="utf-8") as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)<table>.*?</table>", readme_table, file)
    file = re.sub("There are currently \d* icons and the average size is _under_ \d* bytes\!", readme_summary_text, file) 

    f.seek(0)  
    f.write(file)  
    f.truncate()

print(f"README.md updated with {len(svg_list)} icons.")

#	Replace the tables in the REFERENCE document
with open('REFERENCE.md','r+', encoding="utf-8") as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)-\|-\|-.*", reference_table, file)
    file += missing_table

    f.seek(0)  
    f.write(file)  
    f.truncate()
	
print(f"REFERENCE.md updated.")

#	Replace the table in the CHECK document
with open('CHECK.html','r+', encoding="utf-8") as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)<table>.*?</table>", check_table, file)

    f.seek(0)  
    f.write(file)  
    f.truncate()

print(f"CHECK.html updated.")
