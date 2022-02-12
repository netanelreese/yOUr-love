from twilio.rest import Client
import toml


account_sid = 'AC75a4dafecc596dab48029922f9ce4ac6'
auth_token =
client = Client(account_sid, auth_token)


def get_phone_number():
    return ""

phone_num = get_phone_number()

def complete():
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body='Thank you for completing our survey! You will get your results shortly :)',
        to=phone_num
    )
    print(message.sid)


