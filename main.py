import json

def ordina_clienti():
    with open("clienti.json", "r") as f:
        data = json.load(f)

    return sorted(data, key=lambda x: x["priorita"], reverse=True)

ordinati = ordina_clienti()

for i in ordinati:
    print(f'nome: {i["nome"]}, cognome: {i["cognome"]}, età: {i["eta"]}, patrimonio: {i["patrimonio"]}, priorità: {i["priorita"]}')