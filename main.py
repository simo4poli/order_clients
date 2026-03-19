import json

def ordina_clienti():
    with open("clienti.json", "r") as f:
        data = json.load(f)

    return sorted(data, key=lambda x: x["priorita"], reverse=True)

ordinati = ordina_clienti()
def nuovo_aggiungi_e_ordina_per_patrimonio():
    with open("clienti.json", "r") as f:
        data = json.load(f)

    nuovo_cliente = {
        "nome": "Simone",
        "cognome": "Polinori",
        "eta": 22,
        "patrimonio": 500000000.0,
        "priorita": 8
    }

    data.append(nuovo_cliente)

    return sorted(data, key=lambda x: x["priorita"], reverse=True)

ordinati = nuovo_aggiungi_e_ordina_per_patrimonio()


for i in ordinati:
    print(f'nome: {i["nome"]}, cognome: {i["cognome"]}, età: {i["eta"]}, patrimonio: {i["patrimonio"]}, priorità: {i["priorita"]}')

def piu_ricco():
    return sorted(ordinati, key=lambda x: x["patrimonio"], reverse=True)[0]

    return max(data, key=lambda x: x["patrimonio"])
ricco = piu_ricco()
print(f'Il cliente più ricco è {ricco["nome"]} {ricco["cognome"]} con un patrimonio di {ricco["patrimonio"]} euro.')        



