import requests

# 1) Get users data & print out status / encoding / content
def getUsers():
    users = "http://demo.codingnomads.co:8080/tasks_api/users"
    res = requests.get(users)
    return res.json()['data']


users = "http://demo.codingnomads.co:8080/tasks_api/users"
res = requests.get(users)

res.status_code
res.encoding
res.content


# 2) make list of users emails
data = getUsers()

emails = [d['email'] for d in data]

# 3) add yourself as user with POST request --> validate by refreshing get() in 01)
body = {
    # "id": 592,
    "first_name": "Brúnó", 
    "last_name": "Helmeczy", 
    "email": "helmeczybruno32@gmail.com" 
}

def addUser(body_dict):
    users = "http://demo.codingnomads.co:8080/tasks_api/users"
    res = requests.post(users, json = body_dict)

    print(res.status_code)

addUser(body)

# getUsers()

# 4) PUT request to update your info --> validate by refreshing 01)
def updateUser(body_dict = body):
    users = "http://demo.codingnomads.co:8080/tasks_api/users/592"
    res = requests.put(users, json = body_dict)

    print(res.status_code)
    
updateUser(body)

# 5) DELETE req to remove yourself --> validate
def deleteUser():
    users = "http://demo.codingnomads.co:8080/tasks_api/users/593"
    res = requests.delete(users)

    print(res.status_code)
