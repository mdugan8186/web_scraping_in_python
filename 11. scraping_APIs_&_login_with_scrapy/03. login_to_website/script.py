# ==== login to website - build the spider ====

# this is only an educational video. it is not recommended to scrap a website that require logins. this isn't a good practice because if the website doesn't want to be scraped the owners will ban your IP but also your account. think twice about doing this even if your intentions are good


# == open dev tools ==
# 1. click on the networks tab:

# 2. click All:

# 3. check the Preserve log box:
# this will help store the requests that will be sent when we log in

# 4. refresh the page:

# 5. in the browser:
# type in username and password. because of this website you can use any value
# admin
# *****

# 6. clean up the requests before clicking in the login button:
# in the dev tools click on the cross out button, next to the red circle


# 7. click on the login button:

# 8. open the first request listed:
# click login then click on headers
# the 302 in the status code means we were redirected to the homepage

# 9. click on the payload:
# in the form data you will see the token key, username, and password

#  == note ==
# to log into this website using scrapy we have to provide this form data and then send a post request to the address in the headers request url

# == note ==
# the token is generated dynamically
# to see this go to the page and inspect it with the dev tools. in the username input you will see an attribute set to csrf_token and then there is a token value
# the token value is generated dynamically so if you refresh the webpage the token keeps changing
# later when building the spider we'll copy the token value to send it with the form data


# == create a new spider ==
# 1. crate a new project:
# scrapy startproject api_project

# 2. create the spider:
# scrapy genspider quotes_login quotes.toscrape.com/login


# == in the spider file ==
# 1. define a new variable in the parse function:
# csrf_token = response.xpath('')

# 2. locate the xpath for the csrf value from the form:
# //input[@name='csrf_token']/@value

# 3. paste it into the variable and add .get()
# csrf_token = response.xpath('//input[@name='csrf_token']/@value').get()

# 4. import FormRequest:
# from scrapy import FormRequest

# 5. make a yield with 3 parameters:
# yield FormRequest.from_response(
#             response,
#             formxpath='//form',
#             formdata={

#             }
#         )

# 6. add 3 arguments to the formdata:
# a. the csrf_token - set the value to the token variable we made

# b. username

# c, password

# 7. add the callback argument:
#  callback = self.after_login
# this will help us verify that we're logged in


# == define the after_login function ==
# 1. under the parse function create the function

# 2. to help verify that we're logged in we need to locate the logout button. when you're logged in there is a logout button available.
# //a[@href='/logout']

# 3. get the text:
# //a[@href='/logout']/text()

# 4. create a conditional statement that will help us know if a logout text is on the page:
# if it present then we are logged in
# def after_login(self, response):
#             if response.xpath("//a[@href='/logout']/text()").get():
#                 print('Successfully logged in')


# == run the code ==
# 1. in the terminal run:
# scrapy crawl quotes_login

# verify the code worked:
# use Ctrl + F to search for our printed message
