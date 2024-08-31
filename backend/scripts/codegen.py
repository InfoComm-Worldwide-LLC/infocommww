import os
import requests

# Load your Hugging Face API token from an environment variable
HF_API_TOKEN = os.getenv('HF_API_TOKEN')

# Print the API token to verify it's loaded correctly
print(f"Using HF API Token: {HF_API_TOKEN}")

# Define a function to generate code using GPT-Neo
def generate_code(prompt):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    response = requests.post(
        "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B",
        headers=headers,
        json={"inputs": prompt},
    )
    return response.json()

# Example usage
if __name__ == "__main__":
    prompt = "Create a basic React component for a navigation bar."
    generated_code = generate_code(prompt)
    print(generated_code)
