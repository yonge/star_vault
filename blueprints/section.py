import re

# Open the HTML file and read the content
with open('living_here.html', 'r') as f:
    html = f.read()

# Define a regular expression pattern to match section#
pattern = r'section\d+'

# Use re.sub() to find and replace all occurrences of section#
def increment_section(match):
    section = match.group(0)
    section_num = int(section[7:])
    return f'section{section_num+1}'


html = re.sub(r'section7|(section\d+)', increment_section, html) 
# Write the modified HTML back to the file
with open('test.html', 'w') as f:
    f.write(html)

