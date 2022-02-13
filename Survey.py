from twilio.rest import Client
import toml
import mysql.connector

user_db = mysql.connector.connect(
  host="127.0.0.1",
  user="phpmyadmin",
  database="user_data"
)

account_sid = 'AC75a4dafecc596dab48029922f9ce4ac6'
config = toml.load("config.toml")
tokendic = config.get("Twillio")
auth_token = tokendic.get("key")

client = Client(account_sid, auth_token)

cursorObject = user_db.cursor()

# returns a persons answers (array of answers)
def get_table():
    query = "SELECT * FROM user_data"
    cursorObject.execute(query)
    result = cursorObject.fetchall()
    for x in result:
        print(x)
    return result

user_data = get_table()

# returns the persons phone number
def get_phone_number(user):
    return user[1]

# return the persons instagram handle
def get_insta(user):
    return user[2]

# returns the persons name
def get_name(user):
    return user[0]

# sorts the array with insertion sort
def sort(arr):
    if arr[2][1]>arr[1][1]:
        temp = arr[2]
        arr[2] = arr[1]
        arr[1] = temp
    if arr[1][1]>arr[0][1]:
        temp = arr[1]
        arr[1] = arr[0]
        arr[0] = temp


# TODO
#
def get_answers(user):
    return ""


def get_matches():
    for user1 in user_data:
        matches = [['Blank', 0, 'insta'], ['Blank', 0, 'insta'], ['Blank', 0, 'insta']]  # Name, Percent
        for user2 in user_data:
            if user1 != user2:
                num_same = num_same_answers(user1, user2)
                if num_same > matches[2][1]:
                    matches[2] = [get_name(user2), num_same, get_insta(user2)]
                    sort(matches)
        #send_matches(matches_text(matches), get_phone_number(user1))
        print(matches_text(matches))
        print(get_phone_number(user1))
        print(get_name(user1))

# returns the percent of number of same answers to 20 questions
def num_same_answers(answers1, answers2):
    num_same = 0
    i = 0
    for answer1 in answers1:
        answer2 = answers2[i]
        if (answer1 == answer2):
            num_same += 1
        i += 1
    return 100 * num_same / 20.0

#phone_num = get_phone_number()

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
def send_matches(text, phone_number):
    message = client.messages.create(
        messaging_service_sid='MGc8bc55077da9aebfdc146d03c77e3aa2',
        body=text,
        to=phone_number
    )
    print(message.sid)

get_matches()
