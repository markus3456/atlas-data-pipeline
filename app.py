import os
import json
import pandas as pd
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
Channel_id = 'abcd'
path = "C:/Users/marku/Projects/Python_Projects/MongoDB_Atlas/json_output"

def test_db_connection(destination):
    # Create a new client and connect to the server
    client = MongoClient(destination, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def extract(api_key, Channel_id, search):

    yt = YTstats(api_key, Channel_id, search)
    #yt.get_channel_statistics()
    #yt.get_channel_video_data()
    yt.get_videos_by_search()
    #yt.dump()
    yt.dump2()


def transform(original_file):
    # Step 1: Read the Original JSON File
    with open(original_file, 'r') as file:
        #original_data = json.load(file)
        original_data = json.load(file)

    # Step 2: Parse and Extract Information
    
    
    video_stats = original_data

    sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True)
    stats = []
    for vid in sorted_vids:
        video_id = vid[0]
        date = vid[1]["publishedAt"]
        title = vid[1]["title"]
        views = int(vid[1]["viewCount"])
        likes = int(vid[1].get("likeCount",0))
        comments = int(vid[1].get("commentCount",0))
        stats.append([title, video_id, date, views,likes,comments])

    df = pd.DataFrame(stats, columns=["title","video_id","date","views","likes","comments"])
    print(df.head(10))
    


    for index, row in df.iterrows():
        # Convert the row to a dictionary
        row_dict = row.to_dict()

        # Define the filename based on a unique identifier (e.g., index or a specific column)
        filename = f"{row['video_id'].lower().replace(' ', '_')}_data.json"
        output_directory = 'json_output/'
        # Define the full file path
        file_path = output_directory + filename

        # Save the row as a JSON file
        with open(file_path, 'w') as json_file:
            json_file.write(json.dumps(row_dict, indent=2))

    print(f"{index + 1} Items saved to {output_directory}")
    

def load(destination, path):
    client = MongoClient(destination, server_api=ServerApi('1'))
    db = client['youtube-analytics']  # Replace 'your_database' with your actual database name
    collection = db['caferacer_stats']  # Replace 'your_collection' with your actual collection name


    # Step 4: Insert Documents into MongoDB
    json_folder_path = path

    # Iterate through JSON files in the folder
    for filename in os.listdir(json_folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(json_folder_path, filename)

            # Read the JSON file
            with open(file_path, 'r') as file:
                json_data = json.load(file)

            # Insert the document into MongoDB
            collection.insert_one(json_data)
    print ("objects succesfully uploaded")
a = test_db_connection(mongodb_url)
#b = extract(api_key, Channel_id, search)
#c = transform(file)
d = load(mongodb_url, path)

