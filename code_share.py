import csv
import os
from PyPDF2 import PdfFileReader
import json

# Function to extract JSON data from a PDF file
def extract_json_from_pdf(pdf_file):
    # Your code to extract JSON data from the PDF file goes here
    # Replace this with your actual code to extract JSON from the PDF
    # For example, you can use PyPDF2 or any other library for PDF extraction
    # and return the JSON data as a Python dictionary
    json_data = {}  # Replace this with the actual JSON data
    return json_data

# Folder containing the PDF files
pdf_folder = 'path_to_pdf_folder'

# Create a CSV file and write the headers
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['File Name', 'Part Name', 'Header', 'Section Text', 'Component ID', 'Component Text', 'Question Type', 'Part of Question', 'Part of Answer', 'Selected', 'Unselected'])

    # Iterate through the PDF files in the folder
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            file_name = os.path.basename(pdf_file)
            pdf_path = os.path.join(pdf_folder, pdf_file)

            # Extract JSON data from the PDF file
            json_data = extract_json_from_pdf(pdf_path)

            # Iterate through the JSON data and write rows to the CSV
            for part_name, part_data in json_data.items():
                header = part_data['Header']
                section_text = part_data['Section Text']

                for component_id, component_data in part_data['kv_components'].items():
                    question_type = component_data['question_type']
                    component_text = component_data['component_text']
                    part_of_question = component_data.get('part_of_question', '')
                    part_of_answer = component_data.get('part_of_answer', '')
                    selected = ', '.join(component_data.get('selected', []))
                    unselected = ', '.join(component_data.get('unselected', []))

                    # Write a row for each component
                    csv_writer.writerow([file_name, part_name, header, section_text, component_id, component_text, question_type, part_of_question, part_of_answer, selected, unselected])

print("CSV file 'output.csv' has been created.")
