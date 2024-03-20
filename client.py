import requests
import json

# Define the URL for the Flask endpoint
url = 'http://127.0.0.1:5000/predict'

# Define the JSON data with all 5 features
data = {
    "feature1": 1.5,
    "feature2": 2.0,
    "feature3": 0.5,
    "feature4": -1.0,
    "feature5": 3.2
}

# Convert the data to JSON format
json_data = json.dumps(data)

# Set the content type header to application/json
headers = {'Content-Type': 'application/json'}

# Make the POST request
response = requests.post(url, data=json_data, headers=headers)

# Print the response
print(response.text)
