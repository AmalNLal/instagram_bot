from instagram import insta

def story(self):
  bot=self.bot
  bot.find_element_by_class_name('OE3OK').click()
  time.sleep(9)
  try:
    for i in range(40):
      time.sleep(5)
      bot.find_element_by_class_name('coreSpriteRightChevron').click()
  except Exception  as exp:
    time.sleep(10)

story()
