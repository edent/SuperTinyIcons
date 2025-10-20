import os
import xml.etree.ElementTree as ET
import re
import sys
from pathlib import Path

table_columns = 6
img_domain = "https://edent.github.io/SuperTinyIcons/images/svg/"
parent_dir = Path(".").parent.absolute()
svg_dir = f"{parent_dir}/images/svg/"
print(f"Getting SVGs from {svg_dir}")

svg_list = sorted(os.listdir( svg_dir ))
svg_data = {}
total_bytes = 0

#	Set up the tables
readme_table = "<table>\n"

counter = 0
#	Loop through all the SVG data
for svg_file in svg_list:
	name     = ET.parse(f'{svg_dir}{svg_file}').getroot().attrib["aria-label"]
	bytes    = os.stat(f'{svg_dir}{svg_file}').st_size
	total_bytes += bytes

	if counter == 0 :
		readme_table += "<tr>\n"
		
	readme_table += f'<td>{name}<br>'
	readme_table += f'<img src="{img_domain}{svg_file}" width="100" title="{name}"><br>'
	readme_table += f'{bytes} bytes</td>\n'
	
	counter +=1

	if counter == table_columns:
		readme_table += "</tr>\n\n"
		counter = 0
		
if counter != 0 :
		readme_table += "</tr>\n\n"
		
readme_table += "</table>"

#	Calculate the number of icons and average size
readme_summary_text = f"There are currently {len(svg_list)} icons and the average size is _under_ {round(total_bytes / len(svg_list))} bytes!"

#	Replace the table in README with the new one
with open(f"{parent_dir}/README.md",'r+', encoding="utf-8") as f: 
	file = f.read() 
	
	file = re.sub(r"(?s)<table>.*?</table>", readme_table, file)
	file = re.sub(r"There are currently \d* icons and the average size is _under_ \d* bytes\!", readme_summary_text, file) 

	f.seek(0)
	f.write(file)
	f.truncate()