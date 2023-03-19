import os
import xml.etree.ElementTree as ET

table_length = 6
counter = 0

svg_list = sorted(os.listdir('images/svg/'))

print("<table>")
for svg in svg_list:
	name = ET.parse('images/svg/'+svg).getroot().attrib["aria-label"]
	if counter == 0 :
		print("<tr>")
	print( "<td>" + name + "<br>" + 
	      '<img src="https://edent.github.io/SuperTinyIcons/images/svg/' + svg + '" width="100" title="' + name + '"><br>' + 
			str( os.stat('images/svg/'+svg).st_size ) +" bytes</td>")
	counter +=1
	if counter == 6 :
		print("</tr>\n")
		counter = 0
if counter != 0 :
		print("</tr>\n")
print("</table>")