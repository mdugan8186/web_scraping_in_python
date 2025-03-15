# ==== MongoDB ====

# == update pipelines in the pipelines.py file ==
# 1. change the name of the class to MongoDBPipeline

# 2. import pymongo


# == connect to the cluster ==
# 1a. crate a self.client variable:
# in the open_spider function create a variable
# self.client = pymongo.MongoClient("mongodb+srv://michael:<db_password>@cluster0.tytid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# = note =
# the string for this can be found in the mongoDB webpage. go to clusters/ connect/ drivers
# driver: python, version: (your version)

# 1b. change the password to the password you created for yourself

# = example of where to put the password =
# mongodb+srv://michael:******@cluster0.tytid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

# 2. self.db = self.client['My_Database']

# 3. close the database:
# in the close_spider function create a variable
# self.client.close()

# 4. create a variable to store scraped data:
# collection_name = 'transcripts'

# 5. insert each item that was scraped:
# in the process_item function
# self.db[self.collection_name].insert_one(dict(item))
# return item


# == go to the spiders file ==
# 1. comment out the user-agent and uncomment the transcript in the yield


# == go back to the setting.py file ==
# 1. edit the ITEM_PIPELINES:
# change the name of the pipeline (TranscriptSpiderPipeline) to (MongoDBPipeline). this is the class name we created in the pipelines.py file

# before:
# ITEM_PIPELINES = {
#     "transcript_spider.pipelines.TranscriptSpiderPipeline": 300,
# }

# after:
# ITEM_PIPELINES = {
#     "transcript_spider.pipelines.MongoDBPipeline": 300,
# }


# == run the code ==
# 1. in the terminal:
# scrapy crawl transcripts


# == view the data ==
# 1. in the mongDB webpage go to clusters and then got to browse collections
