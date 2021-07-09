import requests

def ziskaj_data(mesto):
    base_url = "https://goweather.herokuapp.com/weather/"
    request_url = base_url + city

    response = requests.get(request_url)

    if response.status_code != 200:
        print("Vyskytla sa nejaka chyba!")
        print(response.text)
        return None
    
    return response


def naformatuj_odpoved(city, data):
    # poriesit krajne pripady?
    current_temperature = data['temperature']
    print("V meste", city, "je dnes", current_temperature, "stupnov Celzia.")
    print("Pozrime sa na predpoved na jednotlive dni.")

    days = data['forecast']
    if days:
        for day in days:
            index = day['day']
            day_temp = day['temperature']

            print("Den " + day['day'] + ":" + " " + day_temp)
            print("     Na tento den si zober: " + priprav_oblecenie(day))

    # ulohy: zmenit den x na meno dnesneho?


def priprav_oblecenie(den):
    # {"day":"1","temperature":"+24 °C","wind":"24 km/h"}
    # uloha :)

    return


def main():
    city = str(input("Pre ktore mesto si prosite predpoved pocasia? Ak nechate pole prazdne, bude to Bratislava. "))

    if city == '': 
        city = "Bratislava"

    data = ziskaj_data(city)
    naformatuj_odpoved(city, data)

# 1: dorob funkciu "priprav_oblecenie"

# 2: poriesit krajne pripady vo funkcii "naformatuj odpoved"

# 3: co sa stane ak napiseme neexistujuce mesto?

# 5: ako spravime, aby sme vzdy napisali plusko pred teplotou?
'''
Den 1: +24 °C
Den 2: +28 °C
Den 3: 26 °C
'''


# 6: extrahujme ziskavanie mesta do samostatnej funkcie