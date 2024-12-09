import ollama



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