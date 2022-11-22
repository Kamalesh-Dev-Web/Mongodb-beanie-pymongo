import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie

from bson.objectid import ObjectId



class posts(Document):
    name: str
    age: int
    
    
async def example():
    # Beanie uses Motor async client under the hood 
    client = AsyncIOMotorClient("mongodb+srv://kamalesh-mongo:5b9SVwxps38mE@cluster0.h5lf0.mongodb.net/?retryWrites=true&w=majority")

    # Initialize beanie with the Product document class
    await init_beanie(database=client.blogs, document_models=[posts])

   
    # Beanie documents work just like pydantic models
    tonybar = posts(name="Kamal", age=25, )
    # And can be inserted into the database
    await tonybar.insert() 
    
    
    # delete_user=await posts.get('637cf875771ba2bc0b52a4cb')
    delete_user=await posts.find(posts.name=="chando").delete()
    
    print(delete_user)
    
    
    
    
    # You can find documents with pythonic syntax
    # product = await Posts.find_one(Posts.age < 90)
         
    # And update them
    # await product.set({Product.name:"Gold bar"})


if __name__ == "__main__":
    asyncio.run(example())