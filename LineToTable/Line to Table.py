from bs4 import BeautifulSoup

# Read the HTML input from a file in the same directory
with open('input.html', 'r') as file:
    html_input = file.read()

# Parse the input HTML
soup = BeautifulSoup(html_input, 'html.parser')

# Find the <ul> element and get its <li> items
ul = soup.find('ul')
items = ul.find_all('li')

# Initialize an empty table
table = soup.new_tag('table')
tbody = soup.new_tag('tbody')
table.append(tbody)

# Iterate through the <li> items and extract specifications and values
for item in items:
    text = item.get_text()
    
    # Split the text into specification and value by the first ":"
    first_colon_index = text.find(":")
    
    if first_colon_index != -1:
        spec = text[:first_colon_index].strip()
        value = text[first_colon_index + 1:].strip()
    else:
        spec = None
        value = text.strip()
    
    tr = soup.new_tag('tr')
    
    # If 'spec' is not None, create a table cell for specification
    if spec:
        td_spec = soup.new_tag('td')
        td_spec.string = spec
        tr.append(td_spec)
    
    # Always create a table cell for the value
    td_value = soup.new_tag('td')
    td_value.string = value
    tr.append(td_value)
    
    tbody.append(tr)

# Replace the <ul> with the table
ul.replace_with(table)

# Save the modified HTML to an output file
with open('Output.html', 'w') as output_file:
    output_file.write(soup.prettify())

# Print a message to confirm that the file has been saved
print("Modified HTML has been saved to Output.html")
