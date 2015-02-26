import pymongo 


connMongo = pymongo.Connection()
print connMongo.database_names()

connMongo.close()


