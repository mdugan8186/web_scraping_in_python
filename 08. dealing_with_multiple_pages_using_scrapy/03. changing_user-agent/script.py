# ==== changing user-agent ====

# == how to see the user agent using scrapy ==

# == using the terminal and shell ==
# 1. in the terminal:
# scrapy shell 'https://www.audible.com/search'

# 2. get the user agent:
# request.headers
# this is the user agent:
#  b'User-Agent': [b'Scrapy/2.12.0 (+https://scrapy.org)']

# we have to change this because the website will recognize we're using scrapy to scrap the website. we need to change the user agent so it looks like we're sending requests using chrome

# to clear the terminal in the shell:
# Ctrl + L

# # to exit the shell terminal use:
# Ctrl + D
# or
# exit()


# == inspecting you browser with dev tools ==
# 1. how to get the user agent you're currently using in your browser:
# 2. go to the browser and right click on inspect
# 3. then go to network
# 4. reload the page and wait for it to finish loading
# 5. go to filter and type in html
# 6. click on any html request
# 7. click on headers
# 8. scroll down to the request headers section
# 9. look for the user-agent
# 10. copy the user_agent


# == changing the user agent ==

# 1. go back to your project folder and open the setting.py file

# 2a. one way to change it is to find the commented out USER_AGENT and change that

# 2b. another way is to find the override the default request header:
# one of the advantages of this option is that you can change all the headers besides user-agent
# a. uncomment it
# b. write 'User-Agent':
# c. paste the user agent you copied from the browser inside quotes
# it should look like this:
# DEFAULT_REQUEST_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# }

# 2c. this method is done inside the script we've written:
# a. we will define a start_request function
# b. we first use the yield keyword
# c. in the scrapy.request
# d. the first argument will be the start_urls webpage
# e. the second argument will be callback=self.parse
# f. in the third argument is going to be the headers with a dictionary value containing the key value pair of 'User-Agent': and the user agent we copied before 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'

# in this user dictionary we can also change other headers besides the user-agent

# 3. comment out the start_urls variable


# 4. since we are using pagination we also need to include the user-agent inside the response.follow
# - we add the third argument of headers with the user agent we copied


# 5. to prove we changed the user-agent:
# we will yield a new element
# in the yield add the key value pair of
# 'User-Agent': response.request.headers['User-Agent']

# this is how to get the user-agent key inside the headers dictionary


# 6. we run the program with the terminal:
# scrapy crawl audible

# to stop it at any time we can use the command:
# Ctrl + Z


# == other user agents ==
# you locate other user agents on this website
# https://explore.whatismybrowser.com/useragents/explore/#google_vignette
