import requests

# Define the URL for the Open Trivia Database API with parameters for 10 boolean-type questions
URL = "https://opentdb.com/api.php?amount=10&type=boolean"
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Send a GET request to the API and retrieve the response data
response = requests.get(URL)
response.raise_for_status()  # Raise an HTTPError if the request was unsuccessful
data = response.json()

# Extract the question data from the response
question_data = data["results"]
