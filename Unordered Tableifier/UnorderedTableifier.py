from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

text_lines = []
output_filepath = None  # Store the output file path
input_filepath = None  # Store the input file path

def setOutputAsDefaultInput():
    global input_filepath
    global output_filepath
    if var1.get():
        input_filepath = output_filepath
        print("Input file set as the output file:", input_filepath)

def openFile():
    global text_lines
    global input_filepath
    input_filepath = filedialog.askopenfilename()
    if input_filepath:
        with open(input_filepath, 'r') as file:
            contents = file.readlines()
        text_lines.extend(contents)

def process_and_generate_html():
    global output_filepath
    if not output_filepath:
        output_filepath = 'Output.html'  # Set a default output file if not specified
    
    # Create le souppe (parse input as html)
    soup = BeautifulSoup("", "html.parser")

    ul_tag = soup.new_tag("ul")
    soup.append(ul_tag)  # Salt and pepper after taste (add ul opening and closing tags)

    for line in text_lines:
        line = line.strip()  # Clean carrots (remove white spaces around line)
        if line:
            li_tag = soup.new_tag("li")  # Prepare cutlery (make an identifier for the li tags)
            li_tag.string = line
            ul_tag.append(li_tag)  # Add chopped carrots to soup (append the tag to the line)

    # Print and save the result
    print(soup.prettify())

    with open(output_filepath, 'w') as output_file:
        output_file.write(str(soup))

def make_table_from_lines():
    global output_filepath
    global input_filepath
    if not output_filepath:
        output_filepath = 'Output.html'  # Set a default output file if not specified
    
    if not input_filepath:
        print("No input file selected.")
        return
    
    with open(input_filepath, 'r') as file:
        html_content_new = file.read()
    print(input_filepath)
    soup = BeautifulSoup(html_content_new, 'html.parser')

# Find the <ul> element and get its <li> items
    ul = soup.find('ul')
    items = ul.find_all('li')

# Initialize an empty table
    table = soup.new_tag('table')

# Create a table body
    tbody = soup.new_tag('tbody')

    # Iterate through the <li> items and extract specifications and values
    for item in items:
        text = item.get_text()
        
        if ":" in text:
            # Split the line at the first ":" symbol
            spec, value = text.split(":", 1)
            spec = spec.strip()
            value = value.strip()
            
            tr = soup.new_tag('tr')
            
            # Create a table cell for the specification
            td_spec = soup.new_tag('td')
            td_spec.string = spec
            tr.append(td_spec)
            
            # Create a table cell for the value
            td_value = soup.new_tag('td')
            td_value.string = value
            tr.append(td_value)
            
            # Add the row to the table body
            tbody.append(tr)

# Replace the <ul> with the table
    ul.replace_with(table)

    # Add the table body to the table
    table.append(tbody)
    
    # Save the modified HTML to an output file
    with open(output_filepath, 'w') as output_file:
        output_file.write(soup.prettify())

# Create a custom style for your Tkinter widgets
def set_custom_style():
    style = ttk.Style()
    style.configure("TButton", foreground="#232B60", background="#A5A736")  # Adjust color saturation
    style.configure("TFrame", background="#f8f9fb")


Window = Tk()
Window.title("File Processing App")
set_custom_style()
style = ttk.Style()
style.configure("TButton.SS.TButton", foreground="#232B60", background="#A5A736")  # Set text and background colors


# Increase the app size
Window.geometry("655x210")

frame = ttk.Frame(bootstyle = LIGHT, padding=(20, 20, 20, 20))
frame.grid(column=0, row=0, sticky=(N, W, E, S))

message_label = ttk.Label(frame, text="Put your files in me >.<", background="#f8f9fb", foreground="Black", font=("Arial", 14))  # Adjust font size and color
message_label.grid(column=3, row=0)  # Add some padding

buttonFile = ttk.Button(frame, text="Open", command=openFile, bootstyle = PRIMARY)
buttonFile.grid(column=3, row=1, pady=10)

buttonLineToTable = ttk.Button(frame, text="These lines should be a table", command=lambda: make_table_from_lines(), bootstyle = "info-outline")
buttonLineToTable.grid(column=2, row=3, padx=10, pady=10)

buttonLineToTable = ttk.Button(frame, text="This text should be an unordered list", command=lambda: process_and_generate_html(), bootstyle =SUCCESS)
buttonLineToTable.grid(column=4, row=3, padx=10, pady=10)

#debugButton = ttk.Button(frame, text="Print current output to terminal", command=lambda: print(input_filepath), style="TButton.SS.TButton")
#debugButton.grid(column=3, row=5, pady=10)

var1 = IntVar()  # Variable to track the checkbox state
#checkbox = tk.Checkbutton(frame, text='Set output file as input', variable=var1, onvalue=1, offvalue=0, command=setOutputAsDefaultInput)
#checkbox.grid(column=3, row=4, pady=10)
labelCbox = ttk.Label(frame, bootstyle="dark", text="Keep using this file")
labelCbox.grid(column = 3, row = 4)
checkbox = ttk.Checkbutton(frame, bootstyle="light-round-toggle")
checkbox.grid(column = 3, row = 5)
Window.mainloop()
