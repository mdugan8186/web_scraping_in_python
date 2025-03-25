# ==== using splash with scrapy ====

# == update the lua/ splash code ==
# 1. change the return:
# change the return from this:
# return {splash:png(),splash:html()}

# to this:
# return {
#     html = splash:html(),
#   }

# the original is god for testing the script and seeing the screenshot of the page. but when run in scrapy scrapy will think it's working with a json response so the xpath will fail


# == create a new project ==
# 1. in the terminal:
# scrapy startproject splash_project

# 2. cd the new folder:

# 3. create a new spider:
# scrapy genspider adamchoi www.adamchoi.co.uk/overs/detailed


# == get code from github ==
# https://github.com/scrapy-plugins/scrapy-splash

# 1. install scrapy-splash in the terminal:
# pip install scrapy-splash


# == go to setting.py ==
# 1. copy and paste code at the bottom of the page:
# SPLASH_URL = 'http://192.168.59.103:8050'

# 2. change the web address to :
# SPLASH_URL = 'http://localhost:8050'

# 3. copy and paste code at the bottom of the page:
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }

# 4. copy and paste code at the bottom of the page:
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# 5. copy and paste code at the bottom of the page:
# REQUEST_FINGERPRINTER_CLASS = 'scrapy_splash.SplashRequestFingerprinter'


# == go to the spider folder ==
# 1. copy the code we wrote in splash:
# change it now if you didn't change it earlier

# 2. create a variable:
# create a variable named script with triple quotes and paste the splash code in it

# 3. comment out the starts_urls variable:

# 4. add localhost:
# in allowed_domains add localhost to it
# allowed_domains = ["www.adamchoi.co.uk", "localhost"]

# 5. import a library:
# from scrapy_splash import SplashRequest

# 6. define a new function:
# in it use a yield and SplashRequest then paste the website we're going to scrape in it

# def start_requests(self):
#         yield SplashRequest(url='https://www.adamchoi.co.uk/overs/detailed')

# 7. add the second argument (callback):
# callback=self.parse

# 8. add a third argument (endpoint):
# endpoint='execute'

# 9. add a fourth argument (args):
# this will call the script variable we defined above
# args={'lua_source': self.script}

# 10. add a fifth argument (meta):
# this tells scrapy to treat the response as html even though it's coming from the splash execute endpoint. without it scrapy assumes it got json and response.xpath() throws an error
# meta={'splash': {'response_type': 'html'}}


# == print the body to check if the code works ==
# 1. in the parse function:
# add a print, this will test the code to see if it's working
# print(response.body)


# == test the code ==
# REMEMBER TO HAVE SPLASH OPEN IN THE BROWSER WITH THE NAME OF THE WEBSITE IN THE WHITE BOX AND THE CODE IN THE OTHER BOX
# 1. in the terminal:
# scrapy crawl adamchoi
