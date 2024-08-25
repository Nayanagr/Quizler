import requests
params = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php",params=params)
data = data.json()["results"]
question_data = data