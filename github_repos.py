from urllib.request import urlopen
import json
response = urlopen('https://api.github.com/users/fall16mis/repos')
data = response.read()
data = json.loads(data)
for i in range(1,len(data)):
    print(data[i]['name'])
