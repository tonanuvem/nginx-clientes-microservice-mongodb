from datetime import datetime
from flask import jsonify, make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

from pymongo import MongoClient
#from bson import json_util
#import json

client = MongoClient("mongodb://localhost:27017/") # Local
#client = MongoClient("mongodb://mong:27017/") # Docker
db = client.tododb

def get_dict_from_mongodb():
    """ # Modelo dos dados
    PEOPLE = {
        "Jones": {
            "fname": "Indiana",
            "lname": "Jones",
            "timestamp": get_timestamp(),
        },
        " Sparrow": {
            "fname": "Jack",
            "lname": " Sparrow",
            "timestamp": get_timestamp(),
        },
        "Snow": {
            "fname": "John",
            "lname": "Snow",
            "timestamp": get_timestamp(),
        },
    }
    """
    itens_db = db.clientes.find()
    itens = []
    #PEOPLE = []
    PEOPLE = {}
    for i in itens_db:
            i.pop('_id') # retira id: criado automaticamente pelo mongodb
            itens.append(i)
            #print(i)
            item = dict(i)
            #print(chave["lname"])
            PEOPLE[item["lname"]] = (i)
    #"""

    #print(type(PEOPLE))
    #print(type(itens))
    #print("\'lname\': \'jose\'" in itens)
    #print(itens)
    return PEOPLE
    #return itens

def read_all():
    PEOPLE = get_dict_from_mongodb()
    dict_clientes = [PEOPLE[key] for key in sorted(PEOPLE.keys())]
    clientes = jsonify(dict_clientes)
    qtd = len(dict_clientes)
    content_range = "clientes 0-"+str(qtd)+"/"+str(qtd)
    # Configura headers
    clientes.headers['Access-Control-Allow-Origin'] = '*'
    clientes.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    clientes.headers['Content-Range'] = content_range
    return clientes


def read_one(lname):
    PEOPLE = get_dict_from_mongodb()
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    else:
        abort(
            404, "Pessoa com sobrenome {lname} nao encontrada".format(lname=lname)
        )
    return person


def create(person):
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    PEOPLE = get_dict_from_mongodb()
    if lname not in PEOPLE and lname is not None:
        item = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        db.clientes.insert_one(item)
        return make_response(
            "{lname} criado com sucesso".format(lname=lname), 201
        )
    else:
        abort(
            406,
            "Pessoa com sobrenome {lname} ja existe".format(lname=lname),
        )


def update(lname, person):
    query = { "lname": lname }
    update = { "$set": {
            "lname": lname,
            "fname": person.get("fname"),
            "timestamp": get_timestamp(), } 
        }
    PEOPLE = get_dict_from_mongodb()

    if lname in PEOPLE:
        db.clientes.update_one(query, update)
        PEOPLE = get_dict_from_mongodb()
        return PEOPLE[lname]
    else:
        abort(
            404, "Pessoa com sobrenome {lname} nao encontrada".format(lname=lname)
        )

def delete(lname):
    query = { "lname": lname }
    PEOPLE = get_dict_from_mongodb()
    if lname in PEOPLE:
        # del PEOPLE[lname]
        db.clientes.delete_one(query)
        return make_response(
            "{lname} deletado com sucesso".format(lname=lname), 200
        )
    else:
        abort(
            404, "Pessoa com sobrenome {lname} nao encontrada".format(lname=lname)
        )

