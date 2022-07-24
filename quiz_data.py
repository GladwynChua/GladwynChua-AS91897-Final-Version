import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=hard", params=parameters)
question_data = response.json()["results"]