import requests

endpoint = 'https://api.mynotifier.app'
apikey = 'Your MyNotifier App Api Key'
message = "Sender"
description = "Content"

requests.post(endpoint, {
    "apiKey" : apikey,
    "message" : message,
    "description" : description,
    "type" : "success" #info, error, warning ve success 
})