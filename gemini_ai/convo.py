import requests
import sys
import os

def read_api_key():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_dir = os.path.join(script_dir, 'credentials')
    api_key_file = os.path.join(credentials_dir, 'gemini_api.txt')

    with open(api_key_file, 'r') as file:
        api_key = file.read().strip()
    return api_key
api_key = read_api_key()

def gemini_convo(prompt):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=" + api_key
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    if response.status_code == 200:
        #return response_json
        if "content" in response_json["candidates"][0]:
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return 'Problem with the response, please try another prompt.'
    else:
        return None
    
prompt = ' '.join(sys.argv[1:])
#print(prompt)
print(gemini_convo(prompt))