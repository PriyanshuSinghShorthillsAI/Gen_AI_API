import ollama


text1 = """please find the value insight in the text and if that insight is not present kindly print the empty string . Output would be like that 
        insight1 : value1
        insight2 : value2
        insight3 : value2
        .......

        insight value can be anything like  net sales, total cost of sales , total operating expense,net income or any things which u think is important if company 
       name is present also mention that  from given text = 
"""


def gen_answer(text):
    response = ollama.chat(model='llama3.1', messages=[
    {
    'role': 'user',
    'content': text,
    },
    ])
    print(response['message']['content'])


def pdf_insight(insigt):
    prompt = text1+insigt
    response = ollama.chat(model='llama3.1', messages=[
    {
    'role': 'user',
    'content': prompt,
    },
    ])
    print(response['message']['content'])


