import json
from datetime import datetime

def save_form_submission(data):
    # Path to save the data
    file_path = '/path/to/data/user_data/submissions.json'
    
    # Add timestamp to the data
    data['timestamp'] = datetime.utcnow().isoformat()
    
    # Load existing data
    try:
        with open(file_path, 'r') as file:
            submissions = json.load(file)
    except FileNotFoundError:
        submissions = []

    # Add the new submission
    submissions.append(data)
    
    # Save the updated data
    with open(file_path, 'w') as file:
        json.dump(submissions, file, indent=4)

# Example data from a form
form_data = {
    'user_id': '123',
    'feedback': 'Great website!'
}

save_form_submission(form_data)
