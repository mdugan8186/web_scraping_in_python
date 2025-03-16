--  ==== introduction to splash ====

-- splash uses a programming language called Lua

-- == in the splash browser user interface ==

-- in the white box at the top you can introduce the website you wan to scrap

-- below is the code we have to write to interact with the javascript website

-- the script will take care of things like clicking on a button, introducing text, and setting waits

-- the parsing will still be done with scrapy


-- == using splash to go to Google and get the HTML code in a screenshot of the website ==

-- in the white box:
-- https://www.google.com/


-- in the terminal:
-- 1. define a function:
function main(splash, args)

    -- 2. url of the website:
    url = args.url

    -- 3. to go to a website with splash use a function called go
    -- wrap this in the assert keyword so if the code breaks we'll get an error message
    assert(splash:go(url))

    -- 4. get the html or png screenshot we have to use the return keyword
    -- for png:
    -- return splash:png()

    -- for html:
    -- return splash:html()

    -- hit Render! to get the screen shot or html and then Script to go back to the code

    -- 5. adding a wait to let the the webpage render correctly:
    assert(splash:wait(2))

    -- 6. defining multiple variables:
    return {
        png = splash:png(),
        html = splash:html()
    }
    -- you will get a screen shot and the html code

-- 7. end:
-- when writing a function in Lua always write end as the last line of code
end



-- == all the code ==
function main(splash, args)
    url = args.url

    assert(splash:go(url))
    assert(splash:wait(2))

    return {
        png = splash:png(),
        html = splash:html()
    }
end