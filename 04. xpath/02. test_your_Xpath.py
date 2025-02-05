# ==== test your Xpath ====

# use this website with this data to test your xpath expression
# https://scrapinghub.github.io/xpath-playground/

# <article class ="main-article">
#     <h1> Titanic(1997) </h1>
#     <p class ="plot" > 84 years later... </p>
#     <p class ="plot2" > In the end ... </p>
#     <div class ="full-script">
#     "13 meters. You should see it. "
#     "Okay, take her up and over the bow rail. "
#     </div>
# </article>


# examples

# //h1 = <h1> Titanic(1997) </h1>
# //h1/text() = Titanic(1997)

# //p = <p class="plot"> 84 years later... </p>
# and
# <p class="plot2"> In the end ... </p>

# //div = <div class="full-script"> "13 meters. You should see it. " "Okay, take her up and over the bow rail. " </div>
# //div/text() = "13 meters. You should see it. " "Okay, take her up and over the bow rail. "

# //p[1] = <p class="plot"> 84 years later... </p>

# //p[2] = <p class="plot2"> In the end ... </p>

# == standard Xpath expression ==
# //div[@class='full-script] = <div class="full-script"> "13 meters. You should see it. " "Okay, take her up and over the bow rail. " </div>

# //div[@class='full-script']/text() = "13 meters. You should see it. " "Okay, take her up and over the bow rail. "

# //p[@class='plot']/text() = 84 years later...


# == logical operators ==
# //p[(@class='plot') or (@class='plot2')] = <p class="plot"> 84 years later... </p>
# <p class="plot2"> In the end ... </p>


# == functions ==
# //p[contains(@class, 'plot')] = <p class="plot"> 84 years later... </p>
# <p class="plot2"> In the end ... </p>

# //div[contains(@class, 'script')] = <div class="full-script"> "13 meters. You should see it. " "Okay, take her up and over the bow rail. " </div>
