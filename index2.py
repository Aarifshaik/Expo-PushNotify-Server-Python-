import requests
import json
from time import sleep

def send_push_notification(expo_push_token, title, body):
    # Expo push notification endpoint
    url = 'https://exp.host/--/api/v2/push/send'
    
    # Create the notification payload
    payload = {
        'to': expo_push_token,
        'sound': 'default',
        'title': title,
        'body': body,
        'data': {
            'extraData': 'Some extra data here'
        }
    }
    
    # Send the POST request to Expo's push notification service
    response = requests.post(url, headers={
        'Content-Type': 'application/json'
    }, data=json.dumps(payload))
    
    # Print response for debugging purposes
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    return response.json()

# Example usage
if __name__ == '__main__':
    expo_push_token = ""
    title = 'Hi Ashraf!'
    body = 'Ashraf is a good boy'
    while(True):
        response = send_push_notification(expo_push_token, title, body)
        print(response)
        sleep(1)
