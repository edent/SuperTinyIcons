import os
import xml.etree.ElementTree as ET
import re
import sys

#	Colour for console text.
class terminal:
	OK   = '\033[92m'
	WARN = '\033[93m'
	FAIL = '\033[91m'

svg_dir = "images/svg/"
ref_dir = "images/reference/"

svg_list = sorted(os.listdir( svg_dir ))
ref_list = sorted(os.listdir( ref_dir ))
svg_data = {}
total_bytes = 0
success = True

#	Loop through all the SVGs
for svg_file in svg_list:
	#	Ignore anything which isn't an .svg
	if not svg_file.endswith('.svg'):
		continue
	#	Is this a valid SVG?
	try:
		ET.parse( svg_dir + svg_file )
	except Exception as err:
		print( f"{terminal.FAIL}❌ {svg_file} is not valid: {err}")
		success = False
	#	Check and correct common whitespace issues.
	with open( svg_dir + svg_file, 'r', encoding="utf-8" ) as open_file:
		content = open_file.read()
		#	Replace Windows line endings (CRLF) with Unix (LF)
		content = content.replace('\r\n', '\n')
		#	Replace double spaces with single space.
		content = content.replace('  ', ' ')
		#	Replace space newline with newline
		content = content.replace(' \n', '\n')
		#	Remove trailing newline
		content = content.strip()
		#	Check the file contents are in the right order.
		lines = content.splitlines()
		#	Check aria-label.
		if ( lines[1].startswith("aria") is False ):
			print(f"{terminal.WARN}⚠️  Layout: {svg_file} aria-label not in expected place.")
			success = False
		#	Check viewBox (exception for DuckDuckGo).
		if ( lines[2].startswith('viewBox="0 0 512 512"') is False and svg_file != "duckduckgo.svg"):
			success = False
			print(f"{terminal.WARN}⚠️  Layout: {svg_file} viewBox not in expected format.")
	#	Save the corrected file
	with open( svg_dir + svg_file, 'w' ) as open_file:
		open_file.write(content)
	#	Get the filename of the service. E.g. service.svg
	svg = svg_file.split('.')[0]
	svg_data[svg] = { 'svg_file' : svg_file }
	#	Get the file size
	bytes = os.stat(f'{svg_dir}{svg_file}').st_size
	svg_data[svg]['bytes'] = bytes
	if (bytes > 1023):
		print( f"{terminal.FAIL}❌ {svg_file} is {bytes} bytes. Files must be under 1,024 Bytes.")
		success = False
	total_bytes += bytes
	#	Check for reference URl
	service = svg_file[:-4]
	ref_url = service + ".url"
	if ref_url not in ref_list:
		success = False
		print(f"{terminal.WARN}⚠️  Reference URl file: {ref_url} should exist in {ref_dir}")
	#	Check for reference image
	ref_imgs = [ service + ".png", service + ".jpg", service + ".svg", service + ".ico", service + ".webp" ]
	if [img for img in ref_imgs if img in ref_list] == []:
		success = False
		print(f"{terminal.WARN}⚠️  Reference image: {ref_imgs[0]} should exist in {ref_dir}")

if success:
	print( f"{terminal.OK}✅ All files in the correct format and under 1,024 Bytes.")
