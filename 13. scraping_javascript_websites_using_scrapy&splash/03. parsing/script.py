# ==== parsing ====

# with the lua code we wrote we obtained the html of the website

# == go to the website to build the xpath that we need to extract the data ==
# we are going to look at the td so we can then look at the tr
# 1. within inspect use find:
# //tr

# to cycle through the entries use a square bracket
# for the date:
# //tr/td[1]

# 2. create a rows variable:
# replace the print(response.body) with rows = response.xpath('//tr')

# 3. make a for loop:

# 4. build the variables in the for loop with the xpaths:
# remember to use the ./ to use the current context for the row variable made earlier
# date = row.xpath('./td[1]/text()').get()

# 5. yield each variable:
# yield {
#     'date': date,
#     'home_team': home_team,
#     'score': score,
#     'away_team': away_team
# }


# == run the spider ==
# 1. in the terminal:
# scrapy crawl adamchoi


# == save the data in a csv or json file ==
# 1. in the terminal:
# scrapy crawl adamchoi -o football_data.json


# == notes about timezone ==
# if the date in your json file is different than the date on your browser it because your browser is adjusting the date based on your timezone, which is different than where the information was uploaded and where the server is located. the timezone for this is in the UK. to be sure, look at the screenshot from the splash code, whatever dates are on that are the correct dates, and this is the date that will be in your json file
