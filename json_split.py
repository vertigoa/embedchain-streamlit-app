import json

def split_json(file_path, split_size, output_folder):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in range(0, len(data), split_size):
        chunk = data[i:i + split_size]
        with open(f'{output_folder}/split_conversations_{i//split_size}.json', 'w', encoding='utf-8') as output_file:
            json.dump(chunk, output_file, indent=4)

# Usage
file_path = '/workspaces/embedchain-streamlit-app/conversations.json'  # Your JSON file path
split_size = 20  # Adjust this based on your preference
output_folder = '/workspaces/embedchain-streamlit-app/splits'  # Output folder

split_json(file_path, split_size, output_folder)
