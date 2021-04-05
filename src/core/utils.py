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
    
    @staticmethod
    def get_host_domain(request):
        scheme = 'https' if request.is_secure() else 'http'
        site = request.get_host()
        site_domain = f'{scheme}://{site}'
        return site_domain