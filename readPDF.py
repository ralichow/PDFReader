
#this code rusn properly but only renames the first file in the folder and tehn gives teh documetn closed error!!!!

#this code has the date format as dd/mm/yyyy
import fitz
from dateutil.parser import parse
import os

# Get the path of the folder containing the PDFs
pdf_folder = 'E:/PYTHON/dummyData/'

# Iterate over all files in the folder
for file_name in os.listdir(pdf_folder):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(pdf_folder, file_name)
    	
        # Open the PDF file in binary mode
        with fitz.open(file_path) as pdf_file:

            # Extract text from all pages of the PDF
            text = ''
            for page_num in range(pdf_file.page_count):
                page = pdf_file.load_page(page_num)
                text += page.get_text()

            # Search for dates in the text
            dates = []
            for word in text.split():
                try:
                    date = parse(word, fuzzy=True)
                    if len(word) == 10 or len(word) == 11:
                        dates.append(date)
                
                except (ValueError, OverflowError):
                    # Handle the error and continue to the next value
                    pass
           
        # Rename the PDF file to the first date found
        if dates:
            new_name = dates[0].strftime('%d-%m-%y ') + file_name
            os.rename(file_path, os.path.join(pdf_folder, new_name))
            print(f'The file {file_name} has been renamed to {new_name}.')
        else:
            print(f'No dates were found in the PDF {file_name}.')


            #Finally it workss!!!!!!!!