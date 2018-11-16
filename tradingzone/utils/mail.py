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
    to = [user.email, 'fbilesanmi@gmail.com']
    text_content = "Thank you for joining us at Agri Trading Zone"
    html_content = '<h1>Thank you for joining us at Agri Trading Zone</h1>' \
                   '<p> It\'s a pleasure to have you on board.</p> ' \
                   '<p>Follow <a href=\'https:agritradingzone.herokuapp.com/accounts/' \
                   + user.id + '/verify/\'>this</a> to verify your account.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_formatted_bid_email(bid):
    subject = "You have received a bid from a user"
    from_email = "hello@agritradingzone.com"
    to = ['abd.traore@agritradingzone.com', 'fbilesanmi@gmail.com']
    text_content = "New bid from a user"
    html_content = '<h1>You have received a new bid</h1>' \
                   '<p>The information are as follows:</p>' \
                   '<p>User:' + bid.client.full_name + '</p>' \
                   '<p>Product:' + bid.product.crop.name + '</p>' \
                   '<p>User:' + bid.price + '</p>' \
                   '<p>Follow <a href=\'https:agritradingzone.herokuapp.com/products/bids/' \
                   + bid.id + '\'>this</a> to verify your account.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
