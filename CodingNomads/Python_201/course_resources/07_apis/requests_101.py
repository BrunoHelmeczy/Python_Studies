import requests

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
request = requests.get(base_url)

type(request.content) # <class 'bytes'>

# query parameters 
params_url = "http://demo.codingnomads.co:8080/tasks_api/tasks?userId=1&complete=true"
req2 = requests.get(params_url)

# chk = request.content.decode('utf-8')
chk = request.json()
type(chk) # dict()

chk.keys()
len(chk)

# query params 2
params_url2 = "http://demo.codingnomads.co:8080/tasks_api/users"

params = {
    "email": "helmeczybruno32@gmail.com"
    # "email": "ryan@codingnomads.co"
}

res = requests.get(params_url2, params = params)

res.json()


# Play around with codingnomads API ----
import pandas as pd

base_url = "http://demo.codingnomads.co:8080/tasks_api"
users = requests.get(base_url + '/users')
df = pd.DataFrame(users.json()['data'])


