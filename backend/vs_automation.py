import os
import requests
GROQ_API_KEY = "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"
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
def generate_code(question):
    headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

    json_data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {
            "role": "system",
            "content": (
                f"generate a apporiate code for the{question} in very presice format add comments to understand the code in python lanuage"
            )
        },
        {
            "role": "user",
            "content": f"{question}"
        }
    ]
}
    response = requests.post(GROQ_ENDPOINT, headers=headers, json=json_data)
    response.raise_for_status()
    result = response.json()
    return result['choices'][0]['message']['content']
def vs_code_sasta_automation(foldername, filename, content):
    default_folder = r"C:\Users\PRERAN S\OneDrive\Desktop\lol_jarvis"
    actuall_complete_path = os.path.join(default_folder, foldername)    
    try:
        os.makedirs(actuall_complete_path, exist_ok=True)
        print("Folder created or exists:", actuall_complete_path)
    except Exception as e:
        print("Error creating folder:", e)
        return    
    safe_filename = filename.replace(" ", "_")
    file_path = os.path.join(actuall_complete_path, f"{safe_filename}.py")
    print("Full file path:", file_path)
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print("File written successfully.")
    except Exception as e:
        print("Error writing file:", e)
        return    
    try:
        os.system(f'code "{file_path}"')  
        print("VS Code command executed.")
    except Exception as e:
        print("Error opening in VS Code:", e)

    return file_path

# task="generate a code for finding prime numbers "
# code = generate_code(task)
# vs_code_sasta_automation("bit", "sastabit", code)



