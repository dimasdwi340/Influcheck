import pymongo

client = pymongo.MongoClient("mongodb+srv://dimasdwi340:mypassword@cobaclusterku.osdwh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

def get_data():
    db = client.influcheck
    items = db.datatesting.find()
    items = list(items)
    return items

items = get_data()

for item in items:
    print (f"username {item['username']} are {item['category_name']}")