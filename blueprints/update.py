import re

# Open the HTML file and read its contents
with open("living_here.html", "r") as file:
    html_doc = file.read()

# Search for the string "countinteger" and increment the integer by 1 after the first 5 occurrences
count = 0
pattern = re.compile(r'section(\d+)')
result = pattern.sub(lambda match: f"section{int(match.group(1))+2}" if count >= 19 else match.group(0), html_doc)

# Write the modified HTML document back to the file
with open("filename.html", "w") as file:
    file.write(result)
