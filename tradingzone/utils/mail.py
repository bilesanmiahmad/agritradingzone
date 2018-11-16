from django.core.mail import EmailMessage, EmailMultiAlternatives


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


def send_formatted_email(user):
    subject = "Welcome to Agritradezone"
    from_email = "hello@agritradingzone.com"
    to = user.email
    text_content = "Thank you for joining us at Agri Trading Zone"
    html_content = '<h1> It\'s a pleasure to have you on board.</h1> ' \
                   '<p>Follow <a href=\'https:agritradingzone.herokuapp.com/accounts/' \
                   + user.id + '/verify/\'>this</a> to verify your account.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
