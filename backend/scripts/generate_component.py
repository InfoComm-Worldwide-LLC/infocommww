import os
import requests

HF_API_TOKEN = os.getenv('HF_API_TOKEN')

def ai_agent_generate_code(prompt):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    response = requests.post(
        "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B",
        headers=headers,
        json={"inputs": prompt},
    )
    result = response.json()
    print(f"AI Response for prompt '{prompt}': {result}")  # Debugging line

    if isinstance(result, list) and 'generated_text' in result[0]:
        generated_text = result[0]['generated_text']
        cleaned_text = generated_text.replace(prompt, '').strip()  # Clean up the output
        return cleaned_text
    else:
        raise Exception("Unexpected response format: ", result)

def create_and_write_file(directory, filename, content):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'w') as file:
        file.write(content)
    print(f"File created: {filepath}")

if __name__ == "__main__":
    tasks = [
        {'directory': '../frontend/src/components', 'filename': 'Navbar.js', 'prompt': "Create a basic React component for a responsive navigation bar with a logo and menu items."},
        {'directory': '../frontend/src/pages', 'filename': 'Home.js', 'prompt': "Create a basic React component for a homepage with a hero section, a title, and a call-to-action button."},
    ]

    for task in tasks:
        generated_code = ai_agent_generate_code(task['prompt'])
        if generated_code:
            create_and_write_file(task['directory'], task['filename'], generated_code)
        else:
            print(f"No content generated for {task['filename']}")
