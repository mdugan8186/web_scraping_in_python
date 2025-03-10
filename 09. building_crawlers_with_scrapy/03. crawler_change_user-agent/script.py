# ==== crawler - changing user-agent ====

# == changing the user agent in settings.py ==
# 1. in the settings.py file change the user agent in the DEFAULT_HEADERS

# 2. you can also change the user agent in the USER_AGENT variable


# == changing the user agent inside the spider ==
# 1. create a user_agent variable:
# above the rules create a variable called user_agent

# 2. set the user agent:
# use the user agent you copied before or use a new one from an alternate source

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'

# 3. create a start_request function:

# 4. make a yield:
# yield.scrapy.Requests()

# 5. set the arguments:
# a. argument 1 - the start_urls link. url= :
# url='https://subslikescript.com/movies_letter-X'

# b. comment out the start_url variable now

# c. argument 2 - the new user-agent. headers= :
# headers={'user-agent': self.user_agent}


# == edit the rules and making a function ==
# 1. add extra argument to the first and second rule:
# process_request='set_user_agent'

# 2. create a set_user_agent function under the rules:
# have 3 parameters self, request, and spider

# 3. create a variable in set_user_agent:
# request.headers['User-Agent'] = self.user_agent

# 4.return request:


# == showing we changed the user-agent ==
# 1. add a user-agent in the parse_item yield:
# 'user-agent': response.request.headers['User-Agent']


# == run the spider ==
# 1. scrapy crawl transcripts
