from pymongo import MongoClient
uri = "mongodb://tohidsk155_db_user:<password>@ac-esclzrn-shard-00-00.bbg34sg.mongodb.net:27017,ac-esclzrn-shard-00-01.bbg34sg.mongodb.net:27017,ac-esclzrn-shard-00-02.bbg34sg.mongodb.net:27017/?ssl=true&replicaSet=atlas-13xyv3-shard-0&authSource=admin&appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)