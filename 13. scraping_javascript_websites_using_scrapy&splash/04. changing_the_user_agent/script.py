# ==== changing the user agent ====

# == changing the user agent in splash ==
# if the user agent isn't changed plash will use the default user agent and that is not a good practice because it will reveal that we're using splash to scrap the website. we have to change the user agent so that it looks like we're sending requests using chrome


# method 1 (easiest way):
# add this in the splash code at the top

# splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")


# method 2:
# this will also help us override other request headers
# we will set the custom headers to the one we just created

# headers = {
#         ['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
#     }
# splash:set_custom_headers(headers)


# method 3:
# this will help you change the user agent or the header, but will also register a callback function that will be called on each request

# splash:on_request(function(request)
#             request:set_headers('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
#         end)
