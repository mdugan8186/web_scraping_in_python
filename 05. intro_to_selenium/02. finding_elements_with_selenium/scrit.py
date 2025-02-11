# ==== how to find elements wih selenium(theory) ====

# == locating elements ==

# = to find a single element (returns a single element) =
# driver.find_element

# = to find a multiple element (returns a list)  =
# driver.find_elements


# = attributes =
# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

# = specify which attribute with By =
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")


# = other things you can locate with selenium =
# dropdowns
# logins
# waits


# == examples ==

# = test site =
# <article class ="main-article">
#     <h1> Titanic(1997) </h1>
#     <p class ="plot" > 84 years later... </p>
#     <p class ="plot2" > In the end ... </p>
#     <div class ="full-script">
#     "13 meters. You should see it. "
#     "Okay, take her up and over the bow rail. "
#     </div>
# </article>

# driver.find_element(By.CLASS_NAME, "main-article")
# driver.find_element(By.CLASS_NAME, "plot")
# driver.find_element(By.CLASS_NAME, "full-script")

# driver.find_element(By.TAG_NAME, "h1")
# driver.find_element(By.TAG_NAME, "p")
# driver.find_element(By.TAG_NAME, "div")
