# ==== scrapy's shell command ====

# before scraping the website test your code with a shell command

# to exit the shell terminal use:
# Ctrl + D
# or
# exit()

# to clear the terminal in the shell:
# Ctrl + L


# 1. inspect the website

# 2. locate the element:
# h1

# 3. use command+F to use find to check the Xpath:
# //h1

# 4. in the terminal write:
# scrapy shell
# when you get the 3 arrows (>>>) you are in shell mode

# 5. in the terminal run the commands:

# = for request =
# r = scrapy.Request(url='https://www.worldometers.info/world-population/population-by-country/')

# = to fetch =
# fetch(r)

# = to see the html of the website =
# response.body

# = to get a specific element =
# inside write the xpath expression we used before
# response.xpath('//h1')

# to get the text without the element
# response.xpath('//h1/text()')

# to get only the text
# response.xpath('//h1/text()').get()


# == another example ==
# get the country names from the list
# //td/a

# write this in the terminal (this will return a list)
# response.xpath('//td/a/text()').getall()
