import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from youtube_stats import YTstats


# Load environment variables from .env file
load_dotenv()

# Access environment variables
mongodb_url = os.getenv("MONGODB_URL")
api_key = os.getenv("API_KEY")

#search variables
search = 'cafe racer'
file = 'search.json'

def test_db_connection(destination):
    # Create a new client and connect to the server
    client = MongoClient(destination, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def extract():

    yt = YTstats(api_key, search)
    #yt.get_channel_statistics()
    #yt.get_channel_video_data()
    yt.get_videos_by_search()
    #yt.dump()
    yt.dump2()

a = test_db_connection(mongodb_url)