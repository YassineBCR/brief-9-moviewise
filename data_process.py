import json
import pymongo

mongo_uri = "mongodb://localhost:27017/"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

# Access a specific database
db = client["data_movies"]

db.drop_collection('movies')
db.drop_collection('users')

db.create_collection('movies')
movies = db["movies"]
with open('movielens_movies.json', 'r') as mv:
    for line in mv.readlines():
        movies.insert_one(json.loads(line))

db.create_collection('users')
users = db["users"]
with open('movielens_users.json', 'r') as us:
    for line in us.readlines():
        users.insert_one(json.loads(line))

category = movies.distinct("genres")

# Afficher les catégories
print("Catégories de genres disponibles :")
for genre in category:
    print(genre)