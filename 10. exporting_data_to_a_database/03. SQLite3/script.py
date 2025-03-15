# ==== SQLite3 ====

# == go to pipelines.py ==

# to work with SQLite we only need to import sqlite3

#  == edit the open_spider function ==
# 1. create a database file:
# this will create a database file, set the name in the parenthesis
# self.connection = sqlite3.connect('transcripts.db')

# 2. create a cursor object:
# this will help execute SQl queries
# self.c = self.connection.cursor()

# 3. write a query:
# this will use a multi-line string and in it we will write the SQL query. it will be the parsed items from our spider file
# self.c.execute('''
#             CREATE TABLE transcripts(
#                 title TEXT,
#                 plot TEXT,
#                 transcript TEXT,
#                 url TEXT
#                        )
#         ''')

# 4. make sure everything is saved:
# self.connection.commit()


# == edit the process_item function:
# 1. create an execute:
# we use a multiline string to write SQL again. in it we write the queries. we use a ? (question mark) for every item we have that we copied from the open_spider
# self.c.execute('''
#             INSERT INTO transcripts (title, plot, transcripts, url) VALUES(?, ?, ?, ?)
#         ''')

# 2. create a second parameter:
# this will list each item that is scraped
# self.c.execute('''
#             INSERT INTO transcripts (title, plot, transcripts, url) VALUES(?, ?, ?, ?)
#         ''', (
#             item.get('title'),
#             item.get('plot'),
#             item.get('transcript'),
#             item.get('url'),
#         ))

# 3. make sure everything is saved:
# self.connection.commit()

# 4. make a try/ except statement:
# to prevent an error and the script from breaking when we run the query for the second or third time. we are creating a table and we can't create a table with the same name, so if we run it a second time we'll get an error that the table already exists. now if the error is raised it will just be passed
# self.c = self.connection.cursor()
#         # query
#         try:
#             self.c.execute('''
#                 CREATE TABLE transcripts(
#                     title TEXT,
#                     plot TEXT,
#                     transcript TEXT,
#                     url TEXT
#                         )
#             ''')
#             self.connection.commit()

#         except sqlite3.OperationalError:
#             pass

# 5. return items that were scraped:
# return item


# == edit the close_spider function ==
# 1. close the connection:
# this will close the connection
# self.connection.close()

# == go to setting.py ==
# 1. edit the ITEM_PIPELINE:
# ITEM_PIPELINES = {
#     "transcript_spider.pipelines.SQLitePipeline": 300,
# }


# == go to the spider.py file ==
# the transcripts we're about to scrap are now arrays/lists. SQLite doesn't support this format so we have to turn them into strings
# the transcript is using getall() which returns a list

# 1. create a variable transcript_list:
# copy the transcript expression
# transcript_list = article.xpath(
#             "./div[@class='full-script']/div[@class='subtitle-cue']/p[@class='cue-line']/text()").getall()

# 2. create a variable transcript_string:
# we will join on transcript_list to concatenate every element of the list. this will turn it into a string
# transcript_string = ' '.join(transcript_list)

# 3. replace the yield transcript expression with the transcript_string we just made
# yield {
#             'title': article.xpath("./h1/text()").get(),
#             'plot': article.xpath("./p/text()").get(),
#             'transcript': transcript_string,
#             'url': response.url,
#             # 'user-agent': response.request.headers['User-Agent'],
#         }


# == run the script ==
# scrapy crawl transcripts


# == view the data ==
# 1. go to this website:
# https://inloop.github.io/sqlite-viewer/#

# 2. drop the file into the drop file box:
# once its dropped all the data should be loaded into the page
