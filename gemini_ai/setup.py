import os
import sys
def save_to_gemini_api_file(data):
    data = str(data)
    folder_path = os.path.join(os.getcwd(), 'credentials')
    file_path = os.path.join(folder_path, 'gemini_api.txt')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, 'w') as file:
        file.write(data)

api_key = sys.argv[1]
save_to_gemini_api_file(api_key)