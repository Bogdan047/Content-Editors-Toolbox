from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap import Style

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
def set_dark_style():
    style = Style('darkly')
    style.configure('TFrame', background='#222222')
    style.configure('TButton', bootstyle = DANGER, font=("Arial", 16, 'bold'))
    style.configure('TButton.primary', background='#A5A736', foreground='#232B60')
    style.configure('TButton.success', background='#28a745', foreground='white')
    style.configure('TButton.info-outline', background='#007BFF', foreground='white')
    style.configure('TLabel', background='#222222', foreground='white')
    style.configure('TCheckbutton', bootstyle= "dark-round-toggle", background='#222222', foreground='white')
    style.map('TButton', background=[('active', '#222222')], foreground=[('active', '#232B60')])
    
def main():
    Window = tk.Tk()
    Window.title("Spyshop Text Convertor")
    global var1
    style = set_dark_style()
    bold_font=('Arial', 14, 'bold')
    frame = ttk.Frame(Window)
    frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    message_label = ttk.Label(frame, bootstyle=LIGHT, foreground='White', background='#222222', font=bold_font, text="Ataseaza fisierul pentru conversie")
    message_label.grid(column=3, row=0, padx = 10, pady =10)

    buttonFile = ttk.Button(frame, bootstyle = DANGER, text="Cauta fisierul", padding=(30, 20), command=openFile)
    buttonFile.grid(column=3, row=1, pady=10)

    buttonLineToTable = ttk.Button(frame, bootstyle = PRIMARY, padding =(40, 50), text="Convertire <li> in tabel", command=make_table_from_lines)
    buttonLineToTable.grid(column=4, row=3, padx=50, pady=50)

    buttonLineToTable = ttk.Button(frame, bootstyle = SUCCESS, padding =(40, 50), text="Convertire text in <li>", command=process_and_generate_html)
    buttonLineToTable.grid(column=2, row=3, padx=50, pady=50)

    var1 = tk.IntVar()
    labelCbox = ttk.Label(frame, text="Pastreaza fisierul convertit in <li> pentru a transforma in tabel")
    labelCbox.grid(column=2, row=4, pady = 10, padx= 5)

    checkbox = ttk.Checkbutton(frame, bootstyle= "success-round-toggle", variable=var1, command=setOutputAsDefaultInput)
    checkbox.grid(column=2, row=5, padx=20, pady=20)
    

    Window.mainloop()

if __name__ == "__main__":
    main()