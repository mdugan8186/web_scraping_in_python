# ==== building the script with splash ====

# == before using splash check to see if a website runs javascript ==
# 1. inspect the website:

# 2. go to the setting:

# 3. find the debugger:
# click on disable javascript

# 4. reload the page:
# if the page doesn't load at all it means that it runs javascript

# 5. restore setting:
# unclick the disable javascript button and reload the page. it should go back to loading properly


# == open splash ==
# 1. paste the webpage in the white box:
# https://www.adamchoi.co.uk/overs/detailed

# 2. delete the default code:
# leave the function header and end at the bottom

# 3. tell splash we want to go to the website:
# assert(splash:go(arg.url))
# = note =
# remember to use assert, it will help us debug the code if there's an error

# 4. add a wait:
# the website needs time to load
# assert(splash:wait(3))


# == locate the all matches button ==
# 1. inspect the button:

# 2. locate the css selector:
# == building a css selector ==
# you can build a css selector with the tag name and the class name. you just have to put them together, instead of writing a space use a dot(.). this can be seen when you're inspecting an element

# this selector is long so we'll use the first 3 words in the class name
# label.btn.btn-sm.btn-primary

# == continue in splash ==
# 1. add the selector:
# all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))

# 2. select the button you want:
# since both buttons have the same css selector, pick the second element with square brackets
# all_matches[2]

# 3. add a mouse click:
# all_matches[2]:mouse_click()

# 4. add a wait:
# assert(splash:wait(3))


# == display the whole page ==
# 1. to display the whole page and not just a small window:
# splash:set_viewport_full()


# == return a screenshot and the html code ==
# 1. return the html and png:
# have the png first so you'll get the screenshot first
# return {
#         splash:png()
#         splash:html(),
#     }


# == disable private mode ==
# if the webpage doesn't render correctly
# 1. splash.private_mode_enabled = false

# private mode is the equivalent of googles incognito mode
# if private mode is enables some websites might not render correctly
