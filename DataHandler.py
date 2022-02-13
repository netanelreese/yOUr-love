import mysql.connector

user_db = mysql.connector.connect(
  host="34.122.13.220",
  user="root",
  password="Violentwinds212!",
  database="your_love"
)

cursorObject = user_db.cursor()

# returns a persons answers (array of answers)
def add_data():
    with open('db.toml', 'r') as file:
        curr = file.readlines()
        file.close()
    data = curr[0].split(',')
    query = "INSERT INTO \
        user_data(name, phone, insta, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19,\
                  q20) " \
            "VALUES(" + data[0] + ", " + data[1] + ", " + data[2]
    i = 0
    for val in data:
        if i > 2:
            query+= ", " + str(val)
        i+=1
    query+=");"
    cursorObject.execute(query)
    result = cursorObject.fetchall()
    for x in result:
        print(x)
    return result