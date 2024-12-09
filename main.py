from prompting import gen_answer,pdf_insight;
from PyPDF2 import PdfReader
import os



folder_path = "pdf_folder"

n = int(input("Enter the choice 1 Genereal question 2 for pdf insight: "))

if(n==1):
    text = input("Asq your Question: ");
    gen_answer(text)

elif(n==2):
    print("Printing your insight value wait......")
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
    # Check if the file is a PDF
        if filename.endswith(".pdf"):
            text2=""
            file_path = os.path.join(folder_path, filename)
            print(f"Processing: {filename}")
        
        # Read the PDF
            reader = PdfReader(file_path)
            for page_num, page in enumerate(reader.pages):
                text2 = page.extract_text()
   
        pdf_insight(text2)

else:
    print("Select a valid option")