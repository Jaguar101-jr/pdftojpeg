import os
from pdf2image import convert_from_path

# Function to convert PDF to JPEG
def pdf_to_jpeg(pdf_file, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = convert_from_path(pdf_file)
    for i, image in enumerate(images):
        image.save(f'{output_folder}/page_{i + 1}.jpg', 'JPEG')

# Usage
pdf_file = '/home/path_to_file.pdf'  # Replace with your PDF file path
output_folder = 'output'     # Replace with your desired output folder
pdf_to_jpeg(pdf_file, output_folder)

