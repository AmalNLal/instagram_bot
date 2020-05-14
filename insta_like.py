from instagram import insta

def like(hashtag):
  bot=self.bot
  bot.get("https://www.instagram.com/explore/tags/{}/". format(hashtag))
  time.sleep(15)

  for i in range(20):
    posts = bot.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
    links =[post.find_element_by_css_selector('a').get_attribute('href') for post in posts]
    for link in links:
      bot.get(link)
      try:
        bot.find_element_by_class_name('wpO6b').click()
        time.sleep(10)
      except Exception as exp:
        time.sleep(60)


like("food")
