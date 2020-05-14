from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class insta:
  def __init__(self,username,password):
    self.username=username
    self.password=password
    self.bot=webdriver.Firefox()

  def login(self):
    bot=self.bot
    bot.get('https://www.instagram.com/')
    time.sleep(4)
    email=bot.find_element_by_class_name('_2hvTZ.pexuQ.zyHYP')
    password=bot.find_element_by_name('password')
    email.clear()
    password.clear()
    email.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(10)
    try:
      bot.find_element_by_class_name('aOOlW.HoLwm').click()
      time.sleep(5)
    except Exception as exp:
      time.sleep(4)

  def follow(self,name):
    self.name=name
    bot=self.bot
    time.sleep(5)
    bot.get("https://www.instagram.com/{}/". format(name))
    time.sleep(20)
    bot.find_element_by_class_name("_5f5mN.jIbKX._6VtSN.yZn4P").click()


sel=insta('_fifty_shades_of_us_','Aryman@235')
sel.login()
sel.follow("akshaykumar")

            
          
      
      
