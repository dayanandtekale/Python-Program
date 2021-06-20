import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
print(client)

print(client.list_database_names())
db = client.Project

coll = db.Projects
for documents in list(coll.find({'id':1},{'_id':0})):
    print(documents)