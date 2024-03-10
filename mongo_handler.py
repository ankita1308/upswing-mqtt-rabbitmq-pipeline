import pymongo

# MongoDB configuration
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['mqtt_messages']
mongo_collection = mongo_db['messages']
