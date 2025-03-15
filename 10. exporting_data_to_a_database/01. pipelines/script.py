# ==== pipelines ====

# ==  open the pipelines.py file ==

# the already made class has three functions, one is already there from the start (precess_item)

# open_spider - this will be called when a spider starts running

# close_spider - this will be called when a spider finishes the scraping process

# precess_items - it only returns a scraped item


# == show the open and close spider function in action ==

# 1. import logging

# 2. in the open_spider function:
# logging.warning('Spider Opened - Pipeline')

# 3. in the close_spider function:
# logging.warning('Spider Closed - Pipeline')


# == open the setting.py file ==
# 1. use find (Ctrl + F) to look for item:
# it will be located in Configure item pipelines

# 2. uncomment the ITEM_PIPELINES code
# it will define the pipelines Class we are using
# ITEM_PIPELINES = {
#    "transcript_spider.pipelines.TranscriptSpiderPipeline": 300,
# }

# = note =
# if we had two entries in ITEM_PIPELINES whatever one has a lower number will run first because it has a higher priority


# == run the spider ==
# 1. in the terminal:
# scrapy crawl transcripts

# 2. view the output:
# you can see both warning messages. these are the exact moments that the spider will start working and finish
