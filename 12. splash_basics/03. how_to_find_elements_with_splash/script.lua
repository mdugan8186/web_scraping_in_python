-- ==== how to find elements with splash ====

-- == finding the element ==
-- 1. using this webpage https://www.amazon.com go to the search bar, type in books. then inspect the search bar with dev tools.

-- 2. find the element we want:
-- id="twotabsearchtextbox"


-- == go pack to the splash homepage ==
-- well use the same code we used for google, the code is the base code for interacting with any website

-- function main(splash, args)
--     url = args.url
    
--     assert(splash:go(url))
--     assert(splash:wait(2))
    
--     return {
--       png = splash:png(),
--       html = splash:html()
--       }
--   end


-- 1. modify the link in the white box:
https://www.amazon.com/

-- 2. create a new variable:
-- input_box = assert(splash:select)
-- select() will select only one element
-- select_all() will select multiple elements

-- 3. we have to use the css selector, we can't use the id or xpath:
-- we write the css selector with the hash sign (#)
-- input_box = assert(splash:select("#twotabsearchtextbox"))

-- 4. using the focus function:
-- before we can send some text to the input box we have to use focus. every time we want to use an element located we have to use the focus function 
-- input_box:focus()

-- 5. send text to the box:
-- input_box:send_text("books")

-- 6. let the page render with another wait:
-- add another wait
-- assert(splash:wait(2))

-- 7. check your code with the render and see if it performs properly:
-- if its good continue

-- 8. go back to the webpage. locate and inspect the search button
-- id="nav-search-submit-button"

-- 9. in splash create a new variable:
-- /button = assert(splash:select("#nav-search-submit-button"))

-- 10. click on the button:
-- button:mouse_click()

-- 11. add another wait to let the page render the results:

-- 12. render the script:
-- if the page doesn't finish rendering (images are missing from screenshot) add more time to the wait




function main(splash, args)
    url = args.url
    
    assert(splash:go(url))
    assert(splash:wait(2))

    input_box = assert(splash:select("#twotabsearchtextbox"))
    input_box:focus()
    input_box:send_text("books")
    assert(splash:wait(2))

    button = assert(splash:select("#nav-search-submit-button"))
    button:mouse_click()
    assert(splash:wait(2))
    
    return {
      png = splash:png(),
      html = splash:html()
      }
  end