import ollama
from PyPDF2 import PdfReader



file_path = "FY24_Q1_Consolidated_Financial_Statements.pdf"
reader = PdfReader(file_path)

text1 = """lease find the value insight in the text and if that insight is not present kindly print the empty string . Output would be like that 
        insight1 : value1
        insight2 : value2
        insight3 : value2
        .......

        insight value are == net sales, total cost of sales , total operating expense,net income from 
"""


def gen_answer(text):
    response = ollama.chat(model='llama3.1', messages=[
    {
    'role': 'user',
    'content': text,
    },
    ])
    print(response['message']['content'])

print("Enter the Question You have in precised way to get better output")
b = input();
gen_answer(b);


def pdf_insight(insigt):
    response = ollama.chat(model='llama3.1', messages=[
    {
    'role': 'user',
    'content': insigt,
    },
    ])
    print(response['message']['content'])

text2="";
for page in reader.pages:
    text2+=page.extract_text()
    text2+=" "

prompt = text1+text2;

pdf_insight(prompt);

