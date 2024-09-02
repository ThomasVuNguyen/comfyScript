import os
import ollama
class tinyllama:
    def __init__(self):
        print('tinyllama engaged')
    
    def ask(self, query):
        
        #os.system('comfy oled think')

        stream = ollama.chat(
            model='tinyllama',
            messages=[{'role': 'user', 'content': query}],
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)