# ==== scraping data from multiple links ====

# == locating the table xpath ==
# to get the xpath for the first table we will surround the xpath with parenthesis and then use square brackets to index the first xpath choice or the first table (the historical population)
# (//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]

# we will keep adding slashes to get further into the element
# (//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody

# then
# (//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr


# == to store the data in a file ==
# for a json file:
# inn the terminal type in:
# scrapy crawl worldometers -o population.json

# for a csv file:
# inn the terminal type in:
# scrapy crawl worldometers -o population.csv


# == to add the country name into the scraped data ==
# we will use the meta argument for this in the relative url yield we have
