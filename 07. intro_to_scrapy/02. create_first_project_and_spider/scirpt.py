# ==== creating our first project and spider ====

# 1. to start a new project open the terminal and type
# scrapy startproject <project_name> [project_dir]
# scrapy startproject spider_tutorial

# it will give you this message:
# You can start your first spider with:
# cd spider_tutorial
# scrapy genspider example example.com


# 2. start your spider
# cd into the newly created project folder
# cd spider_tutorial

# to start the new spider run the command
# we don't have to use the https:// protocol because scrapy takes care of that part also we dont need the last slash / because scrapy takes care of that too
# website - https://www.worldometers.info/world-population/population-by-country/

# scrapy genspider name_of_spider example.com
# in our case
# scrapy genspider worldometers www.worldometers.info/world-population/population-by-country

# it will return this message and the spider can be found in the spiders folder
# Created spider 'worldometers' using template 'basic' in module:
#   spider_tutorial.spiders.worldometers
