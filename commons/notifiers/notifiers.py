#Python
import boto3
from botocore.exceptions import ClientError

#Django
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Models
from .models import NotifierBase


class EmailNotifier(NotifierBase):

    def notify(self, data, user):
        print("======= Notify event", 'Django Email =======')
        subject = 'ALERT @{}! Admin user updated a product'.format(user.username)
        from_email = 'system.catalog@aljovi.com.mx"'
        content = render_to_string(
            'emails/products/update_product.html',
            {'sku': data.sku, 'user': user}
        )

        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()


class EmailAWSSESNotifier(NotifierBase):

    def notify(self, data, user):
        print("======= Notify event", 'AWS SES Email =======')

        aws_region = "us-west-2"
        char_set = "UTF-8"
        sender = "system.catalog@aljovi.com.mx" # This address must be verified with Amazon SES.
        recipient = user.email # If your account is still in the sandbox, this address must be verified.
        subject = 'ALERT @{}! Admin user updated a product'.format(user.username)
        content_html = render_to_string(
            'emails/products/update_product.html',
            {'sku': data.sku, 'user': user}
        )

        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=aws_region)

        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': char_set,
                            'Data': content_html,
                        },
                    },
                    'Subject': {
                        'Charset': char_set,
                        'Data': subject,
                    },
                },
                Source=sender,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])


class WhatsAppNotifier(NotifierBase):

    def notify(self, data, user):
        print("======= Notyfy event", 'WhatsApp =======')