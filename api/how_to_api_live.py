import requests

url = "https://randomuser.me/api/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json() # JSON – Javascript object notation
    # data = {'kluc1': 'hodnota1', results: [{}, {}] }
    person = data['results'][0]
    personName = person['name']
    firstName = personName['first']
    lastName = personName['last']

    print("zdravi ta " + firstName + " " + lastName)
else:
    print("Nastala nejaka chyba.")
    print(response)