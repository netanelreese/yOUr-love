from twilio.rest import Client
import toml
import mysql.connector

user_db = mysql.connector.connect(
  host="34.122.13.220",
  user="root",
  password="Violentwinds212!"
)

print(user_db)

account_sid = 'AC75a4dafecc596dab48029922f9ce4ac6'
config = toml.load("config.toml")
tokendic = config.get("Twillio")
auth_token = tokendic.get("key")

client = Client(account_sid, auth_token)

# returns a persons answers (array of answers)
def get_answers(name):
    return ""
# returns the persons phone number
def get_phone_number():
    return ""

# return the persons instagram handle
def get_insta():
    return ""

# returns the persons top 3 matches
def sort(matches):
    pass

# TODO
#
def get_matches(name1):
    matches = [['Blank', 0, 'insta'], ['Blank', 0, 'insta'], ['Blank', 0, 'insta']]  # Name, Percent
    for name2 in persons:
        answers1 = get_answers(name1)
        answers2 = get_answers(name2)
        num_same = num_same_answers(answers1, answers2)
        if num_same > matches[2][1]:
            matches[3] = [name2, num_same, get_insta()]
            sort(matches)
    return matches

# returns the percent of number of same answers to 20 questions
def num_same_answers(answers1, answers2):
    num_same = 0
    i = 0
    for answer1 in answers1:
        answer2 = answers2[i]
        if (answer1 == answer2):
            num_same += 1
        i += 1
    return num_same / 20.0

phone_num = get_phone_number()

def complete():
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body='Thank you for completing our survey! You will get your results shortly :)',
        to='+18177579731'
    )
    print(message.sid)

# returns the text to be sent in send_matches(text)
def matches_text(matches):
    return 'Your top 3 matches are:\n1. ' + matches[0][0] + ', Similairity: ' + str(matches[0][1]) + '%, Instagram: ' \
           + matches[0][2] + '\n2. ' + matches[1][0] + ', Similairity: ' + str(matches[1][1]) + '%, Instagram: ' + \
           matches[1][2] + '\n3. ' + matches[2][0] + ', Similairity: ' + str(matches[2][1]) + '%, Instagram: ' + \
           matches[2][2]

# texts the person their matches
def send_matches(text):
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body=text,
        to='+18177579731'
    )
    print(message.sid)

