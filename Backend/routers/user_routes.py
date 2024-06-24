from fastapi import APIRouter
from models.user import User
from database.MongoDB import MongoDB
from schema.userSchema import user_serializer,user_list_serializer

user_router =APIRouter()
dbConn= MongoDB()
client,collection=dbConn.connectDB(databaseName="tea-app",collectionName="user")

#POST req 
@user_router.post("/")
async def create_user(user:User):
    collection.insert_one(dict(user))