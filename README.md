**Data Pipeline from Youtube API to MongoDB Atlas Database**


**Overview**

This App facilitates the capability of extracting Data from a Youtube API transforming the data using Python and uploading individual .json documents to a MongoDB Database on Atlas (Cloud). 
It can analyzed video stats such as view count, likes, comments and more of entire youtube channels or individual videos based on a given search term. 

**Deployment**

This app can run in any Python supported environment. The whole directory should be copied into the working directory. All neccessary libaries can be installed using the requirements.txt file. 
To extract Data from Youtube API, a API Key is required and can be configured on https://developers.google.com/youtube/v3.
To load Data to the MongoDB Atlas Database a registraion on MongoDB and the URI to your Database is required. 

**Requirements:**

- Python 3
- installation of following libaries (can be installed using requirements.txt)
  - pymongo
  - requests
  - ipython
  - python-dotenv
  - pandas
- MongoDB Atlas Account and Database and URI
- Youtube API Key

  
