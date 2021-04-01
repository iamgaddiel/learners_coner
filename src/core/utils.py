from django.core.mail import EmailMessage

class Util:

    @staticmethod
    def send_email(data):
        mail = EmailMessage(
            subject=data['subject'], 
            body=data['message'], 
            from_email=data['sender'],
            to=[data['recipient']])
        mail.send()

        print(data['sender'])