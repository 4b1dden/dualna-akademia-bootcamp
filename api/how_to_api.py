# krok 1: kniznica na requesty 

import requests


# url / endpoint

url = 'https://randomuser.me/api/'

# GET / POST / ine parametre (body, headers, ...)

response = requests.get(url)

# ocekovat, ci sa nasa poziadavka uspesne spracovala

if response.status_code == 200:
    # super, mame data, mozeme s nimi robit co chceme
    data = response.json()

    person = data['results'][0]

    print("zdravi ta " + person['name']['first'] + " " + person['name']['last']) 


# pridavanie parametrov

# iba nejake nationality => ?nat=gb

# iba niektore fields => ?inc=gender,name,nat

# spracovavanie dat pomocou funckii
    # def pozdrav(...?): ?

# ako vygenerujeme 10 ludi?
