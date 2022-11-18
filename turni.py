import pymongo
from bson.objectid import ObjectId
from pymongo.cursor import Cursor
from datetime import date, timedelta
import pandas as pd
import random


mongo = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo['fidelpol']

servizi = db['servizio']
agenti = db['agente']
agenti_servizi = db['agente_servizio']

cache_servizi = {}
cache_servizi_agente = {}

assegnazioni = set()


def populate():
    s = {
        'descrizione': 'FIRENZE 6-14',
        'tipo': 'mattina'
    }
    x = servizi.insert_one(s)
    mylist = [
        {
            'agente_id': ObjectId('6377554424f173de8f26f157'),
            'servizio_id': x.inserted_id
        }
    ]
    agenti_servizi.insert_many(mylist)


def get_agenti_by_servizio(servizio: dict) -> Cursor:
    return agenti_servizi.find({ 'servizio_id': servizio.get('_id') })


def get_agente(_id: ObjectId) -> dict:
    return agenti.find_one({"_id": _id})


def get_servizio(sid: str) -> dict:
    if sid in cache_servizi:
        return cache_servizi[sid]
    else:
        _id = ObjectId(sid)
        servizio = servizi.find_one({"_id": _id})
        cache_servizi[sid] = servizio
        return servizio


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_settimana():
    start_date = date(2022, 11, 21)
    end_date = date(2022, 11, 28)
    return [x.strftime('%Y-%m-%d') for x in daterange(start_date, end_date)]


def get_nd():
    return []
    """
    risultati = [
        ('2022-11-24', ObjectId('63775524d8cdd85258d64216')), # ROSSI MARIO
        ('2022-11-22', ObjectId('63775524d8cdd85258d64217')), # PICA PIERPAOLO
        ('2022-11-23', ObjectId('6377554424f173de8f26f157')), # ALIGHIERI DANTE
        ('2022-11-24', ObjectId('6377554424f173de8f26f158')) # POLO MARCO
    ]
    return risultati
    """


def app():
    # populate()
    # Recupera la settimana lavorativa
    settimana = get_settimana()

    # Recupera tutti gli agenti attivi
    agenti_attivi = list(agenti.find({}, { '_id': 1, 'nome': 1, 'cognome': 1}))
    # Genera una lista piu' veloce solo con gli _id per un lookup rapido
    agente_indice = [x.get('_id') for x in agenti_attivi]

    # Genera la tabella dei turni vuota
    tabella_turni = []
    for i in agenti_attivi:
        tabella_turni.append(['' for x in range(7)])

    # Popola la tabella con i giorni fissi (riposi, ferie, malattie, ecc)
    for item in get_nd():
        idx_agente = agente_indice.index(item[1])
        idx_giorno = idx_giorno = settimana.index(item[0])
        tabella_turni[idx_agente][idx_giorno] = '--------'
        assegnazioni.add(item)

    # Stabilisci i servizi da coprire

    servizi_da_coprire = servizi.find({}, {'_id': 1})
    servizi_da_coprire = [x.get('_id') for x in servizi_da_coprire]

    for giorno in settimana:
        for sid in servizi_da_coprire:
            # Recupera gli agenti che potrebbero svolgere il servizio

            servizio = get_servizio(sid)

            if sid in cache_servizi_agente:
                agenti_servizio = cache_servizi_agente[sid]
            else:
                agenti_servizio = list(get_agenti_by_servizio(servizio))
                cache_servizi_agente[sid] = agenti_servizio

            # random.shuffle(agenti_servizio)   

            if len(agenti_servizio) > 0:
                for x in agenti_servizio:
                    agente_id = x.get('agente_id')

                    # Marca nelle assegnazioni l'agente per evitare passaggi doppi
                    t1 = (giorno, agente_id)

                    # Indici necessari al posizionamento in tabella
                    idx_agente = agente_indice.index(agente_id)
                    idx_giorno = settimana.index(giorno)

                    # Verifica se l'utente e' disponibile quel giorno
                    if t1 not in assegnazioni:
                        assegnazioni.add(t1)
                        tabella_turni[idx_agente][idx_giorno] = servizio.get('descrizione').rjust(15)
                        break

    
    print(pd.DataFrame(tabella_turni, columns=settimana, index=[f"{x.get('cognome')} {x.get('nome')}" for x in agenti_attivi]))


if __name__ == '__main__':
    app()