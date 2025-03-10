# ==== crawler - rules ====

# the spiders we were working with were using the default template, which is the basic template


# == to see the other spiders we can work with ==
# 1. open the terminal:
# scrapy genspider -l

# this shows all the available templates
# Available templates:
#   basic
#   crawl
#   csvfeed
#   xmlfeed


# == creating a new spider with the crawl template ==

# 1. open the terminal:
# scrapy genspider -t crawl transcripts subslikescript.com/movies

# 2. add custom_settings:
# custom_settings allow you to override the default setting for a specific spider instead of modifying the global setting for all your  spiders. there are many options we can add here. these options will help us from getting blocked or throttled and mimic human behavior since some websites restrict how often a scraper can send requests in a short period of time

# 3. add a DOWNLOAD_DELAY:
# add a DOWNLOAD_DELAY of 0.5 in custom_setting

# 4. adjust the rules:
# the rules has 3 arguments

# a. LinkExtractor():
# this is used to specify the links you want to extract or not extract. there are several options (arguments) we can sse here. we will use the restrict_xpath which restricts the region we want the crawl spider to extract the links

# b. callback method:
# this is set to a string, unlike what we've seen in the basic template. in the crawl spider it must be defined as a string

# c. follow:
# this a boolean argument and when it's set to True it will send our links to the LinksExtractor

# 5. # change the LinkExtractor to restrict_xpaths=('')
# when we locate the xpath we want to use we will enter it in between the brackets

# 6. get the xpath:
# we will find the xpath for the list of movies
# //ul[@class="scripts-list"]/li/a

# 7. add this to the restrict_xpath('') argument:
# this will only follow the links that have this xpath
# - notice we didn't add the /@href. this is because the LinkExtractor object will automatically search for the href attribute so we have to omit the href

# 8. add a print statement to parse function:
# delete the default code and add print(response.url) to test the code out

# 9. test the code:
# in the terminal
# scrapy crawl transcripts


# == click on one of the movies to scrapy the website ==
# 1. find the xpath for the main article:
# //article[@class='main-article']

# 2. find the title:
# //article[@class='main-article']/h1

# 3. find the plot:
# //article[@class='main-article']/p

# 4. adjust parse_item:
# in parse_item remove the print statement and add an article variable with a response and xpath
# article = response.xpath("//article[@class='main-article']")

# 5. add a yield for data we will scrap:
# use the article as your context and the ./ method. the (.) is to specify the current context and the (/) is for the immediate child nodes

# 6. get the xpath for the transcript:
# - remember we have to follow the hierarchy of the html with scrapy
# //article[@class='main-article']div[@class='full-script']/div[@class='subtitle-cue']/p[@class='cue-line']
# - we will only need this part because we already have //article[@class='main-article'] in a variable
# div[@class='full-script']/div[@class='subtitle-cue']/p[@class='cue-line']


#  7. make a transcript variable in the yield:
# use the same ./ method

# 8. get the text with /text() and .get() or .getall()

# 9. add the response.url to the yield:


# == avoid getting weird values ==
# if your version of scrapy doesn't support UTF-8 by default so we have to add it in setting.py

# 1. on the very last line add:
# FEED_EXPORT_ENCODING = "utf-8"


# == run the script and save to a file ==
# 1. in the terminal:

# to run:
# scrapy crawl transcripts

# to run and create and store the data in a file:
# scrapy crawl transcripts -o transcripts.csv
