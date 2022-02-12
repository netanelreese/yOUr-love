from twilio.rest import Client
import toml

account_sid = 'AC75a4dafecc596dab48029922f9ce4ac6'
config = toml.load("config.toml")
tokendick = config.get("Twillio")
auth_token = tokendick.get("key")

client = Client(account_sid, auth_token)

# returns a persons answers (array of answers)
def get_answers(name):
    return ""
# returns the persons phone number
def get_phone_number():
    return ""

# return the persons name and instagram handle
def get_person():
    return ""

# returns the persons top 3 matches
def sort(matches):
    pass

# TODO
#
def get_matches():
    matches = [['Blank', 0, 'insta'], ['Blank', 0, 'insta'], ['Blank', 0, 'insta']]  # Name, Percent
    for person in persons:
        answers1 = get_answers(name1)
        answers2 = get_answers(name2)
        num_same = num_same_answers(answers1, answers2)
        if num_same > matches[2][1]:
            matches[3] = [person, num_same, 'insta']
            sort(matches)
    return matches

# returns the number of same answers to 20 questions
def num_same_answers(answers1, answers2):
    num_same = 0
    i = 0
    for answer1 in answers1:
        answer2 = answers2[i]
        if (answer1 == answer2):
            num_same += 1
        i += 1
    return num_same

phone_num = get_phone_number()

def complete():
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body='Thank you for completing our survey! You will get your results shortly :)',
        to='+18177579731'
    )
    print(message.sid)

# returns the text to be sent in matches()
def matches_text(matches):
    return 'Your top 3 matches are:\n1. ' + matches[0][0] + ', Similairity: ' + matches[0][1] + '%, Instagram: ' + \
           matches[0][2] + '\n2. ' + matches[1][0] + ', Similairity: ' + matches[1][1] + '%, Instagram: ' + \
           matches[1][2] + '\n3. ' + matches[2][0] + ', Similairity: ' + matches[2][1] + '%, Instagram: ' + \
           matches[2][2]

# texts the person their matches
def send_matches(text):
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body=text,
        to='+18177579731'
    )
    print(message.sid)

