from pymongo import MongoClient
user = 'root'
password = 'Mjg4MjctZWZpZ2lh' 
host='localhost'
#create the connection url
connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)


# connect to mongodb server
print("Connecting to mongodb server")
connection = MongoClient(connecturl)


# get database list
print("Getting list of databases")
dbs = connection.list_database_names()

# print the database names

for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")


# select the 'training' database 
db = connection.training

# select the 'python' collection 
collection = db.python

# create a sample document
doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}

# insert a sample document
print("Inserting a document into collection.")
collection.insert_one(doc)

# query for all documents in 'training' database and 'python' collection
docs = collection.find()
print("Printing the documents in the collection.")

for document in docs:
    print(document)


collection2 = db.mongodb_glossary

# create documents
docs = [{"database":"a database contains collections"},
    {"collection":"a collection stores the documents"},
    {"document":"a document contains the data in the form of key value pairs."}]

# insert documents
print("Inserting documents into collection.")
collection2.insert_many(docs)

# query for all documents in 'training' database and 'python' collection
collection2.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)
    
# close the server connecton
print("Closing the connection.")
connection.close()