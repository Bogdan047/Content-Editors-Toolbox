

from bs4 import BeautifulSoup


#Consult recipe book (read input file)
with open('input.txt', 'r') as file:
    text_lines = file.readlines()

#Create le souppe (parse input as html)
soup = BeautifulSoup("", "html.parser")

ul_tag = soup.new_tag("ul")
soup.append(ul_tag) #salt and pepper after taste (add ul opening and closing tags)

for line in text_lines:
    line = line.strip() #clean carrots (remove white spaces around line)
    if line:
        li_tag = soup.new_tag("li") #prepare cuttlery (make an identifier for the li tags)
        li_tag.string = line
        ul_tag.append(li_tag) #add chopped carrots to soup (append the tag to the line)



print(soup.prettify())

with open('output.html', 'w') as output_file:
    output_file.write(str(soup))