function main(splash, args)
    -- splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")

    --[[
    headers = {
        ['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    splash:set_custom_headers(headers)
    --]]

    splash:on_request(function(request)
            request:set_headers('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
        end)


    splash.private_mode_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(3))
    local all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
    all_matches[2]:mouse_click()
    assert(splash:wait(3))
    splash:set_viewport_full()
    return {
      html = splash:html()
    }
end
  