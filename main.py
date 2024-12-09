from prompting import gen_answer,pdf_insight;
from PyPDF2 import PdfReader



file_path = "FY24_Q1_Consolidated_Financial_Statements.pdf"
reader = PdfReader(file_path)

text2="";
for page in reader.pages:
    text2+=page.extract_text()
    text2+=" "

n = int(input("Enter the choice 1 Genereal question 2 for pdf insight: "))

if(n==1):
    text = input("Asq your Question: ");
    gen_answer(text)

elif(n==2):
    print("Printing your insight value wait......")
    pdf_insight(text2)

else:
    print("Select a valid option")