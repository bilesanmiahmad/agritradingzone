import csv
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


def get_countries():
    country_list = []
    with open('country.csv', 'r') as country_csv:
        reader = csv.DictReader(country_csv)
        for row in reader:
            country = [row['3Code'], row['Country']]
            country_list.append(country)

    return country_list
