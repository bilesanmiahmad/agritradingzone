import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/mail.agritradingzone.com/messages",
        auth=("api", ""),
        data={"from": "Excited User <mailgun@mail.agritradingzone.com>",
              "to": ["fbilesanmi@gmail.com", "hello@agritradingzone.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
