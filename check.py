# /// script
# dependencies = [
#   "requests",
# ]
# ///

#	Run with either:
#	uv run check.py
#	or
#	python3 check.py

import atexit
import os
import re
import requests
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

#	Colour for console text.
class terminal:
	OK   = '\033[92m'
	WARN = '\033[93m'
	FAIL = '\033[91m'

#	Flag
success = True

#	File Locations
svg_dir = Path(__file__).parent / "images" / "svg/"
ref_dir = Path(__file__).parent / "images" / "reference/"

#	Start the Nu Validator server
if not shutil.which("java"):
	raise RuntimeError("Java not found. Please install it or add it to PATH.")

jar_dir = Path(__file__).parent / "test" / "vnu.jar"
jar_port = 8888
server = subprocess.Popen(
	[
		"java",
		"-cp", str(jar_dir),
		"nu.validator.servlet.Main",
		str(jar_port)
	],
	stdout=subprocess.DEVNULL,
	stderr=subprocess.DEVNULL,
)
#	Terminate on exit
atexit.register(server.terminate)

#	Wait for the server to start
url = f"http://localhost:{jar_port}/"
for _ in range(50):
	try:
		requests.get(url, timeout=0.5)
		break
	except requests.ConnectionError:
		time.sleep(0.5)
else:
	server.terminate()
	success = False
	raise RuntimeError("Validator did not start in time")

#	Validator needs to be supplied with HTML
html_boilerplate = '<!doctype html><html lang="en"><head><title>test</title></head><body>'
#	Validator options
url = f"http://localhost:{jar_port}/?out=gnu"
headers = {"Content-Type": "text/html; charset=utf-8"}

#	Files
svg_list = sorted(os.listdir( svg_dir ))
ref_list = sorted(os.listdir( ref_dir ))
svg_data = {}
total_bytes = 0

#	Loop through all the SVGs
for svg_file in svg_list:
	#	Ignore anything which isn't an .svg
	if not svg_file.endswith('.svg'):
		print(f"{terminal.WARN}⚠️  Filetype: {svg_file} does not end with .svg")
		success = False
		continue
	#	Is this a valid SVG?
	try:
		ET.parse( svg_dir / svg_file )
	except Exception as err:
		print( f"{terminal.FAIL}❌ {svg_file} is not valid: {err}")
		success = False
	#	Check and correct common whitespace issues.
	with open( svg_dir / svg_file, 'r', encoding="utf-8" ) as open_file:
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
	#	Validate against Nu
	html = html_boilerplate + content
	#	Send to Nu
	response = requests.post(url, headers=headers, data=html.encode("utf-8"))
	if len(response.text) > 0:
			print( f"{terminal.FAIL}❌ {svg_file} errors: {response.text}")
			success = False
	#	Save the corrected file
	with open( svg_dir / svg_file, 'w' ) as open_file:
		open_file.write(content)
	#	Get the filename of the service. E.g. service.svg
	svg = svg_file.split('.')[0]
	svg_data[svg] = { 'svg_file' : svg_file }
	#	Get the file size
	bytes = os.stat(f'{svg_dir}/{svg_file}').st_size
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

#	Shut down the Nu Validator
server.terminate()