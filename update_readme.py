import os
import xml.etree.ElementTree as ET
import re

table_length = 6
counter = 0

svg_list = sorted(os.listdir('images/svg/'))
total_bytes = 0

table = "<table>\n"
for svg in svg_list:
	name = ET.parse('images/svg/'+svg).getroot().attrib["aria-label"]
	bytes = os.stat('images/svg/'+svg).st_size
	total_bytes += bytes

	if counter == 0 :
		table += "<tr>\n"
		
	table += f"<td>{name}<br>"
	table += f"<img src=\"https://edent.github.io/SuperTinyIcons/images/svg/\"{svg} width=\"100\" title=\"{name}\"><br>"
	table += f"{bytes} bytes</td>\n"
	
	counter +=1

	if counter == 6 :
		table += "</tr>\n\n"
		counter = 0
		
if counter != 0 :
		table += "</tr>\n\n"
		
table += "</table>\n"

summary_text = f"There are currently {len(svg_list)} icons the average size is _under_ {round(total_bytes / len(svg_list))} bytes!"

with open('README.md','r+') as f: 
    file = f.read() 
	
    file = re.sub(r"(?s)<table>.*?</table>", table, file)
    file = re.sub("There are currently \d* icons and the average size is _under_ \d* bytes\!", summary_text, file  ) 

    f.seek(0)  
    f.write(file)  
    f.truncate()
	
print(f"README.md updated with {len(svg_list)} icons.")