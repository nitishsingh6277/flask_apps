from pymongo import MongoClient

# Replace the connection URL with your own
#connection_url = 'mongodb+srv://nitishsingh6277:Newton_6277@atlas-sql-6425b6deee835125f8aa810b-6qsoj.a.query.mongodb.net/Nitishdb?retryWrites=true&w=majority'
# connection_url = 'mongodb+srv://nitishsingh6277:Newton_6277@cluster0.igm7idq.mongodb.net/Nitishdb?retryWrites=true'
connection_url = 'mongodb+srv://nitishsingh6277:Newton_6277@cluster0.igm7idq.mongodb.net/?retryWrites=true&w=majority'
# Create a MongoClient object
client = MongoClient(connection_url)
db = client.test 
print(db)
# Access your database
database = client['Nitishdb']
data = [{
    "name" : "sudh",
    "class": "data science",
    "time": "filwx"
},
{
    "name" : "sudh",
    "class": "data science",
    "time": "filwx"
},
{
    "name" : "sudh",
    "class": "data science",
    "time": "filwx"
},
{
    "name" : "sudh",
    "class": "data science",
    "time": "filwx"
},
{
    "name" : "sudh",
    "class": "data science",
    "time": "filwx"
}]
collections = database["db_record"]
collections.insert_many(data)
print(collections)

# Perform database operations
# Example: Retrieve all documents in the collection
documents = collections.find({'time':'filwx'})
print(collections.find_one())
print('sss')
for document in documents:
    print(document)

# Close the connection
client.close()

