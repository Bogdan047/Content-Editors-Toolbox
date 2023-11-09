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

# Create table headers for the two columns
thead = soup.new_tag('thead')
thead_row = soup.new_tag('tr')
th_spec = soup.new_tag('th')
th_value = soup.new_tag('th')
th_spec.string = 'Specification'
th_value.string = 'Value'
thead_row.append(th_spec)
thead_row.append(th_value)
thead.append(thead_row)
table.append(thead)

# Create a table body
tbody = soup.new_tag('tbody')

# Initialize variables to keep track of the current specification set
current_spec_set = []

# Iterate through the <li> items and extract specifications and values
for item in items:
    text = item.get_text()
    
    if ":" in text:
        # If it contains a colon (":"), it's part of the current specification set
        current_spec_set.append(text)
    elif current_spec_set:
        # If it doesn't contain a colon but there's a current_spec_set, process the set
        spec = current_spec_set[0].split(":")[0].strip()
        values = [line.split(":", 1)[1].strip() for line in current_spec_set]
        
        tr = soup.new_tag('tr')
        
        # Create a table cell for the specification
        td_spec = soup.new_tag('td')
        td_spec.string = spec
        tr.append(td_spec)
        
        # Create a table cell for the values (joining them with line breaks)
        td_value = soup.new_tag('td')
        td_value.string = '\n'.join(values)
        tr.append(td_value)
        
        # Add the row to the table body
        tbody.append(tr)
        
        # Reset the current specification set
        current_spec_set = []

# Replace the <ul> with the table
ul.replace_with(table)

# Add the table body to the table
table.append(tbody)

# Save the modified HTML to an output file
with open('Output.html', 'w') as output_file:
    output_file.write(soup.prettify())

# Print a message to confirm that the file has been saved
print("Modified HTML has been saved to Output.html")
