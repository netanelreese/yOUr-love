from twilio.rest import Client
import toml

account_sid = 'AC75a4dafecc596dab48029922f9ce4ac6'
config = toml.load("config.toml")
tokendick = config.get("Twillio")
auth_token = tokendick.get("key")

client = Client(account_sid, auth_token)

# returns a persons answers
def get_answers():
    return ""
# returns the persons phone number
def get_phone_number():
    return ""

# return the persons name and instagram handle
def get_person():
    return ""

# returns the persons top 3 matches
def get_matches():
    return ""

# returns the number of same answers to 20 questions
def num_same_answers():
    return ""

phone_num = get_phone_number()

def complete():
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body='Thank you for completing our survey! You will get your results shortly :)',
        to='+18177579731'
    )
    print(message.sid)

# returns the text to be sent in matches()
def matches_text():
    return ""

# texts the person their matches
def send_matches():
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body='You matched with',
        to='+18177579731'
    )
    print(message.sid)

