import os
import pprint

from pymongo import MongoClient
from dotenv import load_dotenv

from bson.objectid import ObjectId


load_dotenv()
MONGODB_URL=os.environ['MONGODB_URL']


client=MongoClient(MONGODB_URL)

db=client.blogs

posts_collection=db.posts

print (posts_collection)

new_post={
    'name':'chandhosh',
    'age':'21'
}

new_posts=[
{
    'name':'chandhosh',
    'age':'21'
},
{
    'name':'Hari',
    'age':'55'
}
]

# result=posts_collection.insert_many(new_posts)
# find_document={"age":{"$lt":50}}
update_document={"_id":ObjectId("637b3eeb69568b891a19f972")}

add_age={"$inc":{"age":10}}

result=posts_collection.update_one(update_document,add_age)
# pprint.pprint(result)
# print(result)

count=0

# for doc in result:
#     count+=1
#     pprint.pprint(doc)
#     print()
    

# print(f"no of document available is {count}")

# document_ids = result.inserted_ids
# print(f"_id of inserted document: {document_ids}")
client.close()



