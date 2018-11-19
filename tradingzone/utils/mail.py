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
                   '<p> It\'s a pleasure to have you on board, ' + user.first_name + '.</p> ' \
                   '<p>Follow <a href=\'https://agritradingzone.herokuapp.com/accounts/' \
                   + str(user.id) + '/verify/\'>this</a> to verify your account.</p>'
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
                   '<p>User: ' + bid.client.get_full_name + '</p>' \
                   '<p>Product: ' + bid.product.crop.name + '</p>' \
                   '<p>Bid Price: ' + bid.price + '</p>' \
                   '<p>Follow <a href=\'https://agritradingzone.herokuapp.com/products/bids/' \
                   + str(bid.id) + '\'>this</a> to view full details.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_formatted_user_bid_email(bid):
    subject = "Your have received a bid from a user"
    from_email = "hello@agritradingzone.com"
    to = [bid.client.email, 'fbilesanmi@gmail.com']
    text_content = "Your bid has been received"
    html_content = '<h1>Your bid has been received.</h1>' \
                   '<p>We would inform you shortly if your bid ' \
                   'has been accepted or rejected</p>' \
                   '<p>Thank you for using Agri Trading Zone</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_formatted_sale_email(sale):
    subject = "You have received a new product sale from a user"
    from_email = "hello@agritradingzone.com"
    to = ['abd.traore@agritradingzone.com', 'fbilesanmi@gmail.com']
    text_content = "New bid from a user"
    html_content = '<h1>You have received a product sale from ' + sale.seller.first_name + '.</h1>' \
                   '<p>The information are as follows:</p>' \
                   '<p>User: ' + sale.seller.first_name + '</p>' \
                   '<p>Product: ' + sale.crop + '</p>' \
                   '<p>Price: ' + sale.price + '</p>' \
                   '<p>Follow <a href=\'https://agritradingzone.herokuapp.com/products/sales/' \
                   + str(sale.id) + '\'>this</a> to view full details.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_formatted_user_sale_email(sale):
    subject = "Your product has been received."
    from_email = "hello@agritradingzone.com"
    to = [sale.seller.email, 'fbilesanmi@gmail.com']
    text_content = "Your Product has been received"
    html_content = '<p>Hello ' + sale.seller.first_name + ', </p>' \
                   '<p>Your product has been received and we will get in touch with you shortly.</p>' \
                   '<p>Thank you for using Agri Trading Zone.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_formatted_user_bid_accepted_email(bid):
    subject = "Your bid has been accepted."
    from_email = "hello@agritradingzone.com"
    to = [bid.client.email, 'fbilesanmi@gmail.com']
    text_content = "Your bid was accepted"
    html_content = '<p>Congratulations, ' + bid.client.first_name + ', </p>' \
                   '<p>Your bid has been accepted and we will get in touch with you shortly.</p>' \
                   '<p>Thank you for using Agri Trading Zone.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_formatted_user_bid_rejected_email(bid):
    subject = "Sorry, your bid was been rejected."
    from_email = "hello@agritradingzone.com"
    to = [bid.client.email, 'fbilesanmi@gmail.com']
    text_content = "Your bid was rejected"
    html_content = '<p>We are sorry, ' + bid.client.first_name + ', </p>' \
                   '<p>Your bid was rejected and we will be able to ' \
                   'continue the transaction.</p>' \
                   '<p>You can check out our other products that you may be interested in.</p>' \
                   '<p>Thank you for using Agri Trading Zone.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
