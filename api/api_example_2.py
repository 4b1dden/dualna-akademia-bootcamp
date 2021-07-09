# verejne.digital
import requests
from collections import Iterable

meno = "Igor Matovic"
# meno = str(input("meno:"))

def ziskaj_ids(originalny_id_list):
    return map(lambda elem: int(elem['eid']), originalny_id_list)

def vyhladaj_entity_podla_mena(meno):
    resp = requests.get("https://verejne.digital/api/v/searchEntityByName?name={}".format(meno))
    
    if resp.status_code == 200:
        return resp.json()

def informacie_o_entitach(id_list):
    if not isinstance(id_list, Iterable):
        id_list = [id_list]

    url = "https://verejne.digital/api/v/getInfos?eids={}".format(
        ",".join(map(str, ziskaj_ids(id_list)))
    )
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()
    else:
        print("Chyba v ziskavani informacii o entitach.")
        print(resp.text)
        
        return None

ids = vyhladaj_entity_podla_mena("igor matovic")
data = informacie_o_entitach(ids)

def informacie_o_politikovi(id):
    resp = requests.get(" https://verejne.digital/api/k/info_politician?id={}".format(id))
    
    if resp.status_code == 200:
        return resp.json()


def zoznam_politikov():
    url = "https://verejne.digital/api/k/list_politicians?group=active"
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()

def info_o_vybranom_politikovi(politik_id):
    url = "https://verejne.digital/api/k/info_politician?id={}".format(politik_id)
    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()

def vyfiltruj_podla_strany(zoznam_politikov, strana):
    final = []

    for politik in zoznam_politikov:
        if politik['party_abbreviation'] == strana:
            final.append(politik)

    return final

politici = zoznam_politikov()
skrateni = politici[0:20]

print(vyfiltruj_podla_strany(skrateni, "KDH"))
# print(informacie_o_politikovi(40)) # robert fico

# ---------------------------------------------------------------------------------------------------
# napisme kod na vyhladavanie meno -> eids
# napisme kod na eids -> data

# napisme funkciu ziskaj_ids


# napisme funkciu ziskaj vsetkych politikov

# ziskaj vsetkych politikov 
    # vyfiltruj podla strany
    # vyfiltruj podla ... ?



    # napisme a vyuzime funkciu "a_shortest_path"
    
    # to iste v pandas?




# ulohy:
# casto piseme check na 200vku -> ako by sme mohli nas kod zlepsit?