import pymongo
import certifi

developer = {
    "first"  : "Irvin",
    "last"   : "Zavala",
    "email"  : "irvin.zavala",
    "hobbies": ["chess", "sleep", "basketball"],
    "address": {
        "num": 741,
        "street" : "evergreen",
        "city" : "springfield"
    }
}

con_str = "Secret boi"

client = pymongo.MongoClient(con_str, tlsCAFile = certifi.where())
db = client.get_database("iotStore")