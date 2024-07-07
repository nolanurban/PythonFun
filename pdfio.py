from pypdf import PdfReader
from io import StringIO

file = "C:\\Users\\nolan\\Downloads\\Oracle PDF Example.pdf"
pdf_reader = PdfReader(file)
page = pdf_reader.pages[0].extract_text()
str_page = str(page)

string_array = str_page.split('\n')
print(len(string_array))
for i in range(0, len(string_array), 1):
    print(i, " string_array[", i, "] -- ", string_array[i])

# we can leverage this and build it as a function
# it will allow us to see exactly the fields we want and split them how we wish.abs

target_string = string_array[15].split("a")
for t in target_string:
    print("-- ", t)