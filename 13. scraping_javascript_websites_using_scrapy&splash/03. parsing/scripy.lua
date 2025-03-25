function main(splash, args)
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
