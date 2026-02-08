from dataclasses import dataclass
import os
import pymongo
from pymongo import MongoClient

@dataclass

class EnvironmentVariable:
    mongo_db=os.getenv("MONGO_DB_URL")



env_var=EnvironmentVariable()


mongo_db_client=pymongo.MongoClient(env_var.mongo_db)