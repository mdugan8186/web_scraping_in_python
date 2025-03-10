# ==== crawler - pagination ====

# == pagination using the crawl template ==

# 1. find the xpath for the next page:
# //a[@rel='next']

# 2. to chose between the first of second button we will use square brackets to chose the first one
# (//a[@rel='next'])[1]

# 3. create a new rule:
# a. under the rules duplicate the first Rule
# b. change the xpath in the duplicate Rule
# c. remove the callback and follow in the duplicate.
#
# = note: =
# the reason we can delete the callback is because we already set the callback to parse.item. we can get ride of follow is because we're not specifying the callback argument.

# = note: =
# the order in the rules matters, if the second rule was in the first position we would not scrap the first page

# rules = (
#         Rule(LinkExtractor(
#             restrict_xpaths="//ul[@class='scripts-list']/li/a"), callback="parse_item", follow=True),
#         Rule(LinkExtractor(
#             restrict_xpaths="(//a[@rel='next'])[1]")),
#     )


# == scrap less pages ==

# so were not scraping hundreds of pages and transcripts we'll comment out the transcript key/value pair in the yield that gets the transcripts and go to the X page

# 1. comment out the transcript key/value pair

# 2. go to the X page and copy the link and paste it into the start_url variable


# == run the spider ==

# 1. in a terminal:
# scrapy crawl transcripts -o transcripts_letter_x.json
