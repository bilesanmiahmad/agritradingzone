from django.core.mail import EmailMessage


def send_email():
    email = EmailMessage(
            subject='Hello',
            body='You have registered',
            from_email='hello@agritradingzone.com',
            to=['fbilesanmi@gmail.com'],
            reply_to=['hello@agritradingzone.com'],
            headers={'Content-Type': 'text/plain'},
        )
    email.send()
